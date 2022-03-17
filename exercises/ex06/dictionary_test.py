"""Testing file for Dictionary.py."""

__author__ = "730477803"

import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count


def test_invert_normal() -> None:
    """Normal Test."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}
    return None


def test_invert_normalagain() -> None:
    """Normal Test."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}
    return None


def test_edge_invert() -> None:
    """Edge Test."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_fav_color_normal() -> None:
    """Normal Test."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_fav_color_normal_equal() -> None:
    """Normal Test."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Bana": "yellow"}) == "yellow"


def test_fav_color_edge() -> None:
    """Edge Test."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Bana": " "}) == "blue"


def test_count_normal() -> None:
    """Normal Test."""
    x = ["1", "2", "2", "2", "3", "4", "42", "1"]
    assert count(x) == {"1": 2, "2": 3, "3": 1, "4": 1, "42": 1}
    

def test_count_normal_again() -> None:
    """Normal Test."""
    x = ["bana", 'bana', 'bana', 'kandala']
    assert count(x) == {"bana": 3, "kandala": 1}


def test_count_normal_edge() -> None: 
    """Edge Test."""
    x = ['']
    assert count(x) == {'': 1}
