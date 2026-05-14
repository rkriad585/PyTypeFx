import itertools
import random
import re
import sys
import time

from typing import List, Tuple

from typefx._types import Position

from typefx.constant import (
    DELAY,
    DOTS,
    END_HEX,
    FREQUENCY,
    GLITCH,
    HEX_COLORS,
    HOLD,
    LOOP,
    RESET,
    RGB_COLORS,
    SOUND_DURATION,
    START_HEX,
    TEXT,
)
from typefx.effects import SoundEffect
from typefx.utility import (
    _clear_line,
    _cursor_left,
    _make_style,
    _position_prefix,
    _resolve_to_ansi_list,
    gradient,
    hex_to_ansi,
    rgb_to_ansi,
    write,
)


# TypeWriter functions
def TypeWriter(
    text: str = TEXT,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types out text character by character with a typewriter effect.

    Each character is printed individually with an optional delay, supporting
    flexible color modes (named colors, hex strings, palettes, rainbow, random),
    ANSI text styles (bold, underline, etc.), and reverse order output.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    delay : float, optional
        Delay in seconds between each character. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Accepts ANSI color strings, hex strings (e.g. "#FF0000"),
        palette names ("SUCCESS", "NEON"), "rainbow", "random", or a list of any
        of these. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants (e.g. (BOLD, UNDERLINE)). Defaults to ().
    reverse : bool, optional
        If True, types the text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> TypeWriter("Hello", delay=0.05)
    5
    >>> TypeWriter("Hi", delay=0, color="rainbow", style=(BOLD,))
    2
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    chars = reversed(text) if reverse else text

    if delay <= 0:
        out = "".join(
            f"{prefix}{style_str}{next(itertools.cycle(colors))}{ch}{RESET}"
            for ch in chars
        )
        print(out)
        return len(text)

    if prefix:
        sys.stdout.write(prefix)

    color_cycle = itertools.cycle(colors) if colors else None

    for ch in chars:
        if color_cycle:
            sys.stdout.write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            sys.stdout.write(f"{style_str}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()
    return len(text)


def RainbowWriter(
    text: str = TEXT,
    delay: float = DELAY,
    colors: tuple = (),
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types text cycling through rainbow colors.

    Each character is printed in a different color from the rainbow spectrum.
    Supports an explicit `colors` parameter of RGB tuples for custom palettes,
    or the flexible `color` parameter for named/hex/palette inputs.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    delay : float, optional
        Delay in seconds between each character. Defaults to DELAY.
    colors : tuple, optional
        Tuple of (R, G, B) tuples for explicit rainbow colors.
    color : str, list, or None, optional
        Alternative color specification. Defaults to "rainbow" when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types the text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> RainbowWriter("Rainbow", delay=0.05)
    7
    >>> RainbowWriter("RGB", delay=0, colors=((255,0,0), (0,255,0), (0,0,255)))
    3
    """
    if colors:
        resolved = [
            rgb_to_ansi(r, g, b) for r, g, b in colors
        ]
    else:
        resolved = _resolve_to_ansi_list(color if color is not None else "rainbow")
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    chars = reversed(text) if reverse else text

    if delay <= 0:
        out = "".join(
            f"{prefix}{style_str}{next(itertools.cycle(resolved))}{ch}{RESET}"
            for ch in chars
        )
        print(out)
        return len(text)

    if prefix:
        sys.stdout.write(prefix)

    resolved_cycle = itertools.cycle(resolved) if resolved else None

    for ch in chars:
        if resolved_cycle:
            sys.stdout.write(f"{style_str}{next(resolved_cycle)}{ch}{RESET}")
        else:
            sys.stdout.write(f"{style_str}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()
    return len(text)


def HexWriter(
    text: str = TEXT,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types text using customizable hex colors for each character.

    Cycles through the provided colors, applying a new color per character.
    Uses the flexible color resolution system for broad input compatibility.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    delay : float, optional
        Delay in seconds between each character. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Accepts hex strings, named ANSI colors,
        palette names, "rainbow", "random", or lists thereof.
        Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types the text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> HexWriter("RedBlue", delay=0.05, color=["#FF0000", "#0000FF"])
    7
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    chars = reversed(text) if reverse else text

    if delay <= 0:
        out = "".join(
            f"{prefix}{style_str}{next(itertools.cycle(colors))}{ch}{RESET}"
            for ch in chars
        )
        print(out)
        return len(text)

    if prefix:
        sys.stdout.write(prefix)

    color_cycle = itertools.cycle(colors) if colors else None

    for ch in chars:
        if color_cycle:
            sys.stdout.write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            sys.stdout.write(f"{style_str}{ch}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()
    return len(text)


def DelWriter(
    text: str = TEXT,
    delay: float = DELAY,
    hold: int = HOLD,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types out text, pauses, then deletes it character by character.

    Each character is printed with a typewriter effect, held on screen
    for the specified duration, then erased from right to left.

    Parameters
    ----------
    text : str, optional
        The text to write and delete. Defaults to TEXT.
    delay : float, optional
        Delay in seconds for typing and deleting. Defaults to DELAY.
    hold : int, optional
        Time in seconds to hold the full text before deleting. Defaults to HOLD.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types the text in reverse order before deleting. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> DelWriter("Temporary", delay=0.01, hold=0.5)
    9
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    color_cycle = itertools.cycle(colors) if colors else None
    chars = reversed(text) if reverse else text

    if prefix:
        write(prefix)

    for char in chars:
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{char}{RESET}")
        else:
            write(f"{style_str}{char}{RESET}")
        time.sleep(delay)
    time.sleep(hold)
    for _ in range(len(text)):
        write(_clear_line(1))
        time.sleep(delay)
    print()
    return len(text)


def LoopWriter(
    text: str = TEXT,
    loops: int = LOOP,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Repeats the type-and-delete animation multiple times.

    Each loop calls DelWriter to produce a write-hold-erase sequence,
    creating a continuous looping visual effect.

    Parameters
    ----------
    text : str, optional
        The text for the animation. Defaults to TEXT.
    loops : int, optional
        The number of times to repeat the animation. Defaults to LOOP.
    delay : float, optional
        The typing/deleting delay. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types in reverse each loop. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters in the text.

    Examples
    --------
    >>> LoopWriter("Repeat", loops=2, delay=0.01)
    6
    """
    for _ in range(loops):
        DelWriter(text, delay, color=color, style=style, reverse=reverse, position=position)
    return len(text)


def SoundWriter(
    text: str = TEXT,
    delay: float = DELAY,
    sound: bool = True,
    frequency: int = FREQUENCY,
    duration: int = SOUND_DURATION,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types text with optional sound effects on each character.

    Each character is printed with an audible beep when `sound` is True.
    Sound plays asynchronously using a daemon thread to avoid blocking.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    delay : float, optional
        Delay in seconds between characters. Defaults to DELAY.
    sound : bool, optional
        Whether to play a beep per character. Defaults to True.
    frequency : int, optional
        Frequency of the beep in Hertz. Defaults to FREQUENCY.
    duration : int, optional
        Duration of the beep in milliseconds. Defaults to SOUND_DURATION.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types the text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> SoundWriter("Beep", delay=0.1, sound=False)
    4
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    color_cycle = itertools.cycle(colors) if colors else None
    chars = reversed(text) if reverse else text

    if prefix:
        write(prefix)

    for ch in chars:
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            write(f"{style_str}{ch}{RESET}")
        if sound:
            SoundEffect(frequency, duration)
        time.sleep(delay)
    print()
    return len(text)


def GameDialog(
    speaker: str = "NPC",
    text: str = TEXT,
    delay: float = DELAY,
    sound: bool = False,
    frequency: int = FREQUENCY,
    duration: int = SOUND_DURATION,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Displays text in a bordered dialog box, as seen in games.

    Renders a dialog frame with speaker name and typewriter-effect text,
    optionally with per-character sound effects.

    Parameters
    ----------
    speaker : str, optional
        The name of the speaker. Defaults to "NPC".
    text : str, optional
        The dialog text. Defaults to TEXT.
    delay : float, optional
        The typing delay. Defaults to DELAY.
    sound : bool, optional
        Whether to play a sound per character. Defaults to False.
    frequency : int, optional
        Sound frequency in Hertz. Defaults to FREQUENCY.
    duration : int, optional
        Sound duration in milliseconds. Defaults to SOUND_DURATION.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters in the text.

    Examples
    --------
    >>> GameDialog("Hero", "I must save the world!", delay=0.01)
    22
    """
    border = "─" * (len(text) + 10)
    print(f"┌{border}┐")
    print(f"│ {speaker}: ", end="")
    if sound:
        SoundWriter(text, delay, frequency=frequency, duration=duration, color=color, style=style, reverse=reverse, position=position)
    else:
        TypeWriter(text, delay, color=color, style=style, reverse=reverse, position=position)
    print(f"└{border}┘")
    return len(text)


def RandomWriter(
    text: str = TEXT,
    delay: float = DELAY - 0.01,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types text with variable delays simulating human typing pauses.

    Adds longer pauses after punctuation (periods, commas) and spaces,
    plus small random jitter to each delay for a natural feel.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    delay : float, optional
        Base delay between characters. Automatically adjusted for
        punctuation. Defaults to DELAY - 0.01.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types the text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> RandomWriter("Hello. How are you?", delay=0.02)
    19
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    chars = reversed(text) if reverse else text

    if delay <= 0 and colors:
        out = "".join(
            f"{prefix}{style_str}{next(itertools.cycle(colors))}{ch}{RESET}"
            for ch in chars
        )
        print(out)
        return len(text)

    if prefix:
        write(prefix)

    color_cycle = itertools.cycle(colors) if colors else None

    for ch in chars:
        base = delay
        if ch in ".!?":
            base *= 6
        elif ch in ",":
            base *= 2
        elif ch in " ":
            base *= 1.5

        base += random.uniform(0.0, 0.03)
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            write(f"{style_str}{ch}{RESET}")
        time.sleep(base)
    print()
    return len(text)


def MarkdownWriter(
    md_text: str = TEXT,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Strips Markdown formatting and types out the clean text.

    Removes common Markdown syntax (bold **, italic *, headers #, code `,
    strikethrough ~~) before passing to TypeWriter.

    Parameters
    ----------
    md_text : str, optional
        The Markdown-formatted text. Defaults to TEXT.
    delay : float, optional
        The typing delay. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types text in reverse. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters written (after cleaning).

    Examples
    --------
    >>> MarkdownWriter("**Hello** `World`!", delay=0.01)
    11
    """
    clean = re.sub(r"[*_#>`~-]", "", md_text)
    return TypeWriter(text=clean, delay=delay, color=color, style=style, reverse=reverse, position=position)


def HTMLWriter(
    html_text: str = TEXT,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Strips HTML tags and types out the clean text.

    Removes all HTML/XML tags using regex before passing to TypeWriter,
    leaving only the visible text content.

    Parameters
    ----------
    html_text : str, optional
        The HTML-formatted text. Defaults to TEXT.
    delay : float, optional
        The typing delay. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types text in reverse. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters written (after cleaning).

    Examples
    --------
    >>> HTMLWriter("<p>Hello <b>World</b></p>", delay=0.01)
    10
    """
    clean = re.sub(r"<[^>]*>", "", html_text)
    return TypeWriter(text=clean, delay=delay, color=color, style=style, reverse=reverse, position=position)


def GlitchWriter(
    text: str = TEXT,
    glitch: str = GLITCH,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types text with a glitch effect — random characters appear before settling.

    For each character, a random glitch symbol is shown briefly, then replaced
    by the correct character, creating a digital distortion aesthetic.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    glitch : str, optional
        String of characters to use as glitch filler. Defaults to GLITCH.
    delay : float, optional
        Delay in seconds between characters. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    reverse : bool, optional
        If True, types text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> GlitchWriter("Hi", delay=0.02)
    2
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    chars = reversed(text) if reverse else text
    color_cycle = itertools.cycle(colors) if colors else None

    if prefix:
        write(prefix)

    for ch in chars:
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{random.choice(glitch)}{RESET}")
            time.sleep(delay)
            write(f"{_cursor_left()}{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            write(f"{style_str}{random.choice(glitch)}{RESET}")
            time.sleep(delay)
            write(f"{_cursor_left()}{style_str}{ch}{RESET}")
    print()
    return len(text)


def ThinkWriter(
    text: str = TEXT,
    dots: int = DOTS,
    loop: int = LOOP,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    position: Position = "left",
) -> int:
    """
    Simulates a thinking/loading animation with text and trailing dots.

    Repeatedly displays the message followed by an expanding dot sequence,
    then clears and repeats. Useful for loading indicators.

    Parameters
    ----------
    text : str, optional
        The thinking message text. Defaults to TEXT.
    dots : int, optional
        Number of trailing dots in the animation. Defaults to DOTS.
    loop : int, optional
        Number of animation cycles. Defaults to LOOP.
    delay : float, optional
        Delay between dot additions. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters in the text.

    Examples
    --------
    >>> ThinkWriter("Loading", dots=3, loop=1, delay=0.1)
    7
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    color_cycle = itertools.cycle(colors) if colors else None

    if prefix:
        write(prefix)

    for _ in range(loop):
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{text}{RESET}")
        else:
            write(f"{style_str}{text}{RESET}")
        for _ in range(dots):
            write(".")
            time.sleep(delay)
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{_clear_line(len(text) + dots)}{RESET}")
        else:
            write(f"{style_str}{_clear_line(len(text) + dots)}{RESET}")
    print()
    return len(text)


def ReverseWriter(
    text: str = TEXT,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    position: Position = "left",
) -> int:
    """
    Types text in reverse order (backwards).

    Each character is printed from the end of the string to the beginning,
    producing a reversed typing effect.

    Parameters
    ----------
    text : str, optional
        The text to type backwards. Defaults to TEXT.
    delay : float, optional
        Delay in seconds between characters. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> ReverseWriter("hello", delay=0.05)
    5
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)

    if delay <= 0 and colors:
        out = "".join(
            f"{prefix}{style_str}{next(itertools.cycle(colors))}{ch}{RESET}"
            for ch in reversed(text)
        )
        print(out)
        return len(text)

    if prefix:
        write(prefix)

    color_cycle = itertools.cycle(colors) if colors else None

    for ch in reversed(text):
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            write(f"{style_str}{ch}{RESET}")
        time.sleep(delay)
    print()
    return len(text)


def ReverseGlitchWriter(
    text: str = TEXT,
    glitch: str = GLITCH,
    delay: float = DELAY,
    color=None,
    style: tuple = (),
    position: Position = "left",
) -> int:
    """
    Types text in reverse with a glitch distortion effect.

    Combines the reverse-order output of ReverseWriter with the
    glitch character substitution of GlitchWriter.

    Parameters
    ----------
    text : str, optional
        The text to type. Defaults to TEXT.
    glitch : str, optional
        String of glitch characters. Defaults to GLITCH.
    delay : float, optional
        Delay in seconds between characters. Defaults to DELAY.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> ReverseGlitchWriter("ABC", delay=0.02)
    3
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    color_cycle = itertools.cycle(colors) if colors else None

    if prefix:
        write(prefix)

    for ch in reversed(text):
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{random.choice(glitch)}{RESET}")
            time.sleep(delay)
            write(f"{style_str}{next(color_cycle)}{_cursor_left()}{ch}{RESET}")
        else:
            write(f"{style_str}{random.choice(glitch)}{RESET}")
            time.sleep(delay)
            write(f"{style_str}{_cursor_left()}{ch}{RESET}")
    print()
    return len(text)


def BounceWriter(
    text: str = TEXT,
    delay: float = DELAY,
    loop: int = LOOP,
    color=None,
    style: tuple = (),
    position: Position = "left",
) -> int:
    """
    Animates text bouncing in and out character by character.

    Each loop types the text left-to-right, then erases it left-to-right,
    creating a bouncing cursor effect.

    Parameters
    ----------
    text : str, optional
        The text to animate. Defaults to TEXT.
    delay : float, optional
        Delay between each step. Defaults to DELAY.
    loop : int, optional
        Number of bounce cycles. Defaults to LOOP.
    color : str, list, or None, optional
        Color specification. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters in the text.

    Examples
    --------
    >>> BounceWriter("Hi", delay=0.02, loop=1)
    2
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    color_cycle = itertools.cycle(colors) if colors else None

    if prefix:
        write(prefix)

    for _ in range(loop):
        for ch in text:
            if color_cycle:
                write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
            else:
                write(f"{style_str}{ch}{RESET}")
            time.sleep(delay)

        for _ in text:
            if color_cycle:
                write(f"{style_str}{next(color_cycle)}{_clear_line(1)}{RESET}")
            else:
                write(f"{style_str}{_clear_line(1)}{RESET}")
            time.sleep(delay)
    print()
    return len(text)


def BounceGlitchWriter(
    text: str = TEXT,
    glitch: str = GLITCH,
    delay: float = DELAY,
    loop: int = LOOP,
    glitch_color=None,
    color=None,
    style: tuple = (),
    position: Position = "left",
) -> int:
    """
    Bounce animation with glitch distortion during the type phase.

    Combines the bounce type-erase cycle with glitch effects — random
    symbols appear before each character during the forward pass.

    Parameters
    ----------
    text : str, optional
        The text to animate. Defaults to TEXT.
    glitch : str, optional
        String of glitch characters. Defaults to GLITCH.
    delay : float, optional
        Delay between each step. Defaults to DELAY.
    loop : int, optional
        Number of bounce cycles. Defaults to LOOP.
    glitch_color : str, list, or None, optional
        Color for glitch characters. Defaults to HEX_COLORS when None.
    color : str, list, or None, optional
        Color for actual text characters. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants. Defaults to ().
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters in the text.

    Examples
    --------
    >>> BounceGlitchWriter("AB", delay=0.02, loop=1)
    2
    """
    glitch_colors = _resolve_to_ansi_list(glitch_color if glitch_color is not None else HEX_COLORS)
    text_colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    prefix = _position_prefix(len(text), position)
    glitch_cycle = itertools.cycle(glitch_colors) if glitch_colors else None
    text_cycle = itertools.cycle(text_colors) if text_colors else None

    if prefix:
        write(prefix)

    for _ in range(loop):
        for ch in text:
            if glitch_cycle:
                write(f"{style_str}{next(glitch_cycle)}{random.choice(glitch)}{RESET}")
            else:
                write(f"{style_str}{random.choice(glitch)}{RESET}")
            time.sleep(delay)
            if text_cycle:
                write(f"{_cursor_left()}{style_str}{next(text_cycle)}{ch}{RESET}")
            else:
                write(f"{_cursor_left()}{style_str}{ch}{RESET}")
            time.sleep(delay)

        for _ in text:
            write(_clear_line(1))
            time.sleep(delay)
    print()
    return len(text)


def GradientWriter(
    text: str = TEXT,
    start_hex: str = START_HEX,
    end_hex: str = END_HEX,
    delay: float = DELAY,
    position: Position = "left",
) -> int:
    """
    Types text with a smooth color gradient from start to end color.

    Each character is interpolated between the start and end hex colors,
    producing a seamless gradient transition across the text.

    Parameters
    ----------
    text : str, optional
        The text to write. Defaults to TEXT.
    start_hex : str, optional
        The starting HEX color. Defaults to START_HEX.
    end_hex : str, optional
        The ending HEX color. Defaults to END_HEX.
    delay : float, optional
        The delay between characters. Defaults to DELAY.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters written.

    Examples
    --------
    >>> GradientWriter("Gradient", start_hex="#FF0000", end_hex="#0000FF", delay=0.01)
    8
    """
    colored_text = gradient(text=text, start_hex=start_hex, end_hex=end_hex)
    prefix = _position_prefix(len(text), position)
    if prefix:
        write(prefix)
    
    # This is a workaround to print character by character with delay.
    # It splits the string by the escape character to handle multi-byte characters and color codes.
    parts = colored_text.split('[')
    
    # The first part might be empty or a character, print it
    if parts[0]:
        write(parts[0])
        time.sleep(delay)

    # Print the rest of the parts, re-adding the escape character
    for part in parts[1:]:
        # Find the end of the color code
        m_pos = part.find('m')
        if m_pos != -1:
            # We have a color code and a character
            color_code = '[' + part[:m_pos+1]
            char = part[m_pos+1:]
            if char:
                write(color_code + char)
                time.sleep(delay)
        else:
            # Should not happen with the gradient function, but as a fallback
            write('[' + part)
            time.sleep(delay)

    if not text.endswith("\n"):
        print()
    return len(text)


def AutoCompleteWriter(
    text: str = TEXT,
    delay: float = DELAY,
    suggestion_style: tuple = (),
    color=None,
    style: tuple = (),
    reverse: bool = False,
    position: Position = "left",
) -> int:
    """
    Types text with an inline autocomplete/ghost-text effect.

    As each character is typed, the remaining portion of the text is shown
    as a dimmed "ghost" suggestion ahead of the cursor. The next character
    is then typed in the primary style, and the ghost suggestion shrinks
    — mimicking IDE autocomplete behaviour.

    Parameters
    ----------
    text : str, optional
        The full text to type. Defaults to TEXT.
    delay : float, optional
        Delay in seconds between characters. Defaults to DELAY.
    suggestion_style : tuple, optional
        Tuple of ANSI style constants for the ghost suggestion
        (e.g. (DIM,) or (GRAY,)). Defaults to ().
    color : str, list, or None, optional
        Color specification for the typed text. Defaults to HEX_COLORS when None.
    style : tuple, optional
        Tuple of ANSI style constants for typed text. Defaults to ().
    reverse : bool, optional
        If True, types text in reverse order. Defaults to False.
    position : str, optional
        Text alignment: "left", "right", "top", "bottom". Defaults to "left".

    Returns
    -------
    int
        The number of characters processed.

    Examples
    --------
    >>> AutoCompleteWriter("Hello!", delay=0.05)
    6
    """
    colors = _resolve_to_ansi_list(color if color is not None else HEX_COLORS)
    style_str = _make_style(*style)
    ghost_style = _make_style(*suggestion_style)
    prefix = _position_prefix(len(text), position)
    raw = reversed(text) if reverse else text
    chars = list(raw)

    if prefix:
        write(prefix)

    color_cycle = itertools.cycle(colors) if colors else None

    for i, ch in enumerate(chars):
        if color_cycle:
            write(f"{style_str}{next(color_cycle)}{ch}{RESET}")
        else:
            write(f"{style_str}{ch}{RESET}")
        remaining = chars[i + 1:]
        if remaining:
            ghost = "".join(remaining)
            if ghost_style:
                write(f"{ghost_style}{ghost}{RESET}")
                time.sleep(delay)
                write(_clear_line(len(ghost)))
            else:
                time.sleep(delay)
        else:
            time.sleep(delay)
    print()
    return len(text)
