import functools
import io
import sys
import time

from typefx._types import Speed
from typefx.utility import _make_color, _make_delay, _type_out_text


def typefx(hex_colors=None, delay: float = 0.05, loop: int = 1, speed: Speed = "normal"):
    """
    Decorator that applies a typewriter effect to a function's output.

    Captures both ``print()`` output and return values from the decorated
    function, then replays them character-by-character with configurable
    delay, color, and speed options.

    Parameters
    ----------
    hex_colors : str, list, or None, optional
        Color specification: hex string, list of hex strings, or palette
        name ("rainbow", "random"). Defaults to None.
    delay : float, optional
        Base delay between characters in seconds. Defaults to 0.05.
    loop : int, optional
        Number of times to repeat the animation. Defaults to 1.
    speed : str, optional
        Typing speed modifier. One of "fast", "slow", "normal",
        "random", or "none". Defaults to "normal".

    Returns
    -------
    function
        A decorator that wraps the original function.

    Examples
    --------
    >>> @typefx(hex_colors=["#FF0000", "#00FF00"], delay=0.05, loop=1, speed="fast")
    ... def greet():
    ...     print("Hello!")
    >>> greet()
    >>> @typefx(hex_colors="rainbow", delay=0.03)
    ... def message() -> str:
    ...     return "Hello!"
    >>> print(message())
    """
    delay_fn = _make_delay(delay, speed)
    color_fn = _make_color(hex_colors)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            real_stdout = sys.stdout
            buf = io.StringIO()
            sys.stdout = buf
            try:
                result = func(*args, **kwargs)
            finally:
                sys.stdout = real_stdout
            if isinstance(result, str) and result:
                text_type = result
            else:
                printed = buf.getvalue()
                if printed:
                    text_type = printed
                elif result is None:
                    text_type = str(result)
                else:
                    text_type = ""
            if not text_type:
                return result

            loops = max(1, int(loop))
            for i in range(loops):
                _type_out_text(text_type, delay_fn, color_fn)
                if i < loops - 1:
                    time.sleep(0.02)
            return result

        return wrapper

    return decorator