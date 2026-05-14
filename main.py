from time import sleep

from typefx.colors import (
    AMBER,
    AQUA,
    BIM,
    BOLD,
    BRIGHT_CYAN,
    BRIGHT_GREEN,
    BRIGHT_MAGENTA,
    BRIGHT_RED,
    BRIGHT_WHITE,
    BRIGHT_YELLOW,
    CERULEAN,
    CORAL,
    CRIMSON,
    CYAN,
    GREEN,
    LILAC,
    MINT,
    OVERLINE,
    PINK,
    PLUM,
    PURPLE,
    RESET,
    SLATE,
    TOMATO,
    UNDERLINE,
    colorize,
)
from typefx.styles import (
    ACCENT,
    BANNER,
    CAPTION,
    CODE,
    CRITICAL,
    DANGER,
    DEBUG,
    DIM,
    EMPHASIS,
    ERROR,
    GHOST,
    HEADING,
    HIGHLIGHT,
    HINT,
    IMPORTANT,
    INFO,
    KEYWORD,
    LABEL,
    LINK,
    LOG,
    META,
    MUTED,
    NEON,
    NOTE,
    PRIMARY,
    PUNCH,
    QUOTE,
    SECONDARY,
    STRIKETHROUGH,
    SUBHEADING,
    SUCCESS,
    TAG,
    TIP,
    TITLE,
    TRACE,
    VERBOSE,
    WARNING,
    apply_style,
)
from typefx.writers import GradientWriter, RainbowWriter, TypeWriter


def demo_colors():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ New Colors ━━━{RESET}")
    for name, code in [
        ("AMBER", AMBER),
        ("CERULEAN", CERULEAN),
        ("CORAL", CORAL),
        ("CRIMSON", CRIMSON),
        ("LILAC", LILAC),
        ("MINT", MINT),
        ("PINK", PINK),
        ("PLUM", PLUM),
        ("PURPLE", PURPLE),
        ("SLATE", SLATE),
        ("TOMATO", TOMATO),
    ]:
        sample = colorize(f" {name:12}", code, BOLD)
        print(f"  {sample}")


def demo_styles():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Style Presets ━━━{RESET}")
    styles = [
        ("ERROR", ERROR),
        ("SUCCESS", SUCCESS),
        ("WARNING", WARNING),
        ("INFO", INFO),
        ("TIP", TIP),
        ("HINT", HINT),
        ("DANGER", DANGER),
        ("CRITICAL", CRITICAL),
        ("IMPORTANT", IMPORTANT),
        ("NOTE", NOTE),
        ("DEBUG", DEBUG),
        ("TRACE", TRACE),
        ("LOG", LOG),
        ("VERBOSE", VERBOSE),
        ("PRIMARY", PRIMARY),
        ("SECONDARY", SECONDARY),
        ("ACCENT", ACCENT),
        ("MUTED", MUTED),
        ("GHOST", GHOST),
        ("DIM", DIM),
        ("PUNCH", PUNCH),
        ("EMPHASIS", EMPHASIS),
        ("BANNER", BANNER),
        ("TITLE", TITLE),
        ("HEADING", HEADING),
        ("SUBHEADING", SUBHEADING),
        ("CODE", CODE),
        ("KEYWORD", KEYWORD),
        ("LINK", LINK),
        ("QUOTE", QUOTE),
        ("CAPTION", CAPTION),
        ("LABEL", LABEL),
        ("TAG", TAG),
        ("HIGHLIGHT", HIGHLIGHT),
        ("STRIKETHROUGH", STRIKETHROUGH),
        ("NEON", NEON),
        ("META", META),
    ]
    for name, style in styles:
        print(f"  {apply_style(f'{name:18}', style)}")


def demo_writers():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Writers ━━━{RESET}")
    TypeWriter("TypeWriter", delay=0.02, **SUCCESS)
    sleep(0.1)
    RainbowWriter("RainbowWriter", delay=0.02)
    sleep(0.1)
    GradientWriter(
        "GradientWriter",
        delay=0.02,
        start_color=BRIGHT_CYAN,
        end_color=BRIGHT_MAGENTA,
    )


def demo_apply_style():
    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ apply_style ━━━{RESET}")
    styled = apply_style("Bold & Underlined", {"style": (BOLD, UNDERLINE)})
    aqua = apply_style("Aqua text", {"color": AQUA})
    combo = apply_style("Custom Combo", {"color": BRIGHT_YELLOW, "style": (BOLD, OVERLINE)})
    print(f"  {styled}")
    print(f"  {aqua}")
    print(f"  {combo}")


def main():
    print(f"{BOLD}{BRIGHT_CYAN}{OVERLINE}  PyTypeFx Demo  {RESET}")
    print(f"  {colorize('New colors & style presets', BRIGHT_GREEN, BIM)}")

    demo_colors()
    demo_styles()
    demo_writers()
    demo_apply_style()

    print(f"\n{BOLD}{BRIGHT_WHITE}━━━ Done ━━━{RESET}\n")


if __name__ == "__main__":
    main()
