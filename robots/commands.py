# -*- coding: utf-8 -*-
"""Module responsible for robot commands.
"""

from abc import ABC, abstractmethod


NORTH = "N"
EAST = "E"
SOUTH = "S"
WEST = "W"
LOST = "LOST"


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
        if self.robot.direction != LOST:
            current_index = [i for i,_ in enumerate(self.compass) if _ == self.robot.direction][0]
            new_index = current_index - 1
            if new_index < 0:
                new_index = len(self.compass) - 1
            self.robot.direction = self.compass[new_index]

class Right(Command):
    """Represents the right rotation command."""

    def execute(self):
        if self.robot.direction != LOST:
            current_index = [i for i,_ in enumerate(self.compass) if _ == self.robot.direction][0]
            new_index = current_index + 1
            if new_index >= len(self.compass):
                new_index = 0
            self.robot.direction = self.compass[new_index]


class Forward(Command):
    """Represents the forward rotation command."""

    def execute(self):
        def move(direction):
            return {
                NORTH: (0, 1),
                EAST: (1, 0),
                SOUTH: (0, -1),
                WEST: (-1, 0),
            }.get(direction, (0, 0))
        x, y = move(self.robot.direction)
        new_x = self.robot.x + x
        new_y = self.robot.y + y
        if self.grid.check_for_scent(x=new_x, y=new_y) == False:
            self.robot.x = new_x
            self.robot.y = new_y
            if self.grid.check_for_lost_robot(self.robot):
                self.robot.direction = LOST
