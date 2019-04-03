# -*- coding: utf-8 -*-

import pytest

from grid import Grid


def test_with_no_scents():
    grid = Grid(width=5, height=3)
    assert grid.check_for_scent(x=2, y=2) == False


def test_with_scents():
    grid = Grid(width=5, height=3)
    grid.scents = [(2, 2)]
    assert grid.check_for_scent(x=2, y=2) == True
