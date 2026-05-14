# Changelog

## v2.0.1 (2026-05-14)

### Added
- **25+ new ASCII animals**: lion, horse, cow, sheep, elephant, whale, dolphin, shark, snake, spider, butterfly, parrot, eagle, wolf, deer, chicken, hamster, mouse, sloth, dragon, bat, seal, octopus2, crab, dino, cat_love, dog_sleep, bunny3, penguin_dance (55 total)
- **12 new kaomoji categories**: greeting, wave, hug, sorry, thank, excited, nervous, cool, run, fight, magic, food, drink, music, rain, star, flower, cold (30 categories, 600+ kaomoji total)
- **40+ new emoji symbols**: zodiac signs, chess pieces, math symbols, arrows, hearts, currency, geometric shapes (90+ total)
- **7 new banner functions**:
  - `hero_banner()` — prominent hero banner with accent decorations
  - `alert_banner()` — contextual alert banners (info/success/warning/error/critical)
  - `progress_bar()` — visual progress bars with labels
  - `tag()` — badge/label generator with configurable brackets
  - `frame()` — frame ASCII art inside box styles
  - `centered_banner()` — text centered between fill characters
  - `buddy_multi()` — multiple animals side-by-side as mascots
- **Highly customizable parameters** on all existing functions:
  - `color` — text/foreground ANSI color
  - `align` — text alignment (left, center, right)
  - `padding` — internal spacing
  - `width` — output width control
  - `border_color` — box border color
  - `title_color` — title text color

### Changed
- All banner functions now accept optional customization parameters while maintaining full backward compatibility
- `box()` defaults unchanged but now supports color, align, padding, width, border_color, title_color
- `banner_block()` defaults to heavy box style (unchanged) with new box_style, border_color, bg_color params

### Documentation
- Created `docs/index.md` — module overview
- Created `docs/api.md` — full API reference
- Created `docs/guide.md` — usage guide with examples
- Created `docs/examples.md` — comprehensive runnable examples
- Created `docs/changelog.md` — version history

---

## v2.0.0 (2026-05-14)

### Added
- Full banner module (`typefx/banners.py`) with:
  - Box layouts: single, double, rounded, heavy, ascii, double_h, double_v
  - Banner templates: project_banner, banner_block, banner_arrow, banner_dash
  - Dividers and section headers
  - Color art helper
- 28 ASCII art animals (cat, dog, bunny, bear, penguin, bird, fish, owl, fox, pig, frog, koala, panda, turtle, monkey, octopus, alien, ghost, robot)
- 13 kaomoji categories (happy, sad, angry, love, shrug, cat, dog, bear, cute, surprise, sleep, dance, tableflip, party) — 200+ total
- 44 Unicode emoji symbols
- Buddy/mascot system — combine animals with project names
- New ANSI format codes: DOUBLE_UNDERLINE, CURLY_UNDERLINE, DOTTED_UNDERLINE, DASHED_UNDERLINE, SHADOW, SUPERSCRIPT, SUBSCRIPT
- fg_256(n) / bg_256(n) 8-bit ANSI color helpers
- 6 new color palettes: OCEAN, SUNSET, FOREST, CYBER, NOIR, ROSE
- Style presets: BOX_TITLE, BOX_LABEL, BOX_HINT, BOX_ERROR, BOX_SUCCESS, SECTION, SUBSECTION, SEPARATOR, ANCHOR, HIGHLIGHT_BG

---

## v1.0.0 (2026-05-13)

### Added
- Core typewriter effects: TypeWriter, RainbowWriter, HexWriter, DelWriter, LoopWriter
- Advanced writers: GlitchWriter, ReverseWriter, BounceWriter, ThinkWriter, RandomWriter
- Format writers: MarkdownWriter, HTMLWriter
- Game dialog system: GameDialog
- Sound effects: SoundWriter, SoundEffect
- Blinking cursor: BlinkEffect
- Color system: 16 basic + 16 bright + 50+ named colors + HEX/RGB converters
- Style preset system: ERROR, SUCCESS, WARNING, INFO, TITLE, HEADING, CODE, and more
- Gradient text utility
- @typefx decorator
- CLI interface
- Auto-complete writer
- Type safety with _types module
- Full test suite
