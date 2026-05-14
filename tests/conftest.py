import re
from unittest.mock import patch

import pytest


def strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*[a-zA-Z]", "", text)


@pytest.fixture
def mock_sleep():
    with patch("time.sleep") as mock:
        yield mock


@pytest.fixture
def mock_winsound():
    with patch("winsound.Beep") as mock:
        yield mock


@pytest.fixture
def mock_random():
    with patch("random.choice", return_value="X") as mock:
        yield mock
