# -*- coding: utf-8 -*-
"""Module responsible for robot commands.
"""

from abc import ABC, abstractmethod


NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"


class Command(ABC):
    """Represents an abstract command."""

    def __init__(self, robot, grid):
        """Command constructor.

        Parameters
        ----------
        robot: Robot
            The instance of the robot to be commanded.
        grid: Grid
            The instance of the grid the robot is moving around.
        """
        self.robot = robot
        self.grid = grid
        self.compass = [ NORTH, EAST, SOUTH, WEST ]

    @abstractmethod
    def execute(self):
        pass


class Left(Command):
    """Represents the left rotation command."""

    def execute(self):
        current_index = [i for i,_ in enumerate(self.compass) if _ == self.robot.direction][0]
        new_index = current_index - 1
        if new_index < 0:
            new_index = len(self.compass) - 1
        self.robot.direction = self.compass[new_index]

class Right(Command):
    """Represents the right rotation command."""

    def execute(self):
        current_index = [i for i,_ in enumerate(self.compass) if _ == self.robot.direction][0]
        new_index = current_index + 1
        if new_index >= len(self.compass):
            new_index = 0
        self.robot.direction = self.compass[new_index]


class Forward(Command):
    """Represents the forward rotation command."""

    def execute(self):
        pass
