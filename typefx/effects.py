import os
import sys
import threading
import time

from typefx.constant import CURSOR, DELAY, DURATION


def BlinkEffect(
    duration: float = DURATION, cursor: str = CURSOR, delay: float = DELAY
) -> None:
    """
    Displays a blinking cursor effect in the console.

    Alternates between showing and hiding the cursor character at the
    current terminal position for a specified duration.

    Parameters
    ----------
    duration : float, optional
        Total time in seconds for the effect. Defaults to DURATION.
    cursor : str, optional
        Character to use as the cursor. Defaults to CURSOR.
    delay : float, optional
        Delay between blink states in seconds. Defaults to DELAY.

    Returns
    -------
    None

    Examples
    --------
    >>> BlinkEffect(duration=1, cursor="|", delay=0.2)
    """
    end: float = time.time() + duration
    while time.time() < end:
        sys.stdout.write(cursor)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(delay)


def SoundEffect(frequency: int, duration: int) -> None:
    """
    Plays an asynchronous sound effect.

    On Windows uses ``winsound.Beep`` via a daemon thread (non-blocking).
    On other systems outputs the terminal bell character.

    Parameters
    ----------
    frequency : int
        Frequency of the beep in Hertz (Windows only).
    duration : int
        Duration of the beep in milliseconds (Windows only).

    Returns
    -------
    None

    Notes
    -----
    Cross-platform sound support beyond Windows is not yet implemented.
    Linux/macOS currently use only the terminal bell character.

    Examples
    --------
    >>> SoundEffect(frequency=800, duration=100)
    """
    if os.name == "nt":
        import winsound

        threading.Thread(
            target=winsound.Beep, args=(frequency, duration), daemon=True
        ).start()
    else:
        sys.stdout.write("")
        sys.stdout.flush()