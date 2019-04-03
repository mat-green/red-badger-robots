# -*- coding: utf-8 -*-
"""Module responsible for robot data.
"""

class Robot(object):
    """Represents the robot."""

    def __init__(self, x, y, direction):
        """Robot constructor.

        Parameters
        ----------
        x: int
            The x coordinate of the robot on the grid.
        y: int
            The y coordinate of the robot on the grid.
        direction: str
            The direction the robbot is facing, N or E or S or W.
        """
        self.x = x
        self.y = y
        self.direction = direction
