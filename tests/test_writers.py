from tests.conftest import strip_ansi
from typefx.writers import (
    AutoCompleteWriter,
    BounceGlitchWriter,
    BounceWriter,
    DelWriter,
    GameDialog,
    GlitchWriter,
    GradientWriter,
    HexWriter,
    HTMLWriter,
    LoopWriter,
    MarkdownWriter,
    RainbowWriter,
    RandomWriter,
    ReverseGlitchWriter,
    ReverseWriter,
    SoundWriter,
    ThinkWriter,
    TypeWriter,
)


def test_typewriter_basic(capsys, mock_sleep):
    result = TypeWriter("Hi", delay=0.001)
    assert result == 2
    out, _ = capsys.readouterr()
    assert "Hi" in strip_ansi(out)


def test_typewriter_return_count(capsys, mock_sleep):
    result = TypeWriter("Hello", delay=0.001)
    assert result == 5


def test_rainbow_writer(capsys, mock_sleep):
    result = RainbowWriter("Test", delay=0.001)
    assert result == 4
    out, _ = capsys.readouterr()
    assert "Test" in strip_ansi(out)


def test_hex_writer(capsys, mock_sleep):
    result = HexWriter("Hex", delay=0.001)
    assert result == 3


def test_del_writer(capsys, mock_sleep):
    result = DelWriter("AB", delay=0.001, hold=0.001)
    assert result == 2


def test_loop_writer(capsys, mock_sleep):
    result = LoopWriter("X", loops=2, delay=0.001)
    assert result == 1


def test_sound_writer(capsys, mock_sleep):
    result = SoundWriter("Beep", delay=0.001, sound=False)
    assert result == 4


def test_random_writer(capsys, mock_sleep):
    result = RandomWriter("Hi.", delay=0.001)
    assert result == 3


def test_markdown_writer(capsys, mock_sleep):
    result = MarkdownWriter("**bold** text", delay=0.001)
    assert result > 0


def test_html_writer(capsys, mock_sleep):
    result = HTMLWriter("<p>Hello</p>", delay=0.001)
    assert result > 0
    out, _ = capsys.readouterr()
    assert "Hello" in strip_ansi(out)


def test_glitch_writer(capsys, mock_sleep):
    result = GlitchWriter("Hi", delay=0.001)
    assert result == 2


def test_think_writer(capsys, mock_sleep):
    result = ThinkWriter("Loading", dots=1, loop=1, delay=0.001)
    assert result == 7


def test_reverse_writer(capsys, mock_sleep):
    result = ReverseWriter("olleh", delay=0.001)
    assert result == 5


def test_reverse_glitch_writer(capsys, mock_sleep):
    result = ReverseGlitchWriter("ABC", delay=0.001)
    assert result == 3


def test_bounce_writer(capsys, mock_sleep):
    result = BounceWriter("AB", delay=0.001, loop=1)
    assert result == 2


def test_bounce_glitch_writer(capsys, mock_sleep):
    result = BounceGlitchWriter("AB", delay=0.001, loop=1)
    assert result == 2


def test_gradient_writer(capsys, mock_sleep):
    result = GradientWriter("Hi", delay=0.001)
    assert result == 2


def test_game_dialog(capsys, mock_sleep):
    result = GameDialog("Hero", "Hello", delay=0.001, sound=False)
    assert result == 5
    out, _ = capsys.readouterr()
    cleaned = strip_ansi(out)
    assert "Hero" in cleaned
    assert "Hello" in cleaned


def test_typewriter_default_text(capsys, mock_sleep):
    result = TypeWriter(delay=0.001)
    assert result > 0


def test_non_tty_writer_does_not_crash(capsys, mock_sleep):
    result = TypeWriter("Safe", delay=0.001)
    assert result == 4


def test_gradient_writer_returns_int(capsys, mock_sleep):
    result = GradientWriter("X", delay=0.001)
    assert isinstance(result, int)
    assert result == 1


def test_typewriter_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = TypeWriter("Hi", delay=0.001, style=(BOLD,))
    assert result == 2
    out, _ = capsys.readouterr()
    assert "\033[1m" in out


def test_typewriter_reverse(capsys, mock_sleep):
    result = TypeWriter("ABC", delay=0.001, reverse=True)
    assert result == 3
    out, _ = capsys.readouterr()
    cleaned = strip_ansi(out).strip()
    assert cleaned == "CBA"


def test_typewriter_color_named(capsys, mock_sleep):
    from typefx.colors import RED
    result = TypeWriter("X", delay=0.001, color=RED)
    assert result == 1
    out, _ = capsys.readouterr()
    assert "\033[31m" in out


def test_typewriter_color_hex(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, color="#FF0000")
    assert result == 1
    out, _ = capsys.readouterr()
    assert "38;2;255;0;0" in out


def test_typewriter_color_palette(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, color="NEON")
    assert result == 1
    out, _ = capsys.readouterr()


def test_typewriter_color_rainbow(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, color="rainbow")
    assert result == 1
    out, _ = capsys.readouterr()


def test_typewriter_color_random(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, color="random")
    assert result == 1
    out, _ = capsys.readouterr()


def test_typewriter_color_list(capsys, mock_sleep):
    result = TypeWriter("XY", delay=0.001, color=["#FF0000", "#00FF00"])
    assert result == 2
    out, _ = capsys.readouterr()


def test_del_writer_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = DelWriter("AB", delay=0.001, hold=0.001, style=(BOLD,))
    assert result == 2
    out, _ = capsys.readouterr()
    assert "\033[1m" in out


def test_del_writer_reverse(capsys, mock_sleep):
    result = DelWriter("ABC", delay=0.001, hold=0.001, reverse=True)
    assert result == 3


def test_loop_writer_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = LoopWriter("X", loops=1, delay=0.001, style=(BOLD,))
    assert result == 1


def test_markdown_writer_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = MarkdownWriter("**bold**", delay=0.001, style=(BOLD,))
    assert result > 0


def test_html_writer_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = HTMLWriter("<p>text</p>", delay=0.001, style=(BOLD,))
    assert result > 0
    out, _ = capsys.readouterr()
    assert "\033[1m" in out


def test_sound_writer_reverse(capsys, mock_sleep):
    result = SoundWriter("ABC", delay=0.001, sound=False, reverse=True)
    assert result == 3


def test_think_writer_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = ThinkWriter("Loading", dots=1, loop=1, delay=0.001, style=(BOLD,))
    assert result == 7
    out, _ = capsys.readouterr()
    assert "\033[1m" in out


def test_game_dialog_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = GameDialog("Hero", "Hi", delay=0.001, sound=False, style=(BOLD,))
    assert result == 2
    out, _ = capsys.readouterr()
    assert "\033[1m" in out


def test_game_dialog_sound_style(capsys, mock_sleep):
    from typefx.colors import BOLD
    result = GameDialog("Hero", "Hi", delay=0.001, sound=True, style=(BOLD,))
    assert result == 2


def test_glitch_writer_style(capsys, mock_sleep, mock_random):
    from typefx.colors import BOLD
    result = GlitchWriter("Hi", delay=0.001, style=(BOLD,))
    assert result == 2
    out, _ = capsys.readouterr()
    assert "\033[1m" in out


def test_color_none_fallback(capsys, mock_sleep):
    result = TypeWriter("Hi", delay=0.001, color=None)
    assert result == 2
    out, _ = capsys.readouterr()
    assert "Hi" in strip_ansi(out)


def test_position_right(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, position="right")
    assert result == 1


def test_position_top(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, position="top")
    assert result == 1
    out, _ = capsys.readouterr()
    assert "\033[H" in out


def test_position_bottom(capsys, mock_sleep):
    result = TypeWriter("X", delay=0.001, position="bottom")
    assert result == 1


def test_rainbow_writer_position(capsys, mock_sleep):
    result = RainbowWriter("Test", delay=0.001, position="right")
    assert result == 4


def test_hex_writer_position(capsys, mock_sleep):
    result = HexWriter("Hex", delay=0.001, position="top")
    assert result == 3


def test_del_writer_position(capsys, mock_sleep):
    result = DelWriter("AB", delay=0.001, hold=0.001, position="right")
    assert result == 2


def test_loop_writer_position(capsys, mock_sleep):
    result = LoopWriter("X", loops=1, delay=0.001, position="top")
    assert result == 1


def test_sound_writer_position(capsys, mock_sleep):
    result = SoundWriter("X", delay=0.001, sound=False, position="right")
    assert result == 1


def test_game_dialog_position(capsys, mock_sleep):
    result = GameDialog("Hero", "Hi", delay=0.001, sound=False, position="top")
    assert result == 2


def test_random_writer_position(capsys, mock_sleep):
    result = RandomWriter("Hi.", delay=0.001, position="right")
    assert result == 3


def test_markdown_writer_position(capsys, mock_sleep):
    result = MarkdownWriter("**bold**", delay=0.001, position="top")
    assert result > 0


def test_html_writer_position(capsys, mock_sleep):
    result = HTMLWriter("<p>text</p>", delay=0.001, position="bottom")
    assert result > 0


def test_glitch_writer_position(capsys, mock_sleep, mock_random):
    result = GlitchWriter("Hi", delay=0.001, position="right")
    assert result == 2


def test_think_writer_position(capsys, mock_sleep):
    result = ThinkWriter("Loading", dots=1, loop=1, delay=0.001, position="top")
    assert result == 7


def test_reverse_writer_position(capsys, mock_sleep):
    result = ReverseWriter("olleh", delay=0.001, position="right")
    assert result == 5


def test_reverse_glitch_writer_position(capsys, mock_sleep):
    result = ReverseGlitchWriter("ABC", delay=0.001, position="bottom")
    assert result == 3


def test_bounce_writer_position(capsys, mock_sleep):
    result = BounceWriter("AB", delay=0.001, loop=1, position="right")
    assert result == 2


def test_bounce_glitch_writer_position(capsys, mock_sleep):
    result = BounceGlitchWriter("AB", delay=0.001, loop=1, position="top")
    assert result == 2


def test_gradient_writer_position(capsys, mock_sleep):
    result = GradientWriter("Hi", delay=0.001, position="right")
    assert result == 2


def test_auto_complete_writer_basic(capsys, mock_sleep):
    result = AutoCompleteWriter("Hi", delay=0.001)
    assert result == 2
    out, _ = capsys.readouterr()
    assert "Hi" in strip_ansi(out)


def test_auto_complete_writer_reverse(capsys, mock_sleep):
    result = AutoCompleteWriter("ABC", delay=0.001, reverse=True)
    assert result == 3


def test_auto_complete_writer_suggestion_style(capsys, mock_sleep):
    result = AutoCompleteWriter("Hi", delay=0.001, suggestion_style=("\033[2m",))
    assert result == 2
    out, _ = capsys.readouterr()
    assert "\033[2m" in out


def test_auto_complete_writer_position(capsys, mock_sleep):
    result = AutoCompleteWriter("Hi", delay=0.001, position="right")
    assert result == 2
