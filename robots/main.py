# -*- coding: utf-8 -*-
"""Entry point into application.
"""

import click
import os

from commands import Left, Right, Forward, LOST
from grid import Grid
from robot import Robot


@click.command()
@click.option("--file",
              required=True,
              help="the data file to be used to control robots")
def explore(file):
    """
    Simple program that will control the virtual robots defined in the file.

    Parameters
    ----------
    file: str
        The data file to be used to control robots.
    """
    with open(file, 'r', encoding='utf-8') as file:
        width, height = file.readline().split(' ')
        grid = Grid(width=int(width), height=int(height))
        robot_line = file.readline()
        while robot_line:
            x, y, direction = robot_line.split(' ')
            robot = Robot(x=int(x), y=int(y), direction=direction.rstrip())
            instructions = file.readline()
            for instruction in instructions.rstrip():
                command = {
                    "L": Left(robot=robot, grid=grid),
                    "R": Right(robot=robot, grid=grid),
                    "F": Forward(robot=robot, grid=grid),
                }.get(instruction)
                command.execute()
                if robot.lost:
                    break
            if robot.lost:
                print(robot.x, robot.y, robot.direction, "LOST")
            else:
                print(robot.x, robot.y, robot.direction)
            robot_line = file.readline()
            robot_line = file.readline()



if __name__ == '__main__':
    explore()
