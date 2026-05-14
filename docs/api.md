# TypeFx Banners API Reference

## Constants

### `BOX_STYLES`
Dictionary of box-drawing character sets. Keys: `single`, `double`, `rounded`, `heavy`, `ascii`, `double_h`, `double_v`. Each value is a dict with keys: `tl`, `tr`, `bl`, `br`, `h`, `v`.

### `KAOMOJI`
Dictionary mapping category names to lists of kaomoji strings. 30+ categories: happy, sad, angry, love, shrug, cat, dog, bear, cute, surprise, sleep, dance, tableflip, party, greeting, wave, hug, sorry, thank, excited, nervous, cool, run, fight, magic, food, drink, music, rain, star, flower, cold.

### `ALL_KAOMOJI`
Flat list of all kaomoji strings.

### `ANIMALS`
Dictionary mapping animal names to ASCII art strings. 50+ animals: cat1-3, cat_sleep, cat_love, dog1-2, dog_sleep, bunny1-3, bear1-2, penguin1-2, penguin_dance, bird1-2, fish1-2, owl, fox, pig, frog, koala, panda, turtle, monkey, octopus, octopus2, alien, ghost, robot, lion, horse, cow, sheep, elephant, whale, dolphin, shark, snake, spider, butterfly, parrot, eagle, wolf, deer, chicken, hamster, mouse, sloth, dragon, bat, seal, crab, dino.

### `ANIMAL_NAMES`
Flat list of all animal name strings.

### `EMOJI`
Dictionary mapping emoji names to Unicode characters. 90+ symbols including hearts, stars, arrows, zodiac, chess, math, currency, geometric shapes, and more.

### `ALL_EMOJI_NAMES`
Flat list of all emoji name strings.

### `ALERT_STYLES`
Dictionary mapping alert level names to config dicts with `label` and `color` keys. Levels: info, success, warning, error, critical.

## Functions

### Box & Frame Functions

#### `box(text, style="single", title=None, color=None, align="left", padding=0, width=None, border_color=None, title_color=None) -> str`
Wraps text in a box drawn with box-drawing characters.

- **text** — Content to box
- **style** — Box style key from BOX_STYLES
- **title** — Optional title displayed in the top border
- **color** — ANSI color for text inside the box
- **align** — Text alignment: "left", "center", "right"
- **padding** — Number of spaces/blank lines around content
- **width** — Minimum box width
- **border_color** — ANSI color for all border characters
- **title_color** — ANSI color for the title

#### `frame(art, box_style="rounded", padding=1, border_color=None, title=None, title_color=None) -> str`
Convenience wrapper around `box()` for framing ASCII art. Adds 1 padding by default.

### Banner Functions

#### `project_banner(name, tagline=None, version=None, color=BRIGHT_CYAN, accent=GREEN, width=40, align="center", border_style="double", border_color=None) -> str`
Creates a project header banner with name, tagline, and version.

#### `hero_banner(text, color=BRIGHT_CYAN, width=60, accent_char="★", align="center", border_style="heavy", padding=0) -> str`
Creates a prominent hero banner with accent characters on either side of the text.

#### `alert_banner(text, level="info", width=60, align="left", border_style="single") -> str`
Creates a colored alert banner with level label. Levels: info, success, warning, error, critical.

#### `banner_block(text, color=BRIGHT_CYAN, bold=True, align="center", padding=0, width=None, box_style="heavy", border_color=None, bg_color=None) -> str`
Creates a boxed banner block with optional bold text and background color.

#### `banner_arrow(text, color=BRIGHT_CYAN, bold=True, arrow_char="▸", align="left", padding=0, width=None) -> str`
Creates an arrow-pointing banner.

#### `banner_dash(text, color=BRIGHT_WHITE, bold=True, dash_char="─", align="center", width=None) -> str`
Creates a dash-delimited banner.

#### `centered_banner(text, width=50, fill="─", color=CYAN, bold=True, padding=0) -> str`
Creates text centered between fill characters.

### Divider & Rule Functions

#### `divider(char="━", length=40, label=None, color=None, align="center") -> str`
Creates a horizontal divider line with optional label.

- **align** — Label placement: "left", "center", "right"

#### `rule(color=CYAN, char="━", length=50, label=None) -> str`
Creates a colored horizontal rule with optional label.

#### `section_header(text, width=50, color=CYAN, align="left", char="─", padding=0, bottom_line=True) -> str`
Creates a section header with top/bottom lines.

### Utility Functions

#### `progress_bar(pct=50.0, width=20, color=None, fill_char="█", empty_char="░", show_pct=True, label=None) -> str`
Creates a text-based progress bar.

#### `tag(text, color=BRIGHT_CYAN, invert=False, bold=True, bracket="square") -> str`
Creates a small label/badge. Brackets: square, round, curly, angle, none.

#### `color_art(art, color=BRIGHT_CYAN, bg_color=None, align="left", padding=0, width=None) -> str`
Applies ANSI color(s) to ASCII art with alignment and padding.

### Animal Functions

#### `animal(name=None) -> str`
Returns an ASCII art animal. If name is None, returns a random animal.

#### `animal_names() -> list`
Returns a list of all available animal names.

### Kaomoji Functions

#### `kaomoji(category=None) -> str`
Returns a random kaomoji, optionally from a specific category.

#### `kaomoji_list(category=None) -> list`
Returns all kaomoji, optionally filtered by category.

#### `kaomoji_categories() -> list`
Returns all kaomoji category names.

### Emoji Functions

#### `emoji(name=None) -> str`
Returns an emoji symbol. If name is None, returns a random one.

#### `emoji_names() -> list`
Returns all available emoji names.

### Buddy / Mascot Functions

#### `buddy(project, animal_name=None, color=BRIGHT_CYAN, align="left", message=None, message_color=None, show_name=True) -> str`
Creates a mascot display combining an ASCII animal with a project name.

#### `buddy_box(project, tagline=None, animal_name=None, color=BRIGHT_CYAN, box_style="rounded", align="left", padding=0, border_color=None, message=None, message_color=None) -> str`
Creates a boxed mascot display.

#### `buddy_multi(project, animal_names=None, color=BRIGHT_CYAN, count=2, spacing=2, message=None, message_color=None) -> str`
Creates a multi-animal mascot display with animals shown side-by-side.
