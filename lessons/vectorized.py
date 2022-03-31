from __future__ import annotations
from typing import Union


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        """Vectorize concatenation operator."""
        result: list[str] = []
        i: int = 0
        if isinstance(rhs, str):
            for item in self.items:
                result.append(item + rhs)
        else:
            # Build up the result list by concatenating
            # each item in self.items with corresponding item in rhs.items
            assert len(self.items) == len(rhs.items)
            for i in range(0, len(self.items)):
                result.append(self.items[i] + rhs.items[i])
        return StrArray(result)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + " " + last)