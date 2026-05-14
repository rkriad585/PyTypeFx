import argparse

from typefx.writers import (
    RainbowWriter,
    RandomWriter,
    SoundWriter,
    TypeWriter,
)


def main():
    """
    Command-line interface entry point for TypeFx.

    Provides terminal access to TypeWriter, RainbowWriter, SoundWriter,
    and RandomWriter with configurable text, delay, loops, and effects.

    Usage
    -----
    python -m typefx --text "Hello" --delay 0.05 --rainbow
    python -m typefx --file readme.txt --sound --loops 2

    Parameters
    ----------
    None (parses sys.argv via argparse).

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser(description="TypeFx CLI")
    parser.add_argument(
        "-t", "--text", type=str, default="Hello, World!", help="Text to type"
    )
    parser.add_argument(
        "-d", "--delay", type=float, default=0.05, help="Delay between characters"
    )
    parser.add_argument("-l", "--loops", type=int, default=3, help="Number of loops")
    parser.add_argument("-r", "--rainbow", action="store_true", help="Rainbow effect")
    parser.add_argument("-rnd", "--random", action="store_true", help="Random effect")
    parser.add_argument("-s", "--sound", action="store_true", help="Sound effect")
    parser.add_argument("-f", "--file", type=str, help="File to read text from")
    args = parser.parse_args()

    text = args.text
    if args.file:
        try:
            with open(args.file, "r") as f:
                text = f.read()
        except FileNotFoundError:
            print(f"Error: File '{args.file}' not found.")
            return
        except IOError as e:
            print(f"Error reading file '{args.file}': {e}")
            return

    writer = TypeWriter
    kwargs: dict = {"delay": args.delay}
    if args.rainbow:
        writer = RainbowWriter
    elif args.sound:
        writer = SoundWriter
    elif args.random:
        writer = RandomWriter

    for _ in range(max(1, args.loops)):
        writer(text, **kwargs)


if __name__ == "__main__":
    main()
