# -*- coding: utf-8 -*-
"""Module responsible for grid information.
"""



class InputException(Exception):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


class Grid(object):
    """Represents the grid that the robots move around in."""

    def __init__(self, width, height):
        """Grid constructor.

        Parameters
        ----------
        width: int
            The width of the grid, max of 50.
        height: int
            The height of the grid, max of 50.
        """
        self.width = width
        self.height = height
        if self.width > 50:
            raise InputException(self.width, "Width must be less than 50")
        if self.height > 50:
            raise InputException(self.height, "Height must be less than 50")
        self.scents = []  # no scents detected.

    def check_for_scent(self, x, y):
        """Determines if a robot has already been lost at coordinates.
        Parameters
        ----------
        x: int
            The x coordinate of the grid to be checked.
        y: int
            The y coordinate of the grid to be checked.

        Returns
        -------
        bool
            True if a scent is detected, False otherwise.
        """
        if len(self.scents) == 0:
            return False
        scent_found = [tup for tup in self.scents if tup[0] == x and tup[1] == y]
        if scent_found:
            return True
        else:
            return False

    def check_for_lost_robot(self, x, y):
        """Determines if a robot is lost at coordinates.

        Will add coordinates to scents

        Parameters
        ----------
        x: int
            The x coordinate of the grid to be checked.
        y: int
            The y coordinate of the grid to be checked.

        Returns
        -------
        bool
            True if the robot is lost, False otherwise.
        """
        if x > self.width or y > self.height:
            self.scents.append((x, y))
            return True
        else:
            return False
