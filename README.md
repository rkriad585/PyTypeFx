<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/version-2.1.0-green?logo=git&logoColor=white" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-blue" alt="License">
  <img src="https://img.shields.io/badge/tests-198%20passing-brightgreen" alt="Tests">
  <img src="https://img.shields.io/badge/dependencies-0-success" alt="Zero Deps">
</p>

<h1 align="center">TypeFx</h1>
<p align="center"><em>Terminal text effects, ASCII art banners, and mascot displays — zero dependencies.</em></p>

TypeFx brings your terminal applications to life with dynamic typing effects, customizable banner templates, **55+ ASCII art animals**, **600+ kaomoji expressions**, and **90+ Unicode emoji symbols** — all with zero external dependencies.

---

## Table of Contents

- [Quick Start](#quick-start)
- [Installation](#installation)
- [Features](#features)
  - [Typing Effects](#typing-effects)
  - [Banners & ASCII Art](#banners--ascii-art)
  - [ASCII Animals](#ascii-animals)
  - [Kaomoji](#kaomoji)
  - [Emoji Symbols](#emoji-symbols)
  - [Buddy / Mascot System](#buddy--mascot-system)
  - [Color System](#color-system)
  - [Style Presets](#style-presets)
- [Decorator](#decorator)
- [Command-Line Interface](#command-line-interface)
- [Full API Reference](#full-api-reference)
- [Configuration](#configuration)
- [Examples Gallery](#examples-gallery)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

---

## Quick Start

```python
from typefx import project_banner, hero_banner, alert_banner, progress_bar, tag, divider, animal, kaomoji, buddy
from typefx.colors import BRIGHT_CYAN, CYAN, GREEN

# Project banner
print(project_banner("MyApp", tagline="v2.0", version="1.0.0"))

# Alert
print(alert_banner("Server started", level="success", width=50))

# Progress bar
print(progress_bar(75, width=20, label="Loading", color=GREEN))

# ASCII animal
print(animal("dragon"))

# Buddy mascot
buddy("MyApp", animal_name="cat1", color=BRIGHT_CYAN, message="Ready!")
```

## Installation

```bash
pip install PyTypeFx
```

**Or from source:**

```bash
git clone https://github.com/rkriad585/PyTypeFx.git
cd PyTypeFx
pip install -e .
```

---

## Features

### Typing Effects

All 18 writers share consistent parameters: `text`, `delay`, `color`, `style`, `position`.

```python
from typefx import TypeWriter, RainbowWriter, GlitchWriter, GradientWriter, BounceWriter

# Classic typewriter
TypeWriter("Hello, World!", delay=0.05)

# Rainbow cycling text
RainbowWriter("Rainbow effect!", delay=0.03)

# Glitch / distortion effect
GlitchWriter("SYSTEM ONLINE", delay=0.05, color="green")

# Smooth color gradient
GradientWriter("Gradient text", start_hex="#FF0000", end_hex="#0000FF")

# Bounce animation
BounceWriter("BOUNCE!", delay=0.08, color="cyan")

# Loop write-delete animation
LoopWriter("Loading...", loops=5, delay=0.03, color="yellow")

# Game-style dialog box
GameDialog("Hello, adventurer!", delay=0.03, color="green")

# Markdown rendering
MarkdownWriter("This is **bold** and *italic* text.")

# HTML rendering
HTMLWriter("This is <b>bold</b> and <i>italic</i> text.")

# Reverse type
ReverseWriter("Reverse text")

# Thinking animation with blinking dots
ThinkWriter("Analyzing...", color="cyan")

# Ghost autocomplete suggestion
AutoCompleteWriter("autocomplete", color="bright_black")
```

**Full writer list:**

| Writer | Effect |
| --- | --- |
| `TypeWriter` | Standard character-by-character typing |
| `RainbowWriter` | Rainbow color cycling |
| `HexWriter` | Custom hex color cycling |
| `DelWriter` | Type then delete |
| `LoopWriter` | Repeated type-delete loop |
| `SoundWriter` | Type with beep sounds |
| `GameDialog` | Game-style dialog box |
| `RandomWriter` | Random color per character |
| `MarkdownWriter` | Renders `**bold**`, `*italic*`, `__underline__` |
| `HTMLWriter` | Renders `<b>`, `<i>`, `<u>`, `<s>`, `<blink>` |
| `GlitchWriter` | Glitch/distortion effect |
| `ThinkWriter` | Blinking ellipsis before text |
| `ReverseWriter` | Reverse order typing |
| `ReverseGlitchWriter` | Reverse + glitch combined |
| `BounceWriter` | Bounce highlight effect |
| `BounceGlitchWriter` | Bounce + glitch combined |
| `GradientWriter` | Smooth hex-to-hex gradient |
| `AutoCompleteWriter` | Ghost autocomplete suggestion |

---

### Banners & ASCII Art

Every banner function accepts optional `color`, `align`, `padding`, `width`, `border_color`, and `title_color` parameters with full backward compatibility.

```python
from typefx import box, project_banner, hero_banner, alert_banner, progress_bar, tag, divider, frame, centered_banner, section_header, banner_block, banner_arrow, banner_dash, rule, color_art
from typefx.colors import BRIGHT_CYAN, CYAN, GREEN, YELLOW, RED, MAGENTA

# --- Box Layouts (7 styles) ---
print(box("Hello"))                                          # single box
print(box("Content", style="double", title="Output"))        # double-line
print(box("Rounded", style="rounded"))                       # rounded corners
print(box("Heavy", style="heavy"))                           # thick lines
print(box("ASCII", style="ascii"))                           # pure ASCII +-*/

# Fully customized box
print(box("Customized", color=BRIGHT_CYAN, align="center", padding=1, width=30, title="Demo", title_color=GREEN, border_color=CYAN))

# --- Project Banner ---
print(project_banner("MyApp", tagline="Terminal Text Effects", version="2.0.1", color=BRIGHT_CYAN, accent=GREEN))

# --- Hero Banner ---
print(hero_banner("Welcome to MyApp", color=BRIGHT_CYAN, width=60))

# --- Alert Banners (5 levels) ---
print(alert_banner("Everything OK", level="success", width=50))
print(alert_banner("Disk at 85%", level="warning", width=50))
print(alert_banner("Server down", level="error", width=50))
print(alert_banner("Connection lost", level="critical", width=50))

# --- Progress Bars ---
print(progress_bar(25, width=20, label="Download"))
print(progress_bar(50, width=20, label="Processing", color=YELLOW))
print(progress_bar(100, width=20, label="Complete", color=GREEN, show_percent=True))

# --- Tags / Badges ---
print(tag("INFO", color=BRIGHT_CYAN, bracket="square"))
print(tag("URGENT", color=RED, bracket="curly"))

# --- Dividers ---
print(divider(length=50, label="Section", color=CYAN, align="center"))
print(divider(length=40, fill="~", label="Chapter 1", color=YELLOW))

# --- Frames ---
print(frame("  Hello\n  World", box_style="double"))
print(color_art("  ╔═══╗\n  ║ ♥ ║\n  ╚═══╝", color=RED))

# --- Centered Banner ---
print(centered_banner("★ PyTypeFx ★", width=50, color=BRIGHT_CYAN, fill="="))

# --- Section Header ---
print(section_header("Features", color=CYAN, align="center"))

# --- Banner Block with arrow ---
print(banner_block("Main Title", color=BRIGHT_CYAN, align="center"))
print(banner_arrow("Next Step", color=GREEN))
print(banner_dash("Item", color=CYAN))

# --- Rule ---
print(rule(color=CYAN))
```

**Full banner function list:**

| Function | Description |
| --- | --- |
| `box()` | Multi-style box layouts (7 styles) |
| `project_banner()` | Full project header with name, tagline, version |
| `hero_banner()` | Big attention-grabbing header |
| `alert_banner()` | Contextual alerts (info/success/warning/error/critical) |
| `progress_bar()` | Visual progress bars with labels |
| `tag()` | Badges and labels |
| `divider()` | Horizontal dividers with labels |
| `frame()` | Frame ASCII art inside boxes |
| `centered_banner()` | Text centered between fill characters |
| `section_header()` | Section header with decorative borders |
| `banner_block()` | Large banner block with top/bottom borders |
| `banner_arrow()` | Arrow-pointing banner |
| `banner_dash()` | Dashed prefix banner |
| `rule()` | Colored horizontal rule |
| `color_art()` | Color existing ASCII art |
| `buddy()` | Combine animal + project name |
| `buddy_box()` | Buddy mascot inside a box |
| `buddy_multi()` | Multiple animals side-by-side |

---

### ASCII Animals

55+ built-in ASCII art animals. Display one by name, or get a random one.

```python
from typefx import animal, animal_names

# Specific animal
print(animal("dragon"))
#   /\_/\  
#  ( o.o ) 
#   > ^ <  

print(animal("cat1"))
#   /\_/\  
#  ( o.o ) 
#   > ^ <  

print(animal("penguin1"))
#  .---.
# /     \
#  \.-.-./

# Random animal
print(animal())

# List all available names
names = animal_names()
print(len(names))  # 55+
```

**Available animals:**
`cat1`, `cat2`, `cat_love`, `dog1`, `dog2`, `dog_sleep`, `bear`, `penguin1`, `penguin2`, `penguin_dance`, `bunny1`, `bunny2`, `bunny3`, `bird`, `fish`, `fox`, `pig`, `frog`, `koala`, `panda`, `turtle`, `monkey`, `octopus1`, `octopus2`, `lion`, `horse`, `cow`, `sheep`, `elephant`, `whale`, `dolphin`, `shark`, `snake`, `spider`, `butterfly`, `parrot`, `eagle`, `wolf`, `deer`, `chicken`, `hamster`, `mouse`, `sloth`, `dragon`, `bat`, `seal`, `crab`, `dino`, and more.

---

### Kaomoji

600+ Japanese emoticons across 30 categories.

```python
from typefx import kaomoji, kaomoji_categories

# By category
print(kaomoji("happy"))    # (◕‿◕✿)
print(kaomoji("love"))     # ♥‿♥
print(kaomoji("fight"))    # (งಠ_ಠ)ง
print(kaomoji("cat"))      # (=^‥^=)
print(kaomoji("dance"))    # └(^‿^)┘
print(kaomoji("party"))    # d(^‿^)b
print(kaomoji("magic"))    # (∩‿∩)⊃━☆ﾟ.*･｡ﾟ
print(kaomoji("sorry"))    # (シ_ _)シ
print(kaomoji("excited"))  # ヽ(°〇°)ﾉ
print(kaomoji("cold"))     # (っ◕‿◕)っ❄

# Random kaomoji
print(kaomoji())

# List categories
print(kaomoji_categories())
```

**Categories:** happy, sad, angry, love, shrug, cat, dog, bear, cute, surprise, sleep, dance, party, greeting, wave, hug, sorry, thank, excited, nervous, cool, run, fight, magic, food, drink, music, rain, star, flower, cold.

---

### Emoji Symbols

90+ Unicode symbols organized by category.

```python
from typefx import emoji, emoji_categories

# Get emoji by name
print(emoji("heart_red"))     # ♥
print(emoji("star"))          # ★
print(emoji("fire"))          # ♨
print(emoji("aries"))         # ♈
print(emoji("chess_king"))    # ♔
print(emoji("infinity"))      # ∞
print(emoji("euro"))          # €
print(emoji("sun"))           # ☀
print(emoji("peace"))         # ☮

# Random emoji
print(emoji())

# List categories
print(emoji_categories())
```

**Categories:** hearts, stars, zodiac, chess, math, arrows, currency, weather, geometric, music, misc.

---

### Buddy / Mascot System

Combine any ASCII animal with a project name for mascot displays.

```python
from typefx import buddy, buddy_box, buddy_multi
from typefx.colors import BRIGHT_CYAN, GREEN, MAGENTA

# Single mascot
buddy("MyApp", animal_name="cat1", color=BRIGHT_CYAN)

# With message
buddy("MyApp", animal_name="penguin2", color=BRIGHT_CYAN,
      message="Making terminals beautiful!")

# Boxed mascot
buddy_box("MyApp", tagline="v2.0", animal_name="fox", color=BRIGHT_CYAN)

# Multi-animal team (aligned side-by-side)
buddy_multi("MyApp", animal_names=["cat1", "fox", "penguin2"],
            color=BRIGHT_CYAN)
```

---

### Color System

```python
from typefx.colors import (
    RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
    BRIGHT_RED, BRIGHT_GREEN, BRIGHT_CYAN, BRIGHT_WHITE,
    ORANGE, PINK, TEAL, CORAL, MINT, PLUM, GOLD,
    BG_RED, BG_GREEN, BG_CYAN,
    BOLD, UNDERLINE, ITALIC, INVERT, STRIKETHROUGH,
    hex_to_ansi, rgb_to_ansi, colorize
)

# Apply multiple styles
print(colorize("Error!", RED, BOLD, UNDERLINE))

# Hex to ANSI
print(f"{hex_to_ansi('#FF5733')}Orange text{RESET}")

# RGB to ANSI
print(f"{rgb_to_ansi(100, 200, 255)}Custom RGB{RESET}")

# Use a palette
from typefx.colors import PALETTES
print(PALETTES["OCEAN"])   # ['#0077BE', '#0099CC', '#00BFFF', ...]
print(PALETTES["SUNSET"])  # ['#FF4500', '#FF6347', '#FF8C00', ...]
```

**What's included:**
- 16 basic + 16 bright ANSI colors
- 50+ extended named colors (Coral, Mint, Plum, Slate, Gold, etc.)
- Background variants for all colors (`BG_RED`, `BG_GREEN`, ...)
- HEX and RGB to ANSI converters
- 256-color 8-bit helpers (`fg_256()`, `bg_256()`)
- 6 curated palettes: `SUCCESS`, `ERROR`, `WARNING`, `INFO`, `NEON`, `PASTEL`, `OCEAN`, `SUNSET`, `FOREST`, `GARDEN`, `CYBER`, `NOIR`, `ROSE`

---

### Style Presets

40+ composable style presets for quick formatting.

```python
from typefx.styles import apply_style, compose, ERROR, SUCCESS, WARNING, INFO, TITLE, HEADING, CODE, HIGHLIGHT, BANNER, NEON, GHOST

# Apply a preset
print(apply_style("Something went wrong!", ERROR))
print(apply_style("Task completed!", SUCCESS))
print(apply_style("Chapter 1", TITLE))
print(apply_style("Important note", HIGHLIGHT))
print(apply_style("Neon sign", NEON))

# Compose a custom style
from typefx.colors import BRIGHT_MAGENTA, BRIGHT_CYAN, INVERT, BOLD
custom = compose(BRIGHT_MAGENTA, BRIGHT_CYAN, INVERT, BOLD)
print(apply_style("Custom!", custom))

# Use with writers
from typefx import TypeWriter
TypeWriter("Banner text", **BANNER)
TypeWriter("Error text", **ERROR)
```

---

## Decorator

The `@typefx` decorator applies typing effects to any function's output.

```python
from PyTypeFx import typefx

@typefx(hex_colors=["#FF0000", "#00FF00", "#0000FF"], delay=0.03)
def my_message():
    print("This message will be typed out with a cool effect!")

my_message()
```

---

## Command-Line Interface

```bash
# Basic
typefx --text "Hello from the CLI!" --delay 0.05 --rainbow

# From file
typefx --file message.txt --delay 0.03

# Random effect
typefx --text "Random text" --random

# Looping
typefx --text "Looping" --loops 5
```

**CLI Options:**

| Option | Description |
| --- | --- |
| `-t`, `--text` | Text to type |
| `-d`, `--delay` | Delay between characters |
| `-l`, `--loops` | Loop count for `LoopWriter` |
| `-r`, `--rainbow` | Rainbow effect |
| `-rnd`, `--random` | Random writer effect |
| `-s`, `--sound` | Sound effect |
| `-f`, `--file` | Read text from a file |

---

## Full API Reference

### `typefx.writers`

| Function | Signature |
| --- | --- |
| `TypeWriter` | `(text, delay, color, style, reverse, position)` |
| `RainbowWriter` | `(text, delay, style, position)` |
| `HexWriter` | `(text, delay, style, position)` |
| `DelWriter` | `(text, delay, color, style, reverse, position)` |
| `LoopWriter` | `(text, delay, color, style, reverse, position, loops)` |
| `SoundWriter` | `(text, delay, color, style, reverse, position, frequency, duration)` |
| `GameDialog` | `(text, delay, color, style, position)` |
| `RandomWriter` | `(text, delay, style, position)` |
| `MarkdownWriter` | `(text, delay, style, position)` |
| `HTMLWriter` | `(text, delay, style, position)` |
| `GlitchWriter` | `(text, delay, color, style, position, glitch_chars, glitch_duration)` |
| `ThinkWriter` | `(text, delay, color, style, position)` |
| `ReverseWriter` | `(text, delay, color, style, position)` |
| `ReverseGlitchWriter` | `(text, delay, color, style, position)` |
| `BounceWriter` | `(text, delay, color, style, position)` |
| `BounceGlitchWriter` | `(text, delay, color, style, position)` |
| `GradientWriter` | `(text, delay, style, position, start_hex, end_hex)` |
| `AutoCompleteWriter` | `(text, delay, color, style, position, options)` |

### `typefx.banners`

| Function | Description |
| --- | --- |
| `box(text, style, color, align, padding, width, title, title_color, border_color)` | Box layouts in 7 styles |
| `project_banner(name, tagline, version, color, accent)` | Full project header |
| `hero_banner(text, color, width)` | Large attention header |
| `alert_banner(text, level, width)` | 5-level alert banners |
| `progress_bar(percent, width, label, color, show_percent, fill, empty)` | Progress bars |
| `tag(text, color, bracket)` | Badges / labels |
| `divider(length, label, fill, color, align)` | Horizontal dividers |
| `frame(art, box_style, color, padding)` | Frame ASCII art |
| `centered_banner(text, width, fill, color)` | Centered text banner |
| `section_header(text, color, align)` | Section headers |
| `banner_block(text, color, align, padding, width)` | Large banner block |
| `banner_arrow(text, color, align)` | Arrow banner |
| `banner_dash(text, color, align)` | Dashed banner |
| `rule(color, length)` | Colored horizontal rule |
| `color_art(art, color)` | Colorize ASCII art |
| `animal(name)` | Get ASCII animal |
| `animal_names()` | List all animal names |
| `kaomoji(category)` | Get kaomoji by category |
| `kaomoji_categories()` | List all kaomoji categories |
| `emoji(name)` | Get emoji by name |
| `emoji_categories()` | List all emoji categories |
| `buddy(name, animal_name, color, message)` | Mascot display |
| `buddy_box(name, tagline, animal_name, color)` | Boxed mascot |
| `buddy_multi(name, animal_names, color)` | Multi-animal mascot |
| `ALERT_STYLES` | Dict: info, success, warning, error, critical |

### `typefx.effects`

- `BlinkEffect(duration, cursor, delay)` — Blinking cursor animation
- `SoundEffect(frequency, duration)` — System beep sound

### `typefx.colors`

- `hex_to_ansi(hex_color)` — Hex to ANSI foreground
- `bg_hex_to_ansi(hex_color)` — Hex to ANSI background
- `rgb_to_ansi(r, g, b)` — RGB to ANSI foreground
- `bg_rgb_to_ansi(r, g, b)` — RGB to ANSI background
- `fg_256(n)` — 8-bit 256-color foreground
- `bg_256(n)` — 8-bit 256-color background
- `colorize(text, *styles)` — Apply ANSI codes to text

### `typefx.styles`

- `compose(color, *formats)` — Build style dict
- `apply_style(text, style)` — Apply style to string

### `typefx.utility`

- `gradient(text, start_hex, end_hex)` — Apply gradient to text
- `supports_ansi()` — Check terminal ANSI support

---

## Configuration

The `typefx.constant` module contains all default values:

| Constant | Default | Description |
| --- | --- | --- |
| `TEXT` | `"Hello World!"` | Default text for writers |
| `GLITCH` | `"!@#$%^&*()..."` | Glitch character set |
| `CURSOR` | `_` | BlinkEffect cursor |
| `DELAY` | `0.05` | Default character delay |
| `HOLD` | `1` | DelWriter hold time |
| `LOOP` | `3` | Default loop count |
| `DOTS` | `3` | ThinkWriter dot count |
| `FREQUENCY` | `800` | Sound frequency |
| `SOUND_DURATION` | `30` | Sound duration |
| `START_HEX` | `"#E74C3C"` | Gradient start color |
| `END_HEX` | `"#2ECC71"` | Gradient end color |

---

## Examples Gallery

### Gradient Text

```python
from PyTypeFx import GradientWriter

GradientWriter("This is a beautiful gradient!", start_hex="#FF00FF", end_hex="#00FFFF", delay=0.02)
```

### Game Dialog

```python
from PyTypeFx import GameDialog

GameDialog(speaker="Hero", text="I must defeat the final boss!", delay=0.04, sound=True)
```

### Chaining Effects

```python
from PyTypeFx import TypeWriter, DelWriter, BlinkEffect

TypeWriter("Preparing for deletion...")
DelWriter("This message will self-destruct.", hold=2)
BlinkEffect(duration=2)
```

### Alert Dashboard

```python
from typefx import alert_banner, divider, box
from typefx.colors import CYAN

print(box("System Dashboard", style="double", align="center", width=60))
print(alert_banner("CPU: 45%", level="info"))
print(alert_banner("Memory: 72%", level="warning"))
print(alert_banner("Errors: 0", level="success"))
print(divider(length=60, fill="─", color=CYAN))
```

### Multi-Animal Team Mascot

```python
from typefx import buddy_multi
from typefx.colors import BRIGHT_CYAN

buddy_multi("PyTypeFx", animal_names=["dragon", "fox", "penguin2"],
            color=BRIGHT_CYAN)
```

### Custom Box Style

```python
from typefx import box
from typefx.colors import BRIGHT_CYAN, GREEN, CYAN

print(box("Welcome to TypeFx!\nZero dependencies.\n55+ animals. 600+ kaomoji.",
          style="double", color=BRIGHT_CYAN, align="center", padding=1,
          width=50, title="PyTypeFx", title_color=GREEN, border_color=CYAN))
```

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for development setup, testing, code style, and pull request guidelines.

## Code of Conduct

This project follows the [Contributor Covenant](CODE_OF_CONDUCT.md). See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) for details.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.

---

<p align="center">
  <sub>Built with ❤ by <a href="https://github.com/rkriad585">RK RIAD KHAN</a></sub>
</p>
