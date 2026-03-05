# OpenAI X投稿 - 2026-03-05

収集元: ローカルRSSHub (localhost:1200)

---

## @OpenAIDevs (OpenAI Developers - 公式開発者アカウント)

**04:06 JST** | [原文](https://x.com/OpenAIDevs/status/2029272237409484819)

> it’s Windows Wensday

---

## @kevinweil (Kevin Weil - 製品責任者)

**04:21 JST** | [原文](https://x.com/kevinweil/status/2029276082663506048)

> We integrated the Codex harness into Prism (http://prism.openai.com) — this means you get skills, reasoning levels, and the raw tenacity of the Codex model in your LaTeX environment. 
> 
> Oh and we also built version mgmt into Prism, which was one of the top requests. 
> 
> See below thread from @vicapow for some great examples of the power of Codex inside Prism 👇
> 
> Victor Powell: 🧵1/ We've brought the most advanced AI to Prism by introducing Codex to Prism. Prism is already the best place for scientific writing to happen—and with Codex, now you can write, compute, analyze, and iterate all in one place.

---

**03:14 JST** | [原文](https://x.com/kevinweil/status/2029259251726860473)

> 💥 AI accelerating high energy physics 
> 
> Just a few weeks after the gluon scattering paper, this morning we posted the more complicated graviton scattering analogue. See below for more from @ALupsasca 👇
> 
> Alex Lupsasca: We just posted a new preprint: “Single-minus graviton tree amplitudes are nonzero.”
> 
> Yes: a helicity sector long assumed to vanish in quantum gravity can actually appear under well-defined kinematics. Preprint: https://cdn.openai.com/graviton/graviton/graviton.pdf

---

## @npew (Peter Welinder - 研究・技術)

**09:07 JST** | [原文](https://x.com/npew/status/2029372701035651353)

> RT Mitchell Hashimoto
> Ahhhh, Codex 5.3 (xhigh) with a vague prompt just solved a bug that I and others have been struggling to fix for over 6 months. Other reasoning levels with Codex failed, Opus 4.6 failed. Cost $4.14 and 45 minutes. Full trace plus includes original issue: https://ampcode.com/threads/T-019cbadf-cb5a-742e-b0e3-2d7164de743f
> 
> I know this prompt is relatively bad. Honestly, our stable release is in a week, and I was throwing some Hail Marys at the frontier models to see if I could get a clean, understandable fix for some of these bugs. By using `gh`, it grabs much better context from the issue, so its not terrible.
> 
> The best thing that Codex did was eventually start reading GTK4 source code. That's where I ended up (see my GH issue), and I knew the answer was somewhere in there, but I didn't have the time or motivation to do it myself. The other models never went there, and lower reasoning efforts with 5.3 didn't go there either. Only xhigh went there. I think that was a critical difference.
> 
> The final fix was decent. It was small, all in a single file, and very understandable. It had one bug I identified (you can see in the trace), and then I manually cleaned up some style. But, it did a great job.
> 
> Definitely an "it's so over" moment. But at the same time, it feels amazing because now our next stable release will have this fix and I was able to spend the time working on other fixes as it went.

---

