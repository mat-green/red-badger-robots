# -*- coding: utf-8 -*-

import pytest

from commands import Left, Right, Forward, NORTH, EAST, SOUTH, WEST
from grid import Grid
from robot import Robot

@pytest.fixture
def grid():
    return Grid(width=5, height=3)

@pytest.fixture
def robot():
    return Robot(x=0, y=0, direction=NORTH)

def test_left_command(grid, robot):
    """Checks the left command rotates correctly."""

    command = Left(grid=grid, robot=robot)
    command.execute()
    assert robot.x == 0
    assert robot.y == 0
    assert robot.direction == WEST
    command.execute()
    assert robot.direction == SOUTH
    command.execute()
    assert robot.direction == EAST
    command.execute()
    assert robot.direction == NORTH

def test_right_command(grid, robot):
    """Checks the right command rotates correctly."""

    command = Right(grid=grid, robot=robot)
    command.execute()
    assert robot.x == 0
    assert robot.y == 0
    assert robot.direction == EAST
    command.execute()
    assert robot.direction == SOUTH
    command.execute()
    assert robot.direction == WEST
    command.execute()
    assert robot.direction == NORTH
