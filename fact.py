#!/usr/bin/python3
""" Factorial function """
import pytest


def factorialize(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * (factorialize(num - 1))


# Tests
def test_answer():
    assert factorialize(1) == 1
    assert factorialize(5) == 120
    assert factorialize(4) == 24
    assert factorialize(3) == 6
    assert factorialize(2) == 2
    assert factorialize(0) == 1
    assert factorialize(10) == 3628800
