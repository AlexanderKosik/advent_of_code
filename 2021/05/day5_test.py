import pytest
from day5 import valid, low_to_heigh, line, Board, get_points_from_line

def test_valid():
    p1 = (0, 0)
    p2 = (0, 5)
    assert valid(p1, p2)

    p1 = (3, 0)
    p2 = (3, 5)
    assert valid(p1, p2)

    p1 = (2, 0)
    p2 = (3, 5)
    assert valid(p1, p2) == False

def test_low_heigh():
    assert (0, 10) == low_to_heigh(0, 10)
    assert (0, 10) == low_to_heigh(10, 0)

def test_line():
    p1 = (0, 0)
    p2 = (0, 2)
    result = {(0, 0), (0, 1), (0, 2)}
    assert result == line(p1, p2)

    p1 = (4, 1)
    p2 = (0, 1)
    result = {(0, 1), (1, 1), (2, 1), (3, 1), (4, 1),}
    assert result == line(p1, p2)

def test_board():
    b = Board(10, 10)
    assert 0 == b.dangerous()

    b += ((0, 0), (0, 5))
    assert 0 == b.dangerous()

    b += ((0, 0), (0, 5))
    assert 6 == b.dangerous()

    b += ((0, 0), (2, 0))
    assert 6 == b.dangerous()

    b += ((0, 0), (2, 0))
    assert 8 == b.dangerous()

def test_input_parsing():
    line = "0,9 -> 5,9"
    assert ((0, 9), (5, 9)) == get_points_from_line(line)

    line = "2,7 -> 5,9"
    assert ((2, 7), (5, 9)) == get_points_from_line(line)
