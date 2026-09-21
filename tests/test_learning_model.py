import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from lib.learning_model import public_source, read_model_json, capture_evidence, capture_collected, run_model


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
                       '{"type":"text","part":{"text":"[]"}}']:
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

    def test_source_hash_is_computed_from_received_content(self):
        response = MagicMock()
        response.__enter__.return_value.read.return_value = b"public content"
        opener = MagicMock()
        opener.open.return_value = response
        with patch("lib.learning_model.build_opener", return_value=opener):
            captured = capture_evidence({"url": "https://openai.com/news/", "content_hash": "invented"}, "time")
        self.assertEqual(captured["content_hash"], "sha256:" + hashlib.sha256(b"public content").hexdigest())

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
            captured = capture_collected(original)
        self.assertEqual(captured[0]["retrieved_at"], captured[1]["retrieved_at"])
        self.assertNotEqual(captured[0]["retrieved_at"], "old")
        self.assertEqual(original[0]["retrieved_at"], "old")


if __name__ == "__main__":
    unittest.main()
