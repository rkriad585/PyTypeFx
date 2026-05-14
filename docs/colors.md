# TypeFx Colors Module

The `typefx.colors` module provides ANSI escape code constants and helpers for terminal color output.

## Format Codes

| Constant | Effect |
| --- | --- |
| `RESET` | Reset all styles |
| `BOLD` | Bold / bright text |
| `BIM` | Dim text |
| `UNDERLINE` | Single underline |
| `DOUBLE_UNDERLINE` | Double underline |
| `CURLY_UNDERLINE` | Curly underline |
| `DOTTED_UNDERLINE` | Dotted underline |
| `DASHED_UNDERLINE` | Dashed underline |
| `ITALIC` | Italic text |
| `BLINK` | Slow blink |
| `BLINK_FAST` | Fast blink |
| `BLINK_SLOW` | Slow blink |
| `INVERT` | Reverse/invert colors |
| `CONCEAL` | Concealed text |
| `STRIKETHROUGH` | Strikethrough text |
| `OVERLINE` | Overline text |
| `FRAME` | Framed text |
| `ENCIRCLE` | Encircled text |
| `SHADOW` | Shadow text |
| `SUPERSCRIPT` | Superscript |
| `SUBSCRIPT` | Subscript |
| `BRIGHT` | Bright foreground |
| `BRIGHT_FOREGROUND` | Bright foreground |
| `BRIGHT_BACKGROUND` | Bright background |

## Foreground Colors

### Basic (16)
`BLACK`, `RED`, `GREEN`, `YELLOW`, `BLUE`, `MAGENTA`, `CYAN`, `WHITE`, `GRAY`

### Bright (8)
`BRIGHT_RED`, `BRIGHT_GREEN`, `BRIGHT_YELLOW`, `BRIGHT_BLUE`, `BRIGHT_MAGENTA`, `BRIGHT_CYAN`, `BRIGHT_WHITE`, `BRIGHT_BLACK`

### Extended Named (50+)
`ORANGE`, `PURPLE`, `PINK`, `TEAL`, `VIOLET`, `TURQUOISE`, `LIME`, `GOLD`, `SILVER`, `MARRON`, `NAVY`, `OLIVE`, `CORAL`, `SKYBLUE`, `AQUA`, `INDIGO`, `BROWN`, `AMBER`, `CRIMSON`, `SALMON`, `PLUM`, `SLATE`, `TOMATO`, `CHOCOLATE`, `PEACH`, `MINT`, `CORNFLOWER`, `SPRING_GREEN`, `SEA_GREEN`, `STEEL_BLUE`, `DODGER_BLUE`, `DARK_ORCHID`, `SIENNA`, `PERU`, `ROSY_BROWN`, `KHAKI`, `CHARCOAL`, `CERULEAN`, `CRANBERRY`, `WINE`, `LILAC`, `FUCHSIA`, `MAUVE`, `MIDNIGHT_BLUE`, `LEAF_GREEN`, `GRASS_GREEN`, `MOSS_GREEN`, `FERN_GREEN`, `PINE_GREEN`, `SAGE_GREEN`, `OLIVE_DRAB`, `TAUPE`, `TAN`, `WALNUT`, `SUNFLOWER`, `ROSE_PINK`, `LAVENDER`, `PETAL_RED`, `SKY_BLUE`, `CLOUD_WHITE`, `RAIN_GRAY`, and more.

## Background Colors

All foreground colors have `BG_` prefixed variants: `BG_RED`, `BG_GREEN`, `BG_BRIGHT_CYAN`, `BG_ORANGE`, `BG_MINT`, etc.

## Color Palettes

The `PALETTES` dict provides themed color sets:

| Palette | Colors |
| --- | --- |
| `SUCCESS` | Green tones |
| `ERROR` | Red tones |
| `WARNING` | Yellow/orange tones |
| `INFO` | Blue tones |
| `NEON` | #39FF14, #FF00FF, #00FFFF, #FFFF00 |
| `PASTEL` | Soft pink, blue, green, purple |
| `OCEAN` | Deep blue to light cyan |
| `SUNSET` | Red to orange to yellow to green |
| `FOREST` | Dark to light green |
| `GARDEN` | Multi-color nature tones |
| `CYBER` | Matrix green, magenta, cyan, yellow, orange |
| `NOIR` | Grayscale from black to white |
| `ROSE` | Pink/magenta tones |

## Helper Functions

### hex_to_ansi(hex_color) -> str
Converts a hex color string to ANSI foreground code.
```python
from typefx.colors import hex_to_ansi
print(hex_to_ansi("#FF5733"))  # \033[38;2;255;87;51m
```

### bg_hex_to_ansi(hex_color) -> str
Converts a hex color string to ANSI background code.

### rgb_to_ansi(r, g, b) -> str
Converts RGB values to ANSI foreground code.

### bg_rgb_to_ansi(r, g, b) -> str
Converts RGB values to ANSI background code.

### fg_256(n) -> str
Returns ANSI 8-bit (256-color) foreground code. n must be 0-255.

### bg_256(n) -> str
Returns ANSI 8-bit (256-color) background code.

### colorize(text, *styles) -> str
Applies multiple ANSI style codes to text.
```python
from typefx.colors import colorize, RED, BOLD, UNDERLINE
print(colorize("Error!", RED, BOLD, UNDERLINE))
```
