#!/usr/bin/env python3
#----------------------------------------------------------------------------
# Created By  : Florian Eschenmoser
# Created Date: 06.2022
# ---------------------------------------------------------------------------
"""
Boids

This script creates and visualizes boids. Boids are interacting objects that
exhibit swarm-like behavior which emerges from three simple rules:
(1) Separation
(2) Alignment
(3) Cohesion
"""

# Imports
import argparse

import moderngl
import imgui
# from ... import ...



def parse_cmd_arguments(default=False, argv=None):
    """Parse command-line arguments.

    Args:
        default (bool, optional): If True, command-line arguments will be
            ignored and only the default values will be parsed.
        argv (list, optional): If provided, it will be treated as a list of
            command- line argument that is passed to the parser in place of
            :code: sys.argv.

    Returns:
        (argparse.Namespace): The Namespace object containing argument names and
            values.
    """
    return args



def run(visualize=True):
    """Runs the script.

    The :mod:`main.run` method performs the following actions:

    - Parses command-line arguments
    - Creates boids
    - iteratively computes boid positions
    - iteratively visualizes boids

    Args:
        visualize (boolean): Whether to create a visualization.
    """

    script_start = time()

    ### Parse command line arguments.
    args = parse_cmd_arguments()

    ### create a set of boids
    initializeBoids(args)

    ### initialize visualization
    initializeVisualization(args)
    # for each timestep {

    ### calculate boid positions for the next timestep
    iterateBoids(boidsData)

    ### update visualization
    iterateVisualization(boidsData)
    #}























if __name__ == '__main__':
    run()
