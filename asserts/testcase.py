# pylint: disable=missing-module-docstring
from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class Case:  # pylint: disable=missing-class-docstring
    test_data: Any
    test_output: Any
    test_function: Optional[Any] = None
