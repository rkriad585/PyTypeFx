import platform

from typefx.effects import BlinkEffect, SoundEffect


def test_blink_effect(capsys, mock_sleep):
    BlinkEffect(duration=0.001, cursor="_", delay=0.001)
    out, _ = capsys.readouterr()
    assert "_" in out


def test_sound_effect_windows(mock_sleep):
    if platform.system() == "Windows":
        SoundEffect(frequency=800, duration=30)


def test_constant_imports():
    from typefx.constant import CURSOR, DELAY, DURATION

    assert isinstance(CURSOR, str)
    assert isinstance(DELAY, float)
    assert isinstance(DURATION, float)
