# TypeFx Banners User Guide

## Getting Started

```python
from typefx.banners import box, project_banner, divider
from typefx.colors import BRIGHT_CYAN, GREEN, CYAN

# Simple box
print(box("Hello World"))

# Box with all customizations
print(box(
    "Customized Content",
    style="double",
    title="Output",
    color=BRIGHT_CYAN,
    align="center",
    padding=1,
    width=40,
))
```

## Project Banners

Use `project_banner()` to create professional-looking project headers:

```python
from typefx.banners import project_banner
from typefx.colors import BRIGHT_CYAN, GREEN

# Minimal
print(project_banner("MyApp"))

# Full
print(project_banner(
    "MyApp",
    tagline="A Cool CLI Tool",
    version="1.0.0",
    color=BRIGHT_CYAN,
    accent=GREEN,
    width=50,
    border_style="double",
))
```

## Hero Banner

For attention-grabbing headers:

```python
from typefx.banners import hero_banner

print(hero_banner("Welcome to MyApp", color=BRIGHT_CYAN, width=60))
```

## Alert Banners

Five built-in alert levels: info, success, warning, error, critical:

```python
from typefx.banners import alert_banner

print(alert_banner("System OK", level="success"))
print(alert_banner("Resource usage high", level="warning"))
print(alert_banner("Connection failed", level="critical"))
```

## Progress Bars

```python
from typefx.banners import progress_bar
from typefx.colors import GREEN

print(progress_bar(0, width=20, label="Download"))
print(progress_bar(50, width=20, label="Processing"))
print(progress_bar(100, width=20, label="Complete", color=GREEN))
```

## Tags / Badges

```python
from typefx.banners import tag
from typefx.colors import BRIGHT_CYAN, GREEN, YELLOW

print(tag("INFO", color=BRIGHT_CYAN))
print(tag("DONE", color=GREEN, bracket="round"))
print(tag("WARN", color=YELLOW, bracket="curly", invert=True))
```

## Dividers & Rules

```python
from typefx.banners import divider, rule
from typefx.colors import CYAN, GREEN

# Simple divider
print(divider())

# With label and color
print(divider(length=50, label="Section 1", color=CYAN, align="center"))

# Left-aligned label
print(divider(length=50, label="Start", color=CYAN, align="left"))

# Colored rule
print(rule(color=GREEN, length=40, char="="))
```

## Section Headers

```python
from typefx.banners import section_header
from typefx.colors import CYAN, BRIGHT_CYAN

# Default left-aligned
print(section_header("Features", color=CYAN))

# Centered
print(section_header("Overview", align="center", color=BRIGHT_CYAN))
```

## Centered Banners

```python
from typefx.banners import centered_banner
from typefx.colors import BRIGHT_CYAN

print(centered_banner("★ Hello ★", width=50, color=BRIGHT_CYAN, bold=True))
```

## Framing Art

```python
from typefx.banners import frame, animal

# Frame an animal
print(frame(animal("dragon"), box_style="double"))

# Frame with title
print(frame("  Hello\n  World", box_style="rounded", title="Greeting"))
```

## ASCII Animals

50+ built-in animals:

```python
from typefx.banners import animal, animal_names

# Get all available names
print(animal_names())

# Get specific animal
cat = animal("cat1")
print(cat)

# Get random animal
random_pet = animal()
print(random_pet)
```

## Kaomoji (Japanese Emoticons)

600+ kaomoji across 30+ categories:

```python
from typefx.banners import kaomoji, kaomoji_categories

# List categories
print(kaomoji_categories())

# Random kaomoji
print(kaomoji())

# By category
print(kaomoji("happy"))
print(kaomoji("cat"))
print(kaomoji("greeting"))
print(kaomoji("fight"))
```

Available categories: happy, sad, angry, love, shrug, cat, dog, bear, cute, surprise, sleep, dance, tableflip, party, greeting, wave, hug, sorry, thank, excited, nervous, cool, run, fight, magic, food, drink, music, rain, star, flower, cold.

## Emoji Symbols

90+ Unicode symbols:

```python
from typefx.banners import emoji

# By name
print(emoji("heart"))
print(emoji("zodiac_aries"))
print(emoji("chess_king"))
print(emoji("star_sparkle"))

# Random
print(emoji())
```

## Buddy / Mascot

Combine animals with project names:

```python
from typefx.banners import buddy, buddy_box, buddy_multi
from typefx.colors import BRIGHT_CYAN, BRIGHT_GREEN

# Simple buddy
print(buddy("MyApp", animal_name="cat1", color=BRIGHT_CYAN))

# Buddy with message
print(buddy("MyApp", animal_name="penguin2", color=BRIGHT_CYAN,
            message="Making terminals beautiful!"))

# Buddy without name
print(buddy("Secret", animal_name="fox", show_name=False))

# Boxed buddy
print(buddy_box("MyApp", tagline="v2.0", animal_name="fox"))

# Multiple animals as mascots
print(buddy_multi("MyApp", animal_names=["cat1", "fox", "penguin2"],
                  color=BRIGHT_CYAN, spacing=4))
```

## Color Art

Apply ANSI colors to existing ASCII art:

```python
from typefx.banners import color_art
from typefx.colors import GREEN, BG_BLUE

# Basic color
print(color_art("  Hello", GREEN))

# With background, alignment, and padding
print(color_art("Hi", GREEN, bg_color=BG_BLUE, align="center", width=20, padding=1))
```

## Combining Features

```python
from typefx.banners import *
from typefx.colors import *

# Full startup banner
print(hero_banner("MyApp Server", color=BRIGHT_CYAN, width=60))
print(alert_banner("Server starting on port 8080", level="info", width=60))
print(divider(length=60, color=CYAN))
print(progress_bar(100, width=30, label="Initialized", color=GREEN))
print()
print(buddy("MyApp", animal_name="dragon", color=BRIGHT_CYAN,
            message="Ready to serve!"))
```
