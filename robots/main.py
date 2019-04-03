# -*- coding: utf-8 -*-
"""Entry point into application.
"""

import click

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
    click.echo("Hello, World!")


if __name__ == '__main__':
    explore()
