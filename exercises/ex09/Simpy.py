"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730477803"


class Simpy:
    """A class of a list of float values."""
    values: list[float]

    def __init__(self, init_list: list[float]):
        """Initalizes Simpy class with values list given."""
        self.values = init_list

    def __str__(self) -> str:
        """Returns a str representation of a Simpy Class."""
        return f"Simpy({self.values})"
    
    def fill(self, num: float, n: int) -> None:
        """Fills the values attribute of a Simpy class with a given number "n" number of times."""
        self.values: list[float] = []
        for i in range(0, n):
            self.values.append(num)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a list of values from a range of stop to start with step interval in between."""
        self.values: list[float] = []
        assert step != 0.0
        i: int = 0
        while start != stop:
            self.values.append(start + i * step)
            start += step
    
    def sum(self) -> float: 
        """Returns the sum of Simpy.values."""
        return sum(self.values)
    
    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds two Simpy classes or Simpy class and a float together."""
        new_values: list[float] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                new_num: float = self.values[i] + rhs.values[i]
                new_values.append(new_num)
                i += 1
            return Simpy(new_values)
        if isinstance(rhs, float):
            for item in self.values:
                new_value = item = item + rhs
                new_values.append(new_value)
            return Simpy(new_values)
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Puts a Simpy class to another Simpy class power, or a Simpy to another float power."""
        new_values: list[float] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            while i < len(self.values):
                new_num: float = self.values[i] ** rhs.values[i]
                new_values.append(new_num)
                i += 1
            return Simpy(new_values)
        if isinstance(rhs, float):
            for item in self.values:
                new_value = item = item ** rhs
                new_values.append(new_value)
            return Simpy(new_values)
    
    def __eq__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Creates a list of bools whether the lhs Simpy is equal to rhs Simpy or float at given indicies."""
        bool_list: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in self.values:
                if self.values[i] == rhs.values[i]:
                    bool_list.append(True)
                else: 
                    bool_list.append(False)
                i += 1
            return bool_list
        if isinstance(rhs, float):
            for item in self.values:
                if item == rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
    
    def __gt__(self, rhs: Union[Simpy, float]) -> list[bool]:
        """Creates a list of bools whether the lhs Simpy is greater than to rhs Simpy or float at given indicies."""
        bool_list: list[bool] = []
        i: int = 0
        if isinstance(rhs, Simpy):
            assert len(self.values) == len(rhs.values)
            for item in self.values:
                if self.values[i] > rhs.values[i]:
                    bool_list.append(True)
                else: 
                    bool_list.append(False)
                i += 1
            return bool_list
        if isinstance(rhs, float):
            for item in self.values:
                if item > rhs:
                    bool_list.append(True)
                else:
                    bool_list.append(False)
            return bool_list
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Gets the item from a Simpy class with subscription notation of either a mask of bools, or an int."""
        new_values: list[float] = []
        if isinstance(rhs, list):
            i: int = 0
            for item in rhs:
                if item:
                    new_values.append(self.values[i])
                i += 1
            return Simpy(new_values)
        if isinstance(rhs, int):
            return self.values[rhs]