# TypeFx Banners Module

The `typefx.banners` module provides a comprehensive toolkit for creating ASCII art banners, box layouts, dividers, alert messages, progress bars, and more — all with ANSI color support.

## Features

- **Box Layouts** — 7 box-drawing styles (single, double, rounded, heavy, ascii, double_h, double_v)
- **Banner Templates** — project_banner, hero_banner, alert_banner, centered_banner, banner_block, banner_arrow, banner_dash
- **Dividers & Rules** — Customizable dividers with labels, colored rules
- **Progress Bars** — Configurable progress bars with labels and percentage display
- **Tags & Badges** — Small label/badge generators with customizable brackets
- **Frames** — Frame ASCII art inside box styles
- **ASCII Animals** — 50+ built-in ASCII art animals
- **Kaomoji** — 600+ Japanese emoticons across 30+ categories
- **Emoji Symbols** — 90+ Unicode symbols (stars, arrows, zodiac, chess, math, etc.)
- **Buddy Mascots** — Combine animals with project names for mascot displays
- **Multi-Animal Display** — Show multiple animals side-by-side as a team mascot

## Highly Customizable

All functions accept optional parameters for:
- `color` — Text/foreground ANSI color
- `align` — Text alignment (left, center, right)
- `padding` — Internal spacing
- `width` — Output width control
- `border_color` — Box border color
- `title` — Title text for boxes
- `title_color` — Title text color

## Quick Examples

```python
from typefx.banners import (
    box, project_banner, hero_banner, alert_banner,
    progress_bar, tag, divider, centered_banner,
    animal, kaomoji, emoji, buddy, buddy_multi,
    frame, color_art,
)

# Box with customization
print(box("Hello", style="double", color=BRIGHT_CYAN, align="center", padding=1))

# Project banner
print(project_banner("MyApp", tagline="Terminal Text Effects", version="2.0.1"))

# Alert
print(alert_banner("System OK", level="success"))

# Progress
print(progress_bar(50, width=20, label="Loading"))

# Animal
print(animal("dragon"))
```
