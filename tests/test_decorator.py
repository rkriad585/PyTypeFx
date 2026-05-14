from tests.conftest import strip_ansi
from typefx.decorator import typefx


def test_typefx_decorator_print(capsys, mock_sleep):
    @typefx(delay=0.001)
    def greet():
        print("Hello")

    result = greet()
    assert result is None
    out, _ = capsys.readouterr()
    assert "Hello" in out


def test_typefx_decorator_return(capsys, mock_sleep):
    @typefx(delay=0.001)
    def greet() -> str:
        return "Hello"

    result = greet()
    assert result == "Hello"
    out, _ = capsys.readouterr()
    assert "Hello" in out


def test_typefx_decorator_with_colors(capsys, mock_sleep):
    @typefx(hex_colors=["#FF0000"], delay=0.001)
    def greet():
        print("Red")

    greet()
    out, _ = capsys.readouterr()
    assert "Red" in strip_ansi(out)


def test_typefx_decorator_loop(capsys, mock_sleep):
    @typefx(delay=0.001, loop=2)
    def greet():
        print("Hi")

    greet()
    out, _ = capsys.readouterr()
    assert out.count("Hi") >= 1


def test_typefx_decorator_speed(capsys, mock_sleep):
    @typefx(delay=0.001, speed="fast")
    def greet():
        print("Fast")

    greet()
    out, _ = capsys.readouterr()
    assert "Fast" in out


def test_typefx_decorator_no_output(capsys, mock_sleep):
    @typefx(delay=0.001)
    def nothing():
        pass

    result = nothing()
    assert result is None
