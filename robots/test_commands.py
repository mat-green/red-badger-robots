# -*- coding: utf-8 -*-

import pytest

from commands import Left, Right, Forward, NORTH, EAST, SOUTH, WEST, LOST
from grid import Grid
from robot import Robot

@pytest.fixture
def grid():
    return Grid(width=5, height=3)

@pytest.fixture
def robot():
    return Robot(x=0, y=0, direction=NORTH)

@pytest.fixture
def lost_robot():
    robot = Robot(x=0, y=0, direction=NORTH)
    robot.lost = True
    return robot


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


def test_left_command_for_lost(grid, lost_robot):
    command = Left(grid=grid, robot=lost_robot)
    command.execute()
    assert lost_robot.x == 0
    assert lost_robot.y == 0
    assert lost_robot.direction == NORTH


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


def test_right_command_for_lost(grid, lost_robot):
    command = Right(grid=grid, robot=lost_robot)
    command.execute()
    assert lost_robot.x == 0
    assert lost_robot.y == 0
    assert lost_robot.direction == NORTH


def test_forward_command(grid, robot):
    """Checks the forward command moves correctly."""

    command = Forward(grid=grid, robot=robot)
    command.execute()
    assert robot.x == 0
    assert robot.y == 1
    assert robot.direction == NORTH
    right_command = Right(grid=grid, robot=robot)
    right_command.execute()
    command.execute()
    assert robot.x == 1
    assert robot.y == 1
    assert robot.direction == EAST
    right_command.execute()
    command.execute()
    assert robot.x == 1
    assert robot.y == 0
    assert robot.direction == SOUTH
    right_command.execute()
    command.execute()
    assert robot.x == 0
    assert robot.y == 0
    assert robot.direction == WEST
