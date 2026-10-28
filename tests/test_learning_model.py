import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lib.learning_model import (ModelResponseError, public_source, read_model_json, capture_evidence,
                                capture_collected, run_model)


class ModelBoundaryTests(unittest.TestCase):
    def test_only_allowlisted_https_sources_are_recaptured(self):
        self.assertEqual(public_source("https://www.anthropic.com/news"), "https://www.anthropic.com/news")
        for url in ["http://www.anthropic.com/", "https://127.0.0.1/", "https://anthropic.com.evil.test/",
                    "https://key@anthropic.com/", "https://anthropic.com:8080/"]:
            with self.assertRaises(ValueError):
                public_source(url)

    def test_model_text_and_usage_are_read_without_treating_logs_as_records(self):
        response = '\n'.join(["startup log", json.dumps({"type": "text", "part": {"text": '{"records":[]}'}}),
                               json.dumps({"type": "step_finish", "part": {"cost": 0.12, "tokens": {"input": 100}}})])
        result, usage = read_model_json(response)
        self.assertEqual(result, {"records": []})
        self.assertEqual(usage["cost"], 0.12)
        _, missing = read_model_json(json.dumps({"type": "text", "part": {"text": '{}'}}))
        self.assertIsNone(missing["cost"])

    def test_invalid_model_output_is_rejected(self):
        for output in ["nothing", '{"type":"text","part":{"text":"Not JSON"}}',
                       '{"type":"text","part":{"text":"[]"}}',
                       json.dumps({"type": "text", "part": {"text": "```json\n[]\n```"}}),
                       json.dumps({"type": "text", "part": {"text": "```json\n[{\"records\":[]}]\n```"}})]:
            with self.assertRaises(ValueError):
                read_model_json(output)

    def test_progress_text_is_not_concatenated_with_final_json(self):
        output = '\n'.join(json.dumps({'type': 'text', 'part': {'text': text}}) for text in
                           ['I will inspect the sources.', 'The tool is finished.', '```json\n{"records":[]}\n```'])
        result, _ = read_model_json(output)
        self.assertEqual(result, {'records': []})

    def test_invalid_final_text_does_not_fall_back_to_earlier_json(self):
        output = '\n'.join(json.dumps({'type': 'text', 'part': {'text': text}}) for text in
                           ['{"records":[]}', 'The collection failed.'])
        with self.assertRaises(ValueError):
            read_model_json(output)

    def test_preamble_or_code_fence_around_one_object_is_unwrapped(self):
        # Run 39883452942 failed in read_model_json at line 1 column 1. The exact
        # ```json wrapper did not match, so a prefixed or differently fenced reply
        # rejected the whole day before validation.
        payload = {"records": [], "reason": "維持"}
        encoded = json.dumps(payload, ensure_ascii=False)
        quoted = {"records": [], "reason": "例は ```json\n{\"records\":[{\"id\":\"x\"}]}\n``` で、採用しない"}
        nested = {"records": [{"nested": {"a": 1}}], "reason": "ok"}
        embedded = {"records": [], "reason": "shown as\n```json\n{\"id\":\"x\"}\n```\nend"}
        samples = [
            (f"分析結果です。\n```json\n{encoded}\n```\n", payload),
            (f"```JSON\n{encoded}\n```", payload),
            (f"``` JSON \n{encoded}\n```", payload),
            (f"```\n{encoded}\n```", payload),
            (f"~~~\n{encoded}\n~~~", payload),
            (f"結果だけ返します。\n{encoded}", payload),
            (f"```json\n補足してから示します。\n{encoded}\n```", payload),
            (f"```json\n{encoded}\n```\n以上です。", payload),
            ("\ufeff" + encoded, payload),
            ("前置き\n" + json.dumps(quoted, ensure_ascii=False), quoted),
            ("```json\n" + json.dumps(nested, ensure_ascii=False) + "\n```", nested),
            ("分析結果です。\n```json\n" + json.dumps(embedded, ensure_ascii=False, indent=2) + "\n```\n補足", embedded),
        ]
        progress = json.dumps({"type": "text", "part": {"text": '{"records":[{"type":"warning"}]}'}})
        for wrapped, expected in samples:
            output = progress + "\n" + json.dumps({"type": "text", "part": {"text": wrapped}}, ensure_ascii=False)
            result, usage = read_model_json(output)
            self.assertEqual(result, expected)
            self.assertNotIn("warning", json.dumps(usage))

    def test_ambiguous_or_broken_final_json_stays_rejected(self):
        encoded = json.dumps({"records": []}, ensure_ascii=False)
        other = json.dumps({"records": [{"id": "x"}]}, ensure_ascii=False)
        samples = [
            f"{encoded}\n補足の文章",
            f"{encoded}{other}",
            f"例:{encoded}\n{other}",
            f"```json\n{encoded}\n```\n```json\n{other}\n```",
            f"```json\n{encoded}\n{other}\n```",
            f"前置き {encoded} 続きの文章",
            "説明だけでJSONがない",
            '{"records":[]',
            '```json\n{"records":[}\n```',
        ]
        for text in samples:
            output = json.dumps({"type": "text", "part": {"text": text}}, ensure_ascii=False)
            with self.assertRaises(ModelResponseError) as caught:
                read_model_json(output)
            self.assertEqual(caught.exception.metadata["status"], "invalid_final_json")
            self.assertNotIn(text, json.dumps(caught.exception.metadata, ensure_ascii=False))
            self.assertNotIn(text, str(caught.exception))

    def test_literal_newlines_inside_one_fenced_object_match_run_40618753545(self):
        # Run 40618753545 blue failed in read_model_json: text_parts 1,
        # final_characters 6969, error line 1 column 1, after PR #4.
        # checkpoint-40618753545-1 is only the verified collect stage.
        # The learning artifact records the same metadata and not the model text.
        # Output was 4397 tokens against a 131072 token cap, so the reply was
        # finished, and the stage requires full markdown section bodies. A
        # preamble or fence around one object whose strings contain those
        # literal newlines reproduces the recorded column-1 failure.
        body = "# 企業\n\n既知の製品と日付を残します。\n- 条件が変わった点を明記します。"
        reason = "今回の更新\nと、変えない理由"
        payload = {"records": [{"type": "dossier_section", "body": body}], "reason": reason}
        raw = ('{\n  "records": [{"type": "dossier_section", "body": "' + body
               + '"}],\n  "reason": "' + reason + '"\n}')
        wrapped = f"今回の判断です。\n```json\n{raw}\n```\n"
        with self.assertRaises(json.JSONDecodeError) as decode_error:
            json.loads(wrapped)
        self.assertEqual((decode_error.exception.lineno, decode_error.exception.colno), (1, 1))
        progress = json.dumps({"type": "text", "part": {"text": '{"records":[{"type":"warning"}]}'}})
        output = progress + "\n" + json.dumps({"type": "text", "part": {"text": wrapped}}, ensure_ascii=False)
        result, usage = read_model_json(output)
        self.assertEqual(result, payload)
        self.assertEqual(usage["json_recovery"], ["string_controls"])
        self.assertNotIn(body, json.dumps(usage, ensure_ascii=False))
        self.assertNotIn("warning", json.dumps(usage))
        direct, direct_usage = read_model_json(json.dumps({"type": "text", "part": {"text": raw}}))
        self.assertEqual(direct, payload)
        self.assertEqual(direct_usage["json_recovery"], ["string_controls"])
        comma = '{\n  "records": [],\n  "reason": "維持",\n}'
        # A trailing comma is syntax, not a second value.
        comma_text = "補足してから示します。\n```json\n" + comma + "\n```"
        parsed, comma_usage = read_model_json(json.dumps({"type": "text", "part": {"text": comma_text}}))
        self.assertEqual(parsed, {"records": [], "reason": "維持"})
        self.assertEqual(comma_usage["json_recovery"], ["trailing_commas"])

    def test_literal_newline_repair_does_not_invent_a_closed_object(self):
        unfinished = '前置き\n```json\n{"records": [], "reason": "一行\n二行"\n```'
        second = json.dumps({"records": [{"id": "x"}]}, ensure_ascii=False)
        doubled = '説明です。\n{"records": [], "reason": "一行\n二行"}\n' + second
        for text in (unfinished, doubled, '{"records": [], "reason": "一行\n二行"}\n' + second):
            output = json.dumps({"type": "text", "part": {"text": text}}, ensure_ascii=False)
            with self.assertRaises(ModelResponseError) as caught:
                read_model_json(output)
            self.assertEqual(caught.exception.metadata["status"], "invalid_final_json")
            self.assertNotIn(text, json.dumps(caught.exception.metadata, ensure_ascii=False))

    def test_source_hash_is_computed_from_received_content(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b"public content"
        opener = MagicMock()
        opener.open.return_value = response
        with patch("lib.learning_model.build_opener", return_value=opener):
            captured = capture_evidence({"url": "https://openai.com/news/", "content_hash": "invented"}, "time")
        self.assertEqual(captured["content_hash"], "sha256:" + hashlib.sha256(b"public content").hexdigest())

    def _model_events(self, text, cost):
        return "\n".join([
            json.dumps({"type": "text", "part": {"text": text}}, ensure_ascii=False),
            json.dumps({"type": "step_finish", "part": {"cost": cost, "tokens": {"output": 10}}}),
        ])

    def test_unreadable_final_json_is_retried_once_and_both_costs_are_kept(self):
        context = {"instructions": "Return the complete collection JSON."}
        bad = self._model_events("説明だけでJSONがない", 0.1)
        good = self._model_events('{"records":[]}', 0.2)
        responses = [MagicMock(stdout="1.18.31\n"), MagicMock(stdout=bad, returncode=0),
                     MagicMock(stdout=good, returncode=0)]
        policy = dict(opencode_version="1.18.31", model="zai/glm-5.1", stage_timeout_seconds=600,
                      max_retries_per_stage=1)
        with tempfile.TemporaryDirectory() as temporary, patch.dict("os.environ", {"GLM_API_KEY": "dummy"}), \
                patch("lib.learning_model.subprocess.run", side_effect=responses) as command:
            result, usage = run_model("blue", context, Path(temporary) / "stage", policy)
        self.assertEqual(result, {"records": []})
        self.assertAlmostEqual(usage["cost"], 0.3)
        self.assertEqual(usage["attempts"], 2)
        self.assertEqual(len(usage["steps"]), 2)
        self.assertEqual(command.call_count, 3)
        self.assertNotIn("説明だけでJSONがない", json.dumps(usage, ensure_ascii=False))

    def test_unreadable_final_json_stays_failed_when_the_retry_is_also_unusable(self):
        context = {"instructions": "Return the complete collection JSON."}
        truncated = self._model_events('{"records": [], "reason": "途中', 0.15)
        responses = [MagicMock(stdout="1.18.31\n"), MagicMock(stdout=truncated, returncode=0),
                     MagicMock(stdout=truncated, returncode=0)]
        policy = dict(opencode_version="1.18.31", model="zai/glm-5.1", stage_timeout_seconds=600,
                      max_retries_per_stage=1)
        with tempfile.TemporaryDirectory() as temporary, patch.dict("os.environ", {"GLM_API_KEY": "dummy"}), \
                patch("lib.learning_model.subprocess.run", side_effect=responses) as command:
            with self.assertRaises(ModelResponseError) as caught:
                run_model("blue", context, Path(temporary) / "stage", policy)
        self.assertEqual(caught.exception.metadata["status"], "invalid_final_json")
        self.assertEqual(caught.exception.metadata["attempts"], 2)
        self.assertAlmostEqual(caught.exception.metadata["cost"], 0.3)
        self.assertEqual(command.call_count, 3)
        self.assertNotIn("途中", json.dumps(caught.exception.metadata, ensure_ascii=False))
        self.assertNotIn("途中", str(caught.exception))

    def test_model_process_failure_is_not_retried(self):
        context = {"instructions": "Return the complete collection JSON."}
        responses = [MagicMock(stdout="1.18.31\n"), MagicMock(stdout="", returncode=1)]
        policy = dict(opencode_version="1.18.31", model="zai/glm-5.1", stage_timeout_seconds=600,
                      max_retries_per_stage=1)
        with tempfile.TemporaryDirectory() as temporary, patch.dict("os.environ", {"GLM_API_KEY": "dummy"}), \
                patch("lib.learning_model.subprocess.run", side_effect=responses) as command:
            with self.assertRaises(ValueError):
                run_model("blue", context, Path(temporary) / "stage", policy)
        self.assertEqual(command.call_count, 2)

    def test_long_context_reaches_model_via_stdin_without_file_line_truncation(self):
        context = {'body': 'a' * 50000, 'instructions': 'Return the complete collection JSON.'}
        events = json.dumps({'type': 'text', 'part': {'text': '{"records":[]}'}})
        responses = [MagicMock(stdout='1.18.31\n'), MagicMock(stdout=events, returncode=0)]
        policy = dict(opencode_version='1.18.31', model='zai/glm-5.1', stage_timeout_seconds=600)
        with tempfile.TemporaryDirectory() as temporary, patch.dict('os.environ', {'GLM_API_KEY': 'dummy'}), \
                patch('lib.learning_model.subprocess.run', side_effect=responses) as command:
            run_model('collect', context, Path(temporary) / 'stage', policy)
            arguments, options = command.call_args
            self.assertEqual(json.loads(options['input']), context)
            self.assertNotIn('--file', arguments[0])
            self.assertIn(context['instructions'], arguments[0][-1])

    def test_recaptured_evidence_and_observations_share_actual_retrieval_time(self):
        original = [{"type": "evidence", "id": "E-1", "retrieved_at": "old"},
                    {"type": "observation", "id": "O-1", "retrieved_at": "old"}]
        with patch("lib.learning_model.capture_evidence", side_effect=lambda r, now: {**r, "content_hash": "hash"}):
            captured, gaps = capture_collected(original)
        self.assertEqual(gaps, [])
        self.assertEqual(captured[0]["retrieved_at"], captured[1]["retrieved_at"])
        self.assertNotEqual(captured[0]["retrieved_at"], "old")
        self.assertEqual(original[0]["retrieved_at"], "old")

    def test_unavailable_source_removes_only_dependent_records(self):
        original = [{'type': 'evidence', 'id': 'E-1', 'url': 'https://openai.com/missing'},
                    {'type': 'evidence', 'id': 'E-2', 'url': 'https://google.com/news'},
                    {'type': 'observation', 'id': 'O-1', 'evidence_ids': ['E-1', 'E-2']},
                    {'type': 'observation', 'id': 'O-2', 'evidence_ids': ['E-2']}]
        for error in [HTTPError(original[0]['url'], 403, 'private error detail', {}, None),
                      URLError('private error detail'), TimeoutError('private error detail')]:
            with patch('lib.learning_model.capture_evidence', side_effect=[error, original[1]]):
                captured, gaps = capture_collected(original)
            self.assertEqual([r['id'] for r in captured], ['E-2', 'O-2'])
            self.assertEqual(len(gaps), 1)
            self.assertNotIn('private error detail', str(gaps))
            self.assertNotIn('retrieved_at', original[1])

    def test_invalid_source_contract_is_not_hidden_as_network_gap(self):
        with patch('lib.learning_model.capture_evidence', side_effect=ValueError('unsafe source')):
            with self.assertRaises(ValueError):
                capture_collected([{'type': 'evidence', 'id': 'E-1'}])


if __name__ == "__main__":
    unittest.main()
