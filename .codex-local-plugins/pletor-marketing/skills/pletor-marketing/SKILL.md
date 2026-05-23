---
name: pletor-marketing
description: >
  Use this skill for brand marketing work powered by the imported Pletor systems:
  brand analysis, brand guideline extraction, creative direction, product ad
  concepts, static ad prompts, UGC scripts, image prompt enhancement, JSON image
  prompts, video prompt enhancement, JSON video prompts, Kling 3.0 prompts,
  AI model selection, Pletor node planning, and Pletor API agent runs. Trigger
  when the user asks for Pletor, marketing prompts, ad creative, UGC creative,
  image/video generation prompts, brand-safe campaign generation, or reusable
  creative workflows for a company such as jivo.in.
---

# Pletor Marketing

Use this skill to turn brand, product, and campaign context into production-ready
marketing prompts and Pletor workflow plans.

## Operating Rules

- First identify the job type: brand intelligence, static ad, UGC, image prompt,
  video prompt, JSON prompt, Kling prompt, model selection, workflow design, or
  Pletor API run.
- Load only the matching reference file from `references/`.
- Preserve supplied brand facts, product details, packaging claims, compliance
  limits, and marketplace constraints. Mark inferences clearly.
- Ask for missing campaign-critical inputs only when they are required for the
  output format. Otherwise make conservative assumptions and label them.
- For food, wellness, and edible oil marketing, avoid unsupported health,
  medical, disease, cure, weight-loss, or guaranteed outcome claims.
- When building prompts for image or video generation, specify subject, product,
  setting, composition, lighting, action, camera motion, output ratio, and
  negative constraints.
- When the user wants assets for jivo.in, anchor the work in Jivo's real product
  line, packaging, market channel, and existing visual identity before producing
  campaign ideas.

## Reference Router

Brand intelligence:
- `references/brand-intelligence/brand-analyst-skill.md`: use for brand DNA,
  positioning, visual language, photography direction, typography, color, and
  tone-of-voice analysis from a website or brand material.
- `references/brand-intelligence/Brand guidelines extraction.md`: use for a
  neutral, execution-ready brand guidelines document.

Prompt systems:
- `references/prompt-systems/Static Ads Prompter.md`: use for finished static
  ad image prompts with layout, copy treatment, brand alignment, and ad logic.
- `references/prompt-systems/UGC Prompter.md`: use for creator-style UGC concepts,
  shot-by-shot scripts, hooks, captions, and platform-native ad concepts.
- `references/prompt-systems/Image Prompt Enhancer.md`: use to convert loose
  image ideas into detailed visual generation prompts.
- `references/prompt-systems/Nano-banana-prompter.md`: use when the user asks for
  a strong general image-generation prompt in English.
- `references/prompt-systems/JSON Image Prompter.md`: use when an image model
  needs structured JSON prompt output.
- `references/prompt-systems/Video Prompt Enhancer.md`: use to expand a raw video
  idea into cinematic, physically coherent video instructions.
- `references/prompt-systems/JSON Prompter Video.md`: use when a video model or
  workflow needs structured JSON prompt output.
- `references/prompt-systems/Kling 3.0 Prompter.md`: use specifically for Kling
  3.0 natural-language shot sequences with duration accounting.

Workflow building:
- `references/workflow-building/SKILL-model-selection.md`: use to choose image,
  video, lipsync, audio, upscaling, and text models for a Pletor workflow.
- `references/workflow-building/nodes-overview.md`: use to explain or design
  standard Pletor node flows and prompt structures.
- `references/workflow-building/SKILL-advanced-nodes.md`: use for advanced Pletor
  tools, nodes, and workflow patterns.
- `references/workflow-building/pletor-agent.md`: use when the user provides a
  Pletor API key and wants to discover agents, upload assets, create runs, poll
  completion, or download outputs.

## Default Jivo Marketing Workflow

When the task is about jivo.in or Jivo products:

1. Build or refresh a brand brief from the website, product pages, supplied
   images, packaging, price files, and existing campaign material.
2. Extract reusable guardrails: product range, core benefit language, forbidden
   claims, color and packaging cues, audience, usage occasions, and retail
   platform context.
3. Produce campaign routes before prompts: product education, recipe/use-case,
   family kitchen trust, health-conscious cooking without medical claims, value
   comparison, and marketplace conversion.
4. Convert the selected route into the needed output: static ad prompt, UGC
   script, product image prompt, video prompt, JSON prompt, or full Pletor flow.
5. Include iteration notes: what to test, what creative variable changes, and
   what success metric each creative is meant to move.

## Output Discipline

- Deliver the requested artifact directly.
- Include source assumptions and missing inputs only when they materially affect
  the creative result.
- For ad batches, label variants by objective, audience, format, and platform.
- For prompt output, keep the prompt copy ready to paste into the target tool.
- For Pletor workflow output, list nodes in execution order and show required
  inputs, model choices, expected outputs, and failure checks.
