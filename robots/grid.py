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
