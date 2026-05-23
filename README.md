# Jivo Content Creation

A working repository of short-form marketing assets, brand documentation, and a reusable AI creative-production skill for **[Jivo](https://jivo.in)** — an Indian wellness and healthy-food brand best known for cold-pressed canola oil, olive oils, and superfoods.

This repo is the source of truth for the in-house content team: it holds finished creatives, the project docs, and the `pletor-marketing` skill that turns brand context into production-ready prompts for images, videos, UGC, and marketplace ads.

---

## What's inside

| Path | Description |
|------|-------------|
| `Jivo-Assets-2026-05-23/` | Finished image & video creatives (bottle hero, tadka b-roll/sizzle, bottle reveal, hiring video). |
| `docs/` | Project documentation — the full guide to the marketing skill and how to use it. |
| `.codex-local-plugins/pletor-marketing/` | The reusable Codex marketing skill: a router + 14 prompt/workflow reference systems. |
| `downloads/` | Working folder for sourced reference material (e.g. Instagram clips). |
| `Boring Monkee_DSUyCz6CI9i.mp4` | Reference clip. |

### Assets — `Jivo-Assets-2026-05-23/`

| File | Type | Use |
|------|------|-----|
| `01-jivo-bottle-ad-hero.png` | Image | Product hero / ad creative |
| `02-jivo-tadka-broll-frame.png` | Image | Cooking b-roll frame |
| `03-jivo-tadka-sizzle-video.mp4` | Video | Tadka sizzle clip |
| `04-jivo-bottle-reveal-video.mp4` | Video | Product reveal |
| `05-jivo-hiring-unicorn-editors.mp4` | Video | Hiring / recruitment reel |

---

## The `pletor-marketing` skill

A local Codex plugin that gives the AI a **structured operating system** for Jivo marketing work, instead of writing a fresh ad-hoc prompt each time. It routes a request to the right reference system and applies Jivo-specific brand and compliance guardrails.

It can produce:

- **Brand intelligence** — brand DNA analysis and execution-ready brand guidelines
- **Static ad prompts** — Amazon / Flipkart / Blinkit / Instagram creatives
- **UGC scripts** — hook-first, kitchen-native reels with shots, voiceover, on-screen text, and CTAs
- **Image prompts** — enhanced natural-language and structured JSON prompts
- **Video prompts** — cinematic prompts, JSON video prompts, and Kling 3.0 shot sequences with duration accounting
- **Workflow plans** — model selection and Pletor node/API workflows for batch production

**Structure:**

```
.codex-local-plugins/pletor-marketing/
├── .codex-plugin/plugin.json          # Plugin manifest
└── skills/pletor-marketing/
    ├── SKILL.md                       # Main router + operating rules
    ├── agents/openai.yaml             # Skill UI metadata
    └── references/
        ├── brand-intelligence/        # Brand analyst + guidelines extraction
        ├── prompt-systems/            # Static ads, UGC, image, video, JSON, Kling
        └── workflow-building/         # Model selection, nodes, Pletor agent
```

📖 **Full guide:** [`docs/PLETOR_MARKETING_SKILL_GUIDE.md`](docs/PLETOR_MARKETING_SKILL_GUIDE.md) — covers every capability, Jivo brand context, creative pillars, ready-to-use prompt patterns, and compliance guardrails.

---

## Getting started

```bash
git clone https://github.com/daman8271/jivo-content-creation.git
cd jivo-content-creation
```

- **Browse the assets** in `Jivo-Assets-2026-05-23/`.
- **Read the guide** in `docs/` to understand how the marketing skill works.
- **Use the skill** in Codex: trigger it with prompts like
  *"Use Pletor Marketing to create 12 static ad prompts for Jivo Cold-Pressed Canola Oil for Amazon and Instagram."*

---

## Brand & compliance notes

Jivo operates in edible oils and wellness, so all creative output must avoid unsupported health claims (no *cures*, *prevents*, *treats*, *weight-loss guaranteed*, etc.). Use product-led, accurate language (*cold-pressed*, *low in saturated fat*, *rich in MUFA*, *contains Omega-3 fatty acids*). **Final ads still require legal/regulatory review before publishing.** See the guide's compliance section for the full do/don't list.

---

*Internal working repository for the Jivo in-house content team. Assets are for Jivo marketing use.*
