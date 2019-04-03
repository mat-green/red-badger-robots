# -*- coding: utf-8 -*-

import pytest

from commands import EAST
from grid import Grid
from robot import Robot


def test_with_no_scents():
    grid = Grid(width=5, height=3)
    assert grid.check_for_scent(x=2, y=2) == False


def test_with_scents():
    grid = Grid(width=5, height=3)
    grid.scents = [(2, 2)]
    assert grid.check_for_scent(x=2, y=2) == True


def test_not_lost_robot():
    grid = Grid(width=5, height=3)
    assert grid.check_for_lost_robot(x=0, y=0) == False


def test_lost_robot_on_x():
    grid = Grid(width=5, height=3)
    assert grid.check_for_lost_robot(x=6, y=0) == True


def test_lost_robot_on_y():
    grid = Grid(width=5, height=3)
    assert grid.check_for_lost_robot(x=0, y=4) == True


def test_lost_robot_on_x_y():
    grid = Grid(width=5, height=3)
    assert grid.check_for_lost_robot(x=6, y=4) == True
