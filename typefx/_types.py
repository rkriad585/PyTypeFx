import sys
from typing import List, Tuple, Union

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    try:
        from typing_extensions import Literal
    except ImportError:
        Literal = None  # type: ignore


Position = Literal["left", "right", "top", "bottom"]
Speed = Literal["fast", "slow", "normal", "random", "none"]
ColorInput = Union[str, List[str], Tuple[str, ...], None]
StyleInput = Tuple[str, ...]
