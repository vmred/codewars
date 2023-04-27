from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class TestCase:
    test_data: Any
    test_output: Any
    test_function: Optional[Any] = None
