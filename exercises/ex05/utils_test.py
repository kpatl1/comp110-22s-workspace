"""A test file to make sure utils.py functions are working."""

__author__ = "730477803"

from utils import only_evens
from utils import sub
from utils import concat


def test_evens_normal() -> None:
    """Tests an normal use case of only_evens."""
    assert only_evens([1, 2, 3]) == [2]


def test_evens_empty() -> None:
    """Tests and edge case where there is no data in the input list."""
    assert only_evens([]) == []


def test_evens_negative() -> None:
    """Tests a normal use case but with negative numbers included."""
    assert only_evens([-2, -1, 9]) == [-2]


def test_sub_normal() -> None:
    """Normal test case of sub function."""
    assert sub([123, 1245, 623423, 1245], 2, 3) == [623423]


def test_sub_whole_range() -> None: 
    """Normal test of sub function with the whole range."""
    assert sub([123, 1245, 623423, 1245], 0, 3) == [123, 1245, 623423]


def test_sub_out_of_index() -> None: 
    """Edge case test where there is are negative index values."""
    assert sub([123, 1245, 623423, 1245], -2, 3) == [123, 1245, 623423]


def test_concat_normal() -> None: 
    """Normal test case for concat function."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_other_normal() -> None:
    """Normal test case for concat function."""
    assert concat([1, 2, 3], [6]) == [1, 2, 3, 6]


def test_concat_edge() -> None:
    """Edge test case of concat with two empty strings."""
    assert concat([], []) == []