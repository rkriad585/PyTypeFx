# TypeFx Styles Module

The `typefx.styles` module provides composable style presets for easy text formatting.

## Overview

Styles are dicts with optional `"color"` and `"style"` keys that can be unpacked with `**` into any writer function or used directly with `apply_style()`.`

## Style Presets

### Feedback / Status
| Style | Appearance |
| --- | --- |
| `ERROR` | Red + Bold |
| `SUCCESS` | Green + Bold |
| `WARNING` | Yellow + Bold |
| `INFO` | Cyan + Italic |
| `DANGER` | Bright Red + Bold + Blink |
| `CRITICAL` | Bright Red + Bold + Invert |
| `DEBUG` | Bright Black + Dim |
| `TRACE` | Bright Black + Italic |
| `LOG` | Bright Black |

### Typography
| Style | Appearance |
| --- | --- |
| `TITLE` | Bright White + Bold + Underline |
| `HEADING` | Bright Cyan + Bold |
| `SUBHEADING` | Bright Blue + Italic |
| `CODE` | Bright Green + Italic |
| `KEYWORD` | Bright Magenta + Bold |
| `LINK` | Bright Cyan + Underline |
| `QUOTE` | White + Italic |
| `CAPTION` | Bright Black + Italic |
| `LABEL` | Bright Cyan + Dim |
| `TAG` | Bright Magenta + Dim + Invert |
| `BOLD_STYLE` | Bold only |
| `UNDERLINE_STYLE` | Underline only |
| `OVERLINE_STYLE` | Overline only |

### Themed
| Style | Appearance |
| --- | --- |
| `NEON` | Bold + Bright Magenta + Bright Cyan |
| `GHOST` | Dim |
| `MUTED` | Black + Dim |
| `PUNCH` | Bright White + Bold + Invert |
| `EMPHASIS` | Bright Yellow + Bold + Underline |
| `BANNER` | Bright Cyan + Bold + Overline + Underline |

### Section / Box
| Style | Appearance |
| --- | --- |
| `SECTION` | Cyan + Bold + Double Underline |
| `SUBSECTION` | Bright Cyan + Bold |
| `SEPARATOR` | Bright Black + Dim |
| `ANCHOR` | Bright Cyan + Underline |
| `HIGHLIGHT_BG` | Yellow + Bold + Invert |
| `BOX_TITLE` | Bright Cyan + Bold + Underline |
| `BOX_LABEL` | Bright Blue + Bold |
| `BOX_HINT` | Bright Black + Italic |
| `BOX_ERROR` | Red + Bold + Invert |
| `BOX_SUCCESS` | Green + Bold + Invert |

### Semantic
| Style | Appearance |
| --- | --- |
| `IMPORTANT` | Bright Yellow + Bold + Underline |
| `NOTE` | Blue + Italic |
| `TIP` | Bright Green + Italic |
| `HINT` | Bright Cyan + Dim + Italic |
| `PRIMARY` | Bright Blue + Bold |
| `SECONDARY` | White + Dim |
| `ACCENT` | Bright Magenta + Bold |
| `VERBOSE` | Bright Black + Italic + Dim |
| `META` | Bright Blue + Italic |
| `DIM` | Dim |
| `HIGHLIGHT` | Yellow + Bold + Invert |
| `STRIKETHROUGH` | Strikethrough |

## Helper Functions

### compose(color, *formats) -> dict
Builds a style dict from a color code and optional format codes.
```python
from typefx.styles import compose
from typefx.colors import RED, BOLD, UNDERLINE
style = compose(RED, BOLD, UNDERLINE)
```

### apply_style(text, style) -> str
Applies a style dict directly to a string.
```python
from typefx.styles import apply_style, ERROR
print(apply_style("Something went wrong!", ERROR))
```

## Usage with Writers

Styles can be unpacked into any writer:
```python
from typefx import TypeWriter
from typefx.styles import ERROR, SUCCESS, TITLE

TypeWriter("Error message", **ERROR)
TypeWriter("Success message", **SUCCESS)
TypeWriter("Title text", **TITLE)
```

## Custom Styles

Build your own with `compose()`:
```python
from typefx.styles import compose
from typefx.colors import BRIGHT_MAGENTA, BRIGHT_CYAN, INVERT, BOLD

custom = compose(BRIGHT_MAGENTA, BRIGHT_CYAN, INVERT, BOLD)
TypeWriter("Custom styled!", **custom)
```
