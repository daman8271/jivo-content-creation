# Pletor Marketing Skill Guide for Jivo

This document explains the `pletor-marketing` Codex plugin and skill installed in this workspace. It is written as a practical guide for using the skill to plan, generate, and scale brand-safe marketing work for Jivo.

## Executive Summary

The `pletor-marketing` skill turns the Pletor prompt systems from the imported zip into a reusable Codex marketing capability.

Instead of writing a fresh generic prompt each time, the skill gives Codex a structured operating system for:

- Brand analysis
- Brand guideline extraction
- Static ad prompt creation
- UGC script creation
- Image prompt enhancement
- Structured JSON image prompting
- Video prompt enhancement
- Structured JSON video prompting
- Kling 3.0 video prompt creation
- AI model selection
- Pletor workflow node planning
- Pletor API agent execution planning
- Jivo-specific creative guardrails

For Jivo, this matters because the brand is not just selling a product image or a single ad. Jivo needs repeatable creative systems across product pages, Amazon, Flipkart, Blinkit, quick-commerce, reels, UGC, influencer content, recipe content, and brand education. This skill helps Codex produce those assets with a consistent strategy and without repeatedly rebuilding the same prompt logic.

## Installation Status

The skill exists in two locations:

| Location | Purpose |
|---|---|
| `.codex-local-plugins/pletor-marketing` | Workspace-local copy for this Jivo project folder |
| `~/plugins/pletor-marketing` | Personal Codex plugin copy for reuse across sessions |

The plugin was validated after installation.

Key files:

| File | Purpose |
|---|---|
| `.codex-local-plugins/pletor-marketing/.codex-plugin/plugin.json` | Plugin manifest and UI metadata |
| `.codex-local-plugins/pletor-marketing/skills/pletor-marketing/SKILL.md` | Main skill router and operating rules |
| `.codex-local-plugins/pletor-marketing/skills/pletor-marketing/agents/openai.yaml` | Skill UI metadata |
| `.codex-local-plugins/pletor-marketing/skills/pletor-marketing/references/` | The 14 original Pletor reference systems |

## What This Skill Actually Is

This is not just a folder of prompts. It is a reusable Codex skill packaged inside a local Codex plugin.

That means:

- Codex can identify when the user is asking for brand, ad, UGC, image, video, or Pletor workflow help.
- Codex can load the correct reference system instead of loading every prompt at once.
- The skill can be reused in future sessions after Codex is restarted and the plugin is active.
- The Jivo-specific workflow is now embedded into the skill, so future marketing work starts from better assumptions.

The skill is best understood as a marketing production layer for Codex. It does not replace human creative direction. It gives the agent a stronger repeatable method for turning business context into usable creative prompts, campaign plans, and workflow instructions.

## What Is Inside the Skill

The skill contains one main router file and 14 reference systems.

### 1. Main Skill Router

File:

`skills/pletor-marketing/SKILL.md`

This is the first file Codex reads when the skill triggers. It tells Codex how to route a user request.

It handles questions like:

- Is this a brand analysis job?
- Is this a static ad job?
- Is this a UGC scripting job?
- Is this an image prompt job?
- Is this a video prompt job?
- Is this a JSON prompt job?
- Is this a Pletor workflow job?
- Is this specifically for Jivo?

The router also includes Jivo-specific rules:

- Start from the real brand and product context.
- Preserve supplied product facts.
- Avoid unsupported health, cure, disease, weight-loss, or guaranteed-result claims.
- For images and videos, specify subject, product, setting, composition, lighting, action, camera motion, output ratio, and negative constraints.
- For Jivo work, use product range, packaging, marketplace context, and brand identity before generating campaign ideas.

### 2. Brand Intelligence References

These are used when the task is about understanding a brand before creating content.

| Reference | What It Does | Jivo Use |
|---|---|---|
| `brand-analyst-skill.md` | Produces a brand DNA analysis: positioning, visual language, photography, typography, color, and tone of voice | Analyze `jivo.in`, Amazon listings, packaging, competitor pages, or campaign pages |
| `Brand guidelines extraction.md` | Creates a neutral brand guidelines document from public brand assets | Build a Jivo brand rules document for designers, editors, and ad creators |

Use this when asking:

- "Analyze Jivo's brand."
- "Extract brand guidelines from jivo.in."
- "Tell me the visual identity of Jivo."
- "What should our creative team know before making ads?"

### 3. Prompt System References

These convert campaign ideas into asset-ready prompts.

| Reference | What It Does | Jivo Use |
|---|---|---|
| `Static Ads Prompter.md` | Creates finished static ad image prompts with layout, copy treatment, product scene, and brand alignment | Amazon/Blinkit/Flipkart banners, product education creatives, offer ads, comparison ads |
| `UGC Prompter.md` | Creates creator-style UGC concepts, hooks, captions, and shot-by-shot scripts | Reels, influencer scripts, testimonial-style kitchen videos, product demos |
| `Image Prompt Enhancer.md` | Converts loose image ideas into detailed image generation prompts | Product lifestyle scenes, recipe visuals, premium product shots |
| `Nano-banana-prompter.md` | Produces strong general English image-generation prompts | Quick creative image prompts when JSON is not needed |
| `JSON Image Prompter.md` | Produces structured JSON prompts for image models | Repeatable prompt templates for automated workflows |
| `Video Prompt Enhancer.md` | Expands raw video ideas into cinematic, physically coherent video prompts | Reels, product motion ads, recipe videos, lifestyle films |
| `JSON Prompter Video.md` | Produces structured JSON prompts for video workflows | Automated video workflow inputs |
| `Kling 3.0 Prompter.md` | Creates natural-language Kling 3.0 shot sequences with duration accounting | Kling-specific video generation prompts for Jivo product reels |

Use this when asking:

- "Create 20 static ad prompts for Jivo canola oil."
- "Make a UGC script for Jivo extra light olive oil."
- "Turn this product image into a premium prompt."
- "Give me a Kling prompt for a 9-second cooking oil ad."
- "Make JSON image prompts for five Jivo products."

### 4. Workflow Building References

These are used when the task is not just one prompt, but a repeatable generation system.

| Reference | What It Does | Jivo Use |
|---|---|---|
| `SKILL-model-selection.md` | Helps choose image, video, lipsync, audio, upscaling, and text models | Decide which model to use for product shots, UGC, voiceover, or upscaling |
| `nodes-overview.md` | Explains standard Pletor nodes and simple workflow patterns | Plan a Jivo asset generation workflow |
| `SKILL-advanced-nodes.md` | Covers advanced Pletor nodes and workflow patterns | Build more complex batch creative systems |
| `pletor-agent.md` | Explains how to use the Pletor API: discover agent, upload assets, create run, poll, download outputs | Run Pletor agents when an API key is available |

Use this when asking:

- "Design a Pletor workflow for generating Jivo marketplace ads."
- "What nodes do we need for product image to video?"
- "Which models should we use for Jivo product shots?"
- "Use the Pletor API to run this agent."

## Everything This Skill Can Do

### Brand Analysis

The skill can analyze a brand from a website, product pages, or visual references and turn it into a working creative brief.

For Jivo, this can include:

- Brand identity
- Sector and category
- Brand promise
- Audience segments
- Competitive positioning
- Visual identity
- Product photography language
- Typography and layout behavior
- Tone of voice
- Content themes
- Words to use
- Words to avoid
- Creative direction summary

This is useful before generating any ads because Jivo has a specific identity: health-oriented, Indian kitchen friendly, product-led, education-heavy, and rooted in wellness and social purpose.

### Brand Guidelines Extraction

The skill can turn Jivo's public-facing identity into a usable brand guide.

It can extract:

- Brand principles
- Design principles
- Key attributes
- Imagery categories
- Scene and composition rules
- People imagery guidelines
- Framing and lighting principles
- Logo notes, if visible or supplied
- Color palette observations
- Typography observations
- Brand constraints
- Practical recommendations

This is different from brand analysis. Brand analysis is strategic and interpretive. Brand guidelines extraction is more operational and neutral. It creates a reference that a designer, editor, performance marketer, or agency can follow.

### Static Ad Prompting

The skill can create prompts for still ad creatives.

Possible Jivo outputs:

- Amazon product carousel prompts
- Flipkart banner prompts
- Blinkit quick-commerce ads
- Product benefit explainers
- Offer-led creatives
- Comparison creatives
- Lifestyle product shots
- Recipe-use visuals
- Family kitchen trust visuals
- Ingredient-first visuals
- Premium clean product photography
- Festival or regional food moments

A normal prompt might say:

> Create an ad for Jivo canola oil.

The skill produces a much more usable structure:

- Objective
- Audience
- Product focus
- Scene
- Composition
- Copy placement
- Lighting
- Product visibility
- Props
- Background
- Marketplace format
- Negative constraints
- Compliance guardrails
- Variants for testing

### UGC Script Creation

The skill can create creator-style content that feels more native to Instagram, YouTube Shorts, or quick-commerce performance ads.

Possible Jivo outputs:

- Hook-first reel scripts
- Kitchen demo scripts
- "I switched my cooking oil" scripts
- Family meal prep scripts
- Recipe-led scripts
- Marketplace review-style scripts
- Problem-solution scripts
- Comparison-without-attack scripts
- Creator captions
- Shot lists
- Voiceover lines
- On-screen text
- CTA variants

For Jivo, UGC should not feel like a clinical health lecture. It should feel like a real kitchen moment where the product benefit is easy to understand and the food still looks desirable.

### Image Prompt Enhancement

The skill can take a rough idea and turn it into a polished image generation prompt.

Example rough idea:

> Jivo canola oil in an Indian kitchen with healthy food.

The skill can expand it into:

- Product label visible
- Bottle position
- Food context
- Indian kitchen cues
- Lighting
- Surface textures
- Color palette
- Camera angle
- Depth of field
- Aspect ratio
- Negative prompt
- Brand-safe language

This is useful for product mockups, ad backgrounds, concept testing, and visual direction.

### JSON Image Prompting

The skill can create structured JSON for image generation workflows.

This matters when we want repeatability. JSON prompts are easier to feed into automated pipelines than long freestyle prompts.

Possible Jivo JSON fields:

- Concept
- Subject
- Product
- Setting
- Lighting
- Composition
- Color palette
- Camera
- Props
- Copy space
- Negative constraints
- Aspect ratio
- Output style

This is useful if we are building a batch creative generation system for multiple Jivo SKUs.

### Video Prompt Enhancement

The skill can turn a simple video idea into a complete video generation prompt.

Possible Jivo video outputs:

- 6-second product motion prompt
- 9-second recipe reel prompt
- 15-second UGC prompt
- Product pour shot
- Cooking action sequence
- Marketplace conversion video
- Lifestyle kitchen video
- Before-after kitchen switch story, without making medical claims
- Premium product film prompt

The skill adds:

- Shot progression
- Camera motion
- Physical action
- Duration
- Pacing
- Sound direction
- Product continuity
- Visual continuity
- Negative constraints

### JSON Video Prompting

The skill can create structured JSON video prompts.

This is useful when we want:

- Repeatable Pletor video workflows
- Video generation at scale
- Programmatic creative testing
- Different versions by audience, product, or platform

### Kling 3.0 Prompting

The skill has a Kling-specific prompt reference.

Kling prompts need physically coherent shot language and duration accounting. The skill helps create:

- Style line
- Anchor paragraph
- Shot list
- Exact duration split
- Sound line
- Edge-case handling

For example, a 9-second Jivo oil video can be broken into:

- 0 to 2 seconds: product hero
- 2 to 5 seconds: pouring or cooking action
- 5 to 7 seconds: finished dish
- 7 to 9 seconds: packshot and CTA

### AI Model Selection

The skill can help decide which model or generation route is best for a task.

For Jivo:

- Product accuracy matters more than surreal creativity.
- Label clarity matters for marketplace ads.
- Food must look appetizing and realistic.
- Video should be short, clean, and physically plausible.
- Upscaling may be needed before final delivery.
- Lipsync may be useful for founder, dietitian, chef, or creator-style videos.
- Audio generation may be useful for voiceovers.

The model selection reference helps avoid choosing a tool just because it is popular. It frames model choice around the real output we need.

### Pletor Workflow Planning

The skill can design Pletor workflows using node logic.

Example Jivo workflow:

1. Provide brand context.
2. Provide product image.
3. Use Text Assistant to generate prompt variants.
4. Use Generate Image for static ad concepts.
5. Use Image-to-Video for motion variants.
6. Use Upscale for final output.
7. Use Save/Export node for deliverables.

This is useful when we want to go from one-off creative work to a repeatable production engine.

### Pletor API Agent Planning

If a Pletor API key is available, the skill can help plan and execute:

- Agent discovery
- Input inspection
- Asset upload
- Run creation
- Polling
- Output download
- Error handling

Important: this requires an actual Pletor API key and reachable Pletor agents. The skill can guide the execution, but credentials and live API access are still required.

## Why This Is Better Than Normal Prompting

### 1. Normal Prompting Is Temporary

A normal prompt only exists in the current chat. If you ask for an ad today and then ask again next week, the model may use a different structure, tone, or logic.

The skill is persistent. It keeps the method available across future work.

### 2. Normal Prompting Is Easy to Under-Specify

Most ad prompts are too short:

- "Make this premium."
- "Create a viral ad."
- "Make a reel script."
- "Make this better."

Those prompts leave too much to chance.

The skill forces Codex to think in production terms:

- What is the product?
- Who is the audience?
- What is the platform?
- What is the creative objective?
- What visual format is needed?
- What claims are safe?
- What should be avoided?
- What output format does the next tool need?

### 3. Normal Prompting Mixes Strategy and Execution

One-off prompts often jump straight into output. That creates ads that look polished but are not tied to brand strategy.

The skill separates:

- Brand analysis
- Campaign route
- Creative concept
- Prompt generation
- Workflow design
- Testing plan

For Jivo, that prevents generic wellness ads and keeps the work tied to the real product line and marketplace needs.

### 4. Normal Prompting Does Not Remember the Toolchain

Different tools need different prompt styles.

An image model does not need the same prompt as:

- A video model
- Kling
- A JSON workflow
- A UGC script
- A Pletor node system

The skill routes the task to the correct prompt system.

### 5. Normal Prompting Can Drift Off-Brand

Generic AI output may invent claims, change tone, or create visuals that do not fit Jivo.

The skill includes operating rules:

- Preserve real brand facts.
- Do not invent product claims.
- Mark assumptions.
- Avoid unsupported medical or disease claims.
- Use Jivo's product and marketplace context.
- Keep prompt outputs ready for production use.

### 6. Normal Prompting Is Hard to Scale

If we want 100 ad variants for multiple products, one-off prompting becomes messy.

The skill supports batch logic:

- Variants by platform
- Variants by audience
- Variants by product
- Variants by funnel stage
- Variants by creative angle
- Structured JSON for automation
- Pletor node workflows for repeat production

### 7. Normal Prompting Gives Outputs, Not a System

The skill can create:

- The brand brief
- The campaign map
- The prompt set
- The video plan
- The model selection
- The Pletor workflow
- The testing matrix

That makes it a system for marketing production, not just a prompt.

## Jivo Brand Context the Skill Should Use

This section summarizes Jivo context from public Jivo sources and should be treated as working brand context, not legal or regulatory approval.

### Brand Identity

Jivo presents itself as a wellness and healthy food brand built around better daily consumption choices. Its public pages emphasize canola oil leadership, cold-pressed oils, healthier cooking, wheatgrass, superfoods, nutraceuticals, and daily essentials.

Jivo's own "Who We Are" page states that it is a pioneer and leading seller of canola oil and claims a successful PAN India market for cold press canola oil. It also describes the philosophy as "Wellbeing for everyone."

### Origin and Story

Jivo's public story page states that the brand launched around 2010 with a production facility in Kundli, Haryana, and started with canola oil before expanding into wellness products including wheatgrass juices, supplements, olive oil variants, mustard oil, and superfoods.

The story is important for marketing because Jivo is not just a commodity oil brand. It can be positioned as an education-led brand that introduced a newer cooking oil habit to Indian kitchens.

### Social Purpose

Jivo's public pages connect the business to social welfare, education, and the Kalgidhar/Baru Sahib ecosystem. This can become a strong trust layer, but it should be used carefully:

- Use it in brand storytelling.
- Use it in corporate/brand videos.
- Use it in "why Jivo" content.
- Do not force it into every marketplace conversion creative.

### Product Universe

Based on the public Jivo site, the current visible product universe includes:

- Cold-pressed canola oil
- Extra virgin olive oil
- Extra light olive oil
- Pomace olive oil
- Mustard oil
- Sunflower oil
- Soyabean oil
- Wheatgrass drink
- Immunity booster
- Muesli
- Desi ghee
- Natural minerals and other wellness products

For marketing, this means Jivo can be presented as a broader wellness kitchen brand, not just a single canola oil SKU.

### Canola Oil Positioning

Jivo's canola oil pages emphasize:

- Cold-pressed extraction
- Low saturated fat
- High MUFA
- Omega-3 fatty acids
- Sodium free
- Trans fat free
- Cholesterol free
- High smoke point
- Mild flavor
- Daily Indian cooking suitability
- Frying, sauteing, stir-frying, baking, and other kitchen use cases

These are useful pillars for campaign creation.

### Olive Oil Positioning

Jivo's olive oil pages describe:

- Extra Virgin Olive Oil for salads, dips, marinades, chutneys, and premium use cases
- Extra Light Olive Oil with milder taste and higher smoke point for Indian cooking
- Pomace Olive Oil with neutral flavor for frying, sauteing, roasting, and grilling

This gives us clear product segmentation:

- Extra Virgin: fresh, premium, salad, dressing, garnish
- Extra Light: everyday Indian cooking, mild taste, high heat
- Pomace: frying, roasting, grilling, neutral flavor

### Brand Voice Direction

Jivo's current public copy is health-education-heavy. It explains product benefits, process, nutrients, and cooking use cases.

For stronger modern marketing, the skill should help shift the voice from only "benefit listing" into:

- Kitchen-first storytelling
- Simple health-conscious choice language
- Indian cooking compatibility
- Trust and product proof
- Recipe and occasion-led content
- Marketplace conversion clarity

The brand should sound informed and useful, not clinical or exaggerated.

## Recommended Jivo Creative Pillars

### 1. Better Everyday Cooking

Focus:

- Daily Indian kitchen
- Family meals
- Familiar recipes
- Lighter cooking feel
- Neutral taste
- High smoke point

Example content:

- "Your everyday tadka, made with a smarter oil choice."
- "From breakfast to dinner, one oil that fits the Indian kitchen."

### 2. Cold-Pressed Education

Focus:

- What cold-pressed means
- Why extraction method matters
- Difference from heavily processed/refined oils
- Simple visual comparisons

Example content:

- Side-by-side process graphics
- "Directly crushed seeds. No chemical extraction."
- Educational reels with kitchen demonstrations

### 3. Marketplace Trust

Focus:

- Product visibility
- Pack size clarity
- Benefits as scannable badges
- Reviews and proof points where verified
- Quick add-to-cart motivation

Example content:

- Amazon carousel
- Blinkit square creative
- Flipkart hero banner
- Product detail page A+ content

### 4. Indian Recipe Compatibility

Focus:

- Frying
- Sauteing
- Stir-frying
- Baking
- Roasting
- Salad/dressing use cases for olive oil

Example content:

- "Poha to paratha"
- "From stir-fry to baking"
- "Olive oil that does not overpower Indian flavors"

### 5. Wellness Without Overclaiming

Focus:

- Health-conscious choices
- Balanced diet
- Product composition
- Fat profile
- Lifestyle upgrade

Avoid:

- Cure claims
- Disease claims
- Guaranteed transformation claims
- "Reduces diabetes"
- "Prevents heart disease"
- "Fights cancer"
- "Weight loss guaranteed"

Use safer language:

- "Part of a balanced diet"
- "Contains Omega-3 fatty acids"
- "Rich in MUFA"
- "Low in saturated fat"
- "Suitable for everyday cooking"
- "May help maintain normal cholesterol levels when used as part of a balanced diet," only if approved and backed by compliant source language

### 6. Purpose and Trust

Focus:

- Brand story
- Social purpose
- Education and wellbeing mission
- Long-term wellness positioning

Best channels:

- Brand film
- About page
- Corporate deck
- Founder story
- Retailer pitch
- Distributor pitch
- PR assets

## Best Prompt Patterns for Jivo

### Brand Analysis Prompt

Use:

```text
Use Pletor Marketing to analyze https://jivo.in as a brand. Give me brand identity, positioning, visual language, tone of voice, product pillars, audience, and creative direction for future ads.
```

### Brand Guidelines Prompt

Use:

```text
Use Pletor Marketing to extract brand guidelines for Jivo from jivo.in, shop.jivo.in, product images, and the current packaging files in this workspace. Make it useful for designers and ad creators.
```

### Static Ad Prompt

Use:

```text
Use Pletor Marketing to create 12 static ad prompts for Jivo Cold-Pressed Canola Oil. Target Indian families and health-conscious home cooks. Formats: Amazon carousel, Blinkit square, Instagram feed, and Flipkart banner. Keep claims compliant and product-led.
```

### UGC Prompt

Use:

```text
Use Pletor Marketing to create 8 UGC reel scripts for Jivo Extra Light Olive Oil. Make them kitchen-native, creator-led, and suitable for Instagram Reels. Include hook, shots, voiceover, on-screen text, and CTA.
```

### Image Prompt Prompt

Use:

```text
Use Pletor Marketing to convert this idea into premium image prompts: Jivo canola oil bottle on an Indian kitchen counter beside fresh vegetables and a finished family meal. Make 5 variants for different visual styles.
```

### JSON Image Prompt

Use:

```text
Use Pletor Marketing to create structured JSON image prompts for Jivo canola oil, extra light olive oil, and wheatgrass drink. The prompts should be ready for batch generation in a workflow.
```

### Video Prompt

Use:

```text
Use Pletor Marketing to create a 12-second video prompt for Jivo canola oil. Scene: modern Indian kitchen, product hero, cooking action, finished dish, final packshot. Keep movement realistic and product label visible.
```

### Kling Prompt

Use:

```text
Use Pletor Marketing to create a Kling 3.0 prompt for a 9-second Jivo canola oil reel. Include exact shot durations and a sound line.
```

### Pletor Workflow Prompt

Use:

```text
Use Pletor Marketing to design a Pletor workflow that takes one Jivo product image and generates static ads, short video prompts, and UGC scripts for Amazon, Blinkit, and Instagram.
```

## Example Jivo Campaign System

Campaign:

Jivo Cold-Pressed Canola Oil - Everyday Indian Kitchen

Objective:

Increase product understanding and marketplace conversion for Jivo canola oil.

Audience:

Health-conscious Indian home cooks, young families, working parents, and buyers comparing cooking oils online.

Core message:

Jivo Cold-Pressed Canola Oil is a versatile everyday cooking oil for Indian kitchens, with low saturated fat, MUFA richness, Omega-3 fatty acids, and high-heat cooking usability.

Creative routes:

| Route | Purpose | Best Formats |
|---|---|---|
| Better Tadka | Show daily Indian cooking compatibility | Reels, static ads, UGC |
| Cold-Pressed Explained | Educate on process and product quality | Carousel, explainer reel |
| High Smoke Point Kitchen | Show frying, sauteing, and baking usability | Video ad, product page visual |
| Family Kitchen Switch | Trust and habit-change story | UGC, testimonial-style reel |
| Marketplace Proof | Scan-friendly conversion creative | Amazon, Flipkart, Blinkit |

Production outputs the skill can create:

- 20 static ad prompts
- 10 UGC scripts
- 10 image prompts
- 5 JSON prompt templates
- 5 Kling prompts
- 1 Pletor workflow plan
- 1 testing matrix

Testing matrix:

| Variable | Test |
|---|---|
| Hook | Health-conscious vs taste-neutral vs cold-pressed |
| Visual | Product hero vs cooking action vs family meal |
| Format | Square marketplace vs vertical reel vs carousel |
| CTA | Buy now vs switch today vs discover cold-pressed |
| Proof | MUFA/Omega-3 badges vs product process vs reviews |

## Compliance and Claim Guardrails for Jivo

Because Jivo operates in edible oils and wellness categories, marketing must be careful with health claims.

The skill should help avoid risky claims, but final legal approval is still needed for live ads.

### Safer Claim Types

Generally safer if accurate and source-backed:

- "Cold-pressed"
- "Low in saturated fat"
- "Rich in MUFA"
- "Contains Omega-3 fatty acids"
- "Cholesterol free"
- "Sodium free"
- "Trans fat free"
- "High smoke point"
- "Suitable for everyday cooking"
- "Neutral/mild flavor"
- "Imported from Canada" or "imported from Spain" only when true for the specific SKU

### Risky Claim Types

Avoid unless approved by legal/regulatory review:

- "Cures"
- "Prevents"
- "Treats"
- "Fights cancer"
- "Reduces diabetes"
- "Guarantees heart health"
- "Weight loss guaranteed"
- "Doctor recommended" without approved evidence and usage rights
- "Best" or "#1" claims without current substantiation

### Better Creative Language

Instead of:

> Jivo prevents heart disease.

Use:

> Jivo Cold-Pressed Canola Oil is low in saturated fat and contains Omega-3 fatty acids, making it a smart choice for balanced everyday cooking.

Instead of:

> This oil makes you lose weight.

Use:

> A lighter-feeling everyday cooking choice for health-conscious kitchens.

Instead of:

> Cure cholesterol naturally.

Use:

> Contains Omega-3 fatty acids and may help maintain normal cholesterol levels when used as part of a balanced diet, if this claim is approved for the campaign.

## How the Skill Helps Jivo Marketing Teams

### For Founders and Leadership

It can turn brand direction into clear campaign pillars and creative routes.

Useful outputs:

- Brand positioning
- Product messaging hierarchy
- Campaign strategy
- Creative route comparison
- Marketplace growth ideas

### For Performance Marketers

It can create high-volume creative variants with consistent structure.

Useful outputs:

- Ad prompt batches
- Hook tests
- CTA tests
- Marketplace creative variants
- Funnel-stage creative maps

### For Designers

It can produce precise visual prompts and creative briefs.

Useful outputs:

- Product shot briefs
- Layout direction
- Color and lighting notes
- Negative constraints
- Composition ideas

### For Video Editors

It can turn campaign routes into shot lists and video generation prompts.

Useful outputs:

- Reel scripts
- Shot-by-shot prompts
- Kling prompts
- Motion direction
- Voiceover and caption structure

### For Agencies

It can create a shared source of truth.

Useful outputs:

- Brand guidelines
- Ad concept decks
- Production-ready creative prompts
- Workflow plans
- Compliance notes

### For Automation

It can help convert creative work into repeatable systems.

Useful outputs:

- JSON image prompts
- JSON video prompts
- Batch prompt templates
- Pletor node workflows
- Pletor API execution steps

## What the Skill Does Not Do by Itself

The skill does not automatically:

- Approve claims legally
- Replace food law or advertising compliance review
- Guarantee generated image accuracy
- Guarantee product label fidelity
- Generate final images without an image model or workflow tool
- Generate final videos without a video model or workflow tool
- Run Pletor API jobs without a valid API key
- Know private Jivo data unless it is provided in the workspace or prompt

It is a powerful execution and planning layer, but it still depends on:

- Correct product information
- Brand assets
- Packaging files
- Legal claim approval
- Platform specs
- Model/tool access
- Human review before publishing

## Best Workflow for Using This Skill

### Step 1: Give Context

Provide:

- Product name
- Product image
- Platform
- Target audience
- Creative objective
- Any approved claims
- Any forbidden claims
- Required format

### Step 2: Ask for Campaign Routes

Before generating 50 prompts, ask for 3 to 6 campaign routes.

Example:

```text
Use Pletor Marketing to create 6 campaign routes for Jivo canola oil on Amazon and Instagram. Rank them by conversion potential and brand fit.
```

### Step 3: Pick the Route

Choose the strongest route, then generate prompts.

### Step 4: Generate Batch Variants

Ask for variants by:

- Platform
- Audience
- Hook
- Visual style
- CTA
- Product claim
- Funnel stage

### Step 5: Turn Winners Into Workflows

Once a creative route works, ask the skill to turn it into:

- A JSON prompt template
- A Pletor workflow
- A repeatable batch system

## Suggested Jivo Skill Commands

Use these directly in Codex after restarting:

```text
Use Pletor Marketing to create a Jivo master brand brief from jivo.in and shop.jivo.in.
```

```text
Use Pletor Marketing to create a 30-day content calendar for Jivo canola oil, olive oil, wheatgrass, and ghee.
```

```text
Use Pletor Marketing to create 25 Blinkit ad prompts for Jivo products with square format and product-first composition.
```

```text
Use Pletor Marketing to create UGC scripts for Indian mothers comparing everyday cooking oils without attacking competitors.
```

```text
Use Pletor Marketing to create JSON image prompts for all Jivo product packshots in premium kitchen settings.
```

```text
Use Pletor Marketing to design a Pletor workflow for generating Jivo product ads from one product image and one campaign brief.
```

## Recommended Next Additions

The skill will become stronger if we add these Jivo-specific inputs later:

- Official Jivo logo files
- Current packaging files for every SKU
- Approved claim bank
- Forbidden claim bank
- Marketplace image specs
- Brand color palette
- Font references
- Competitor list
- Best performing past ads
- Product price and pack-size matrix
- Product-wise positioning notes
- Platform-wise creative rules

The most important next file to create is:

`JIVO_APPROVED_CLAIMS_AND_GUARDRAILS.md`

That would let the skill produce much safer and more consistent creative output.

## Source Notes

This guide uses the installed local Pletor Marketing skill and public Jivo pages as working source material.

Official Jivo sources reviewed:

- Jivo home page: https://jivo.in/
- Jivo "Who We Are": https://jivo.in/about/who-we-are
- Jivo "The Story": https://jivo.in/about/the-story/
- Jivo "Why Jivo": https://jivo.in/about/why-jivo/
- Jivo cold-pressed canola oil page: https://jivo.in/edible-oil/canola-oil-cold-pressed/
- Jivo olive oil page: https://jivo.in/edible-oil/olive-oil/
- Jivo shop canola product page: https://shop.jivo.in/product/jivo-cold-press-canola-oil/

Internal skill references:

- `.codex-local-plugins/pletor-marketing/skills/pletor-marketing/SKILL.md`
- `.codex-local-plugins/pletor-marketing/skills/pletor-marketing/references/`

## Bottom Line

The `pletor-marketing` skill gives Jivo a reusable creative production system inside Codex.

It is better than normal prompting because it preserves method, routes tasks to the right prompt system, protects brand consistency, supports batch generation, and can turn marketing ideas into structured outputs for images, videos, UGC, marketplaces, and Pletor workflows.

For Jivo, its best use is not "make one ad." Its best use is:

1. Understand the brand.
2. Define campaign routes.
3. Generate many brand-safe creative variants.
4. Convert winning routes into repeatable workflows.
5. Scale marketing production without losing the brand.
