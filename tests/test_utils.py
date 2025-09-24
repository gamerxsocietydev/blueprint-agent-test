"""Tests for utils module."""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import greet, calculate_sum


def test_greet():
    """Test the greet function."""
    assert greet("World") == "Hello, World!"
    assert greet("Blueprint") == "Hello, Blueprint!"


def test_calculate_sum():
    """Test the calculate_sum function."""
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(0, 0) == 0


if __name__ == "__main__":
    test_greet()
    test_calculate_sum()
    print("All tests passed!")
