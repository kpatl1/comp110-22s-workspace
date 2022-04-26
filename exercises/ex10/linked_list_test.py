"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last, value_at, linkify, scale, max
from typing import Optional

__author__ = "730477803"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_positive_index() -> None:
    """Should return the value of the given index in the linked list."""
    x: Optional[Node] = linkify([1, 2, 3])
    assert value_at(x, 2) == 3


def test_value_at_out_of_bound_index() -> None:
    """Should return the value of the given index in the linked list."""
    with pytest.raises(IndexError):
        x: Optional[Node] = linkify([1, 2, 3])
        value_at(x, 3)


def test_max_normal() -> None:
    """Tests to find the max value in a linked list."""
    x: Optional[Node] = linkify([1, 2, 3, 4])
    assert max(x) == 4


def test_max_none() -> None:
    """An empty list should return a ValueError when max is called."""
    with pytest.raises(ValueError):
        x: Optional[Node] = linkify([])
        max(x)


def test_max_one_value() -> None:
    """When max is called for a linked list with one data point, should return that same one data point."""
    x: Optional[Node] = linkify([2])
    assert max(x) == 2


def test_linkify_normal() -> None:
    """Should create a linked list with a given list."""
    assert print(linkify([1, 2, 3])) == print(Node(3, Node(2, Node(1, None))))


def test_linkify_empty() -> None:
    """Should return None is the input list is empty."""
    assert linkify([]) is None


def test_scale_normal() -> None:
    """Should scale all data values in a linked list by given factor."""
    assert print(scale(linkify([1, 2, 3]), 2)) == print(linkify([2, 4, 6])) 


def test_scale_none() -> None:
    """Should return None when a empty linked list is given to funtion scale."""
    assert scale(linkify([]), 2) is None