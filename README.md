# TypeFx

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-2.0.1-green.svg)](https://github.com/rkriad585/PyTypeFx)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A Python library for creating captivating terminal typing effects, ASCII art banners, and mascot displays with ease.

TypeFx brings your terminal applications to life with dynamic typing effects, customizable banner templates, 50+ ASCII art animals, 600+ kaomoji expressions, and 90+ Unicode emoji symbols — all with zero external dependencies.

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

## Features

### Typing Effects
| Writer | Description |
| --- | --- |
| `TypeWriter` | Simulates standard typing |
| `RainbowWriter` | Types text with a rainbow color effect |
| `GlitchWriter` | Types with a glitch/distortion effect |
| `GradientWriter` | Types text with a smooth color gradient |
| `BounceWriter` | Types forwards then deletes |
| `ReverseWriter` | Types text in reverse |
| `AutoCompleteWriter` | Ghost autocomplete suggestion |
| `GameDialog` | Game-style dialog box |
| and 10+ more... | |

### Banners & ASCII Art
| Function | Description |
| --- | --- |
| `project_banner()` | Full project header with name, tagline, version |
| `hero_banner()` | Big attention-grabbing header |
| `alert_banner()` | Contextual alerts (info/success/warning/error/critical) |
| `box()` | Multi-style box layouts |
| `progress_bar()` | Visual progress bars |
| `tag()` | Badges and labels |
| `divider()` | Horizontal dividers with labels |
| `frame()` | Frame ASCII art inside boxes |
| `centered_banner()` | Text centered between fill characters |
| and 10+ more... | |

### ASCII Animals — 50+ Built-in
cats, dogs, bears, penguins, bunnies, birds, fish, fox, pig, frog, koala, panda, turtle, monkey, octopus, lion, horse, cow, sheep, elephant, whale, dolphin, shark, snake, butterfly, eagle, wolf, deer, dragon, bat, seal, crab, dino, and more.

### Kaomoji — 600+ Japanese Emoticons
30 categories: happy, sad, angry, love, shrug, cat, dog, bear, cute, surprise, sleep, dance, party, greeting, wave, hug, sorry, thank, excited, fight, magic, food, drink, music, rain, and more.

### Emoji Symbols — 90+ Unicode
Hearts, stars, arrows, zodiac signs, chess pieces, math symbols, currency, weather, geometric shapes, and more.

### Buddy / Mascot System
Combine any ASCII animal with a project name for mascot displays. Supports single, boxed, and multi-animal layouts.

### Color System
- 16 basic + 16 bright ANSI colors
- 50+ extended named colors (Coral, Mint, Plum, Slate, etc.)
- Background color variants for all
- HEX/RGB to ANSI converters
- 256-color 8-bit helpers
- 6 curated palettes: OCEAN, SUNSET, FOREST, CYBER, NOIR, ROSE

### Style Presets
40+ composable style presets: ERROR, SUCCESS, WARNING, INFO, TITLE, HEADING, CODE, HIGHLIGHT, BANNER, NEON, GHOST, and more.

## Installation

You can install TypeFx using pip:

```bash
pip install PyTypeFx==0.1.0
```

Or install from source:

```bash
git clone https://github.com/rkriad585/PyTypeFx.git
cd PyTypeFx
pip install -e .
```

## Usage

### Basic Usage

The core of TypeFx is its writer functions. Here's a simple example using the `TypeWriter`:

```python
from PyTypeFx import TypeWriter

TypeWriter("Hello, World!", delay=0.05)
```

### Writers

TypeFx comes with a variety of writers, each providing a different effect:

| Writer | Description |
| --- | --- |
| `TypeWriter` | Simulates standard typing. |
| `RainbowWriter` | Types text with a rainbow color effect. |
| `HexWriter` | Types text using a list of HEX colors. |
| `DelWriter` | Types and then deletes text. |
| `LoopWriter` | Repeats the write-and-delete animation. |
| `SoundWriter` | Types text with an accompanying sound. |
| `GameDialog` | Displays text in a game-style dialog box. |
| `RandomWriter` | Types with a randomized, human-like delay. |
| `MarkdownWriter` | Strips Markdown formatting and types the clean text. |
| `HTMLWriter` | Strips HTML tags and types the clean text. |
| `GlitchWriter` | Types with a "glitch" effect. |
| `ThinkWriter` | Simulates a "thinking" animation with trailing dots. |
| `ReverseWriter` | Types text in reverse. |
| `ReverseGlitchWriter` | Types text in reverse with a glitch effect. |
| `BounceWriter` | Types text forwards and then deletes it. |
| `BounceGlitchWriter` | A bouncing animation with a glitch effect. |
| `GradientWriter` | Types text with a smooth color gradient. |

**Example:**

```python
from PyTypeFx import RainbowWriter, GlitchWriter

RainbowWriter("This is a rainbow effect!", delay=0.03)
GlitchWriter("This is a glitch effect!", delay=0.01)
```

### Banners & ASCII Art

TypeFx includes a complete banner generation system with highly customizable templates. All functions support optional `color`, `align`, `padding`, `width`, and box-specific params while maintaining full backward compatibility.

#### Box Layouts

```python
from typefx import box
from typefx.colors import BRIGHT_CYAN

# Minimal box
print(box("Hello"))

# With title and style
print(box("Content here", style="double", title="Output"))

# Fully customized
print(box("Customized", color=BRIGHT_CYAN, align="center",
          padding=1, width=30, title="Demo"))
```

#### Project & Hero Banners

```python
from typefx import project_banner, hero_banner
from typefx.colors import BRIGHT_CYAN, GREEN

# Project header
print(project_banner("MyApp", tagline="Terminal Text Effects",
                     version="2.0.1", color=BRIGHT_CYAN, accent=GREEN))

# Hero banner
print(hero_banner("Welcome to MyApp", color=BRIGHT_CYAN, width=60))
```

#### Alert Banners

```python
from typefx import alert_banner

print(alert_banner("Everything OK", level="success", width=50))
print(alert_banner("Disk at 85%", level="warning", width=50))
print(alert_banner("Connection lost", level="critical", width=50))
```

#### Progress Bars

```python
from typefx import progress_bar
from typefx.colors import GREEN, YELLOW

print(progress_bar(25, width=20, label="Download"))
print(progress_bar(50, width=20, label="Processing"))
print(progress_bar(100, width=20, label="Complete", color=GREEN))
```

#### ASCII Animals

```python
from typefx import animal, animal_names

# Specific animal
print(animal("dragon"))

# Random animal
print(animal())

# List all names
print(animal_names())
```

#### Kaomoji (Japanese Emoticons)

```python
from typefx import kaomoji, kaomoji_categories

# By category
print(kaomoji("happy"))
print(kaomoji("fight"))
print(kaomoji("cat"))

# List all categories
print(kaomoji_categories())

# Random
print(kaomoji())
```

#### Buddy / Mascot

```python
from typefx import buddy, buddy_box, buddy_multi
from typefx.colors import BRIGHT_CYAN

# Single mascot
buddy("MyApp", animal_name="cat1", color=BRIGHT_CYAN)

# With message
buddy("MyApp", animal_name="penguin2", color=BRIGHT_CYAN,
      message="Making terminals beautiful!")

# Boxed
buddy_box("MyApp", tagline="v2.0", animal_name="fox", color=BRIGHT_CYAN)

# Multi-animal team
buddy_multi("MyApp", animal_names=["cat1", "fox", "penguin2"],
            color=BRIGHT_CYAN)
```

#### Tags, Dividers, Frames & More

```python
from typefx import tag, divider, frame, centered_banner, section_header
from typefx.colors import CYAN, BRIGHT_CYAN

# Tags / badges
print(tag("INFO", color=BRIGHT_CYAN, bracket="square"))

# Divider with label
print(divider(length=50, label="Section", color=CYAN, align="center"))

# Frame art
print(frame("  Hello\n  World", box_style="double"))

# Centered banner
print(centered_banner("★ PyTypeFx ★", width=50, color=BRIGHT_CYAN))

# Section header
print(section_header("Features", color=CYAN, align="center"))
```

---

📚 For full documentation, see the [`docs/`](docs/index.md) folder:
- [Overview](docs/index.md)
- [API Reference](docs/api.md)
- [Usage Guide](docs/guide.md)
- [Examples](docs/examples.md)
- [Changelog](docs/changelog.md)

### Decorator

The `@typefx` decorator allows you to easily apply typing effects to the output of any function.

```python
from PyTypeFx import typefx

@typefx(hex_colors=["#FF0000", "#00FF00", "#0000FF"], delay=0.03)
def my_message():
    print("This message will be typed out with a cool effect!")

my_message()
```

### Command-Line Interface

You can also use TypeFx directly from your terminal.

```bash
typefx --text "Hello from the CLI!" --delay 0.05 --rainbow
```

**CLI Options:**

| Option | Description |
| --- | --- |
| `-t`, `--text` | Text to type. |
| `-d`, `--delay` | Delay between characters. |
| `-l`, `--loops` | Number of loops for effects like `LoopWriter`. |
| `-r`, `--rainbow` | Use the rainbow effect. |
| `-rnd`, `--random` | Use the random writer effect. |
| `-s`, `--sound` | Use the sound effect. |
| `-f`, `--file` | Read text from a file. |

## API Reference

### `writers`

The `writers` module contains all the typing effect functions. See the "Writers" section above for a full list.

### `effects`

- `BlinkEffect(duration: float, cursor: str, delay: float)`: Displays a blinking cursor.
- `SoundEffect(frequency: int, duration: int)`: Plays a sound (platform-dependent).

### `decorator`

- `@typefx(hex_colors=None, delay: float = 0.05, loop: int = 1, speed: str = "normal")`: A decorator to apply typewriter effects to function output.

### `colors`

The `colors` module provides a wide range of color and formatting constants, as well as helper functions:

- `hex_to_ansi(hex_color: str) -> str`: Converts a HEX color to an ANSI escape code.
- `rgb_to_ansi(r: int, g: int, b: int) -> str`: Converts an RGB color to an ANSI escape code.
- `colorize(text: str, *style: str) -> str`: Applies ANSI styles to text.

### `utility`

- `gradient(text: str, start_hex: str, end_hex: str) -> str`: Applies a color gradient to text.
- `supports_ansi() -> bool`: Checks if the terminal supports ANSI escape codes.

## Configuration

The `constant` module contains default values that can be customized:

| Constant | Default Value | Description |
| --- | --- | --- |
| `TEXT` | `"Hello World!"` | Default text for writers. |
| `GLITCH` | `"!@#$%^&*()_+-=[]{}|;':\",./<>?"` | Characters for the glitch effect. |
| `CURSOR` | `_` | Default cursor for `BlinkEffect`. |
| `DELAY` | `0.05` | Default delay between characters. |
| `DURATION` | `2` | Default duration for effects. |
| `HOLD` | `1` | Default hold time for `DelWriter`. |
| `LOOP` | `3` | Default number of loops. |
| `DOTS` | `3` | Default number of dots for `ThinkWriter`. |
| `FREQUENCY` | `800` | Default sound frequency. |
| `SOUND_DURATION` | `30` | Default sound duration. |
| `START_HEX` | `"#E74C3C"` | Default start color for gradients. |
| `END_HEX` | `"#2ECC71"` | Default end color for gradients. |

## Examples

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

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
