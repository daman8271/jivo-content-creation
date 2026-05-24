# Jivo "Flip" Carousel

An 8-slide Instagram carousel that flips a relationship **red flag** into a Jivo virtue
("the product is the better partner"). Modeled on the viral `bakemyday.me` format.

Full design + locked style system: [`../docs/superpowers/specs/2026-05-24-jivo-flip-carousel-design.md`](../docs/superpowers/specs/2026-05-24-jivo-flip-carousel-design.md)

## How it's made
- **Higgsfield (GPT Image 2)** generates the food/oil hero shots (no text) → `heroes/`.
- **Python/Pillow** (`../scripts/build_flip_carousel.py`) white-balances each hero to the
  locked sage tone, composites the real Canola bottle on the cover/closer, and stamps the
  locked Poppins / forest-green type → `slides/`.

Rebuild any time:
```bash
python3 scripts/build_flip_carousel.py        # all slides
python3 scripts/build_flip_carousel.py 02     # one slide
```

## The 8 slides (copy)
1. **He'll always let you down —** Jivo never will. *(cover · real bottle)*
2. **He couldn't handle the heat,** we've got a high smoke point.
3. **He was too heavy,** we're extra light.
4. **He was so fake,** we're 100% pure, cold-pressed.
5. **He gave you mixed signals,** we're consistent every time.
6. **He couldn't commit,** we've been in your kitchen for years.
7. **His replies ran dry,** our food never does.
8. **He broke your heart,** we're the kind that's good for it. — *Cook with someone good for you. — Jivo* *(closer · real bottle + oil heart)*

## Suggested caption
> Situationships end. Good cooking doesn't. 🫒
>
> He couldn't handle the heat. He left you on read. He gave you mixed signals.
> But your oil? Loyal, light, and actually good to you. ❤️
>
> Swipe through every red flag Jivo *doesn't* have →
> Cook with someone good for you.
>
> #Jivo #ColdPressed #CanolaOil #HealthyCooking #IndianKitchen #FoodHumour #Relatable

## ⚠️ Before posting
Run the copy through a **legal/regulatory pass** — keep it product-led, no medical/disease
claims. Soften slide 8 if needed ("light on your heart" / tie to "low in saturated fat,
rich in MUFA").
