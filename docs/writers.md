# TypeFx Writers Module

The `typefx.writers` module provides text animation functions with various visual effects.

## TypeWriter

`TypeWriter(text, delay=0.05, color=None, style=(), reverse=False, position="left")`

Types out text character by character. Supports named colors, hex, rainbow, random modes, and ANSI styles.

```python
from typefx import TypeWriter
TypeWriter("Hello, world!", delay=0.03, color="cyan", style=("bold",))
```

## RainbowWriter

`RainbowWriter(text, delay=0.05, style=(), position="left")`

Types text cycling through rainbow colors.

```python
from typefx import RainbowWriter
RainbowWriter("Rainbow text!", delay=0.04)
```

## HexWriter

`HexWriter(text, delay=0.05, style=(), position="left")`

Types text cycling through predefined hex colors.

## DelWriter

`DelWriter(text, delay=0.05, color=None, style=(), reverse=False, position="left")`

Deletes and retypes text character by character, simulating a correction effect.

## LoopWriter

`LoopWriter(text, delay=0.05, color=None, style=(), reverse=False, position="left", loops=3)`

Repeatedly types and deletes the text in a loop.

```python
from typefx import LoopWriter
LoopWriter("Loading...", loops=5, delay=0.03, color="yellow")
```

## SoundWriter

`SoundWriter(text, delay=0.05, color=None, style=(), reverse=False, position="left", frequency=440, duration=0.1)`

Types text with beep sounds on each character. Requires a terminal that supports `\a` bell characters.

## GameDialog

`GameDialog(text, delay=0.05, color=None, style=(), position="left")`

Types text character by character with an optional box around the output, styled like a game dialog box.

```python
from typefx import GameDialog
GameDialog("Hello, adventurer!", delay=0.03, color="green")
```

## RandomWriter

`RandomWriter(text, delay=0.05, style=(), position="left")`

Types text with each character in a randomly chosen color.

## MarkdownWriter

`MarkdownWriter(text, delay=0.05, style=(), position="left")`

Types markdown-formatted text, rendering bold (`**text**`), italic (`*text*`), and underline (`__text__`) inline.

```python
from typefx import MarkdownWriter
MarkdownWriter("This is **bold** and *italic* text.")
```

## HTMLWriter

`HTMLWriter(text, delay=0.05, style=(), position="left")`

Types HTML-formatted text, rendering `<b>`, `<i>`, `<u>`, `<s>`, `<blink>` tags inline.

```python
from typefx import HTMLWriter
HTMLWriter("This is <b>bold</b> and <i>italic</i> text.")
```

## GlitchWriter

`GlitchWriter(text, delay=0.05, color=None, style=(), position="left", glitch_chars=5, glitch_duration=5)`

Types text with a glitch effect where random characters briefly appear and resolve into the final text.

```python
from typefx import GlitchWriter
GlitchWriter("SYSTEM ONLINE", delay=0.05, color="green")
```

## ThinkWriter

`ThinkWriter(text, delay=0.05, color=None, style=(), position="left")`

Types text with a blinking ellipsis animation before the text appears.

## ReverseWriter

`ReverseWriter(text, delay=0.05, color=None, style=(), position="left")`

Types text in reverse order (last character first).

## ReverseGlitchWriter

`ReverseGlitchWriter(text, delay=0.05, color=None, style=(), position="left")`

Combines reverse typing with glitch effects.

## BounceWriter

`BounceWriter(text, delay=0.05, color=None, style=(), position="left")`

Types text with each character temporarily highlighted (bright/bold) as it appears, creating a bouncing effect.

```python
from typefx import BounceWriter
BounceWriter("BOUNCE!", delay=0.08, color="cyan")
```

## BounceGlitchWriter

`BounceGlitchWriter(text, delay=0.05, color=None, style=(), position="left")`

Combines bounce and glitch effects.

## GradientWriter

`GradientWriter(text, delay=0.05, style=(), position="left", start_hex="#ff0000", end_hex="#0000ff")`

Types text with a smooth color gradient from start_hex to end_hex.

```python
from typefx import GradientWriter
GradientWriter("Gradient text!", start_hex="#ff0000", end_hex="#00ff00")
```

## AutoCompleteWriter

`AutoCompleteWriter(text, delay=0.05, color=None, style=(), position="left", options=None)`

Types text with an autocomplete-style animation where random characters cycle before the correct one lands.

## Common Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `text` | `str` | `"TypeFx"` | The text to display |
| `delay` | `float` | `0.05` | Seconds between each character |
| `color` | `str` | `None` | Named color, hex, palette, rainbow, random |
| `style` | `tuple` | `()` | ANSI style codes (bold, underline, etc.) |
| `position` | `str` | `"left"` | Alignment: left, center, right |
| `reverse` | `bool` | `False` | Type in reverse order |
