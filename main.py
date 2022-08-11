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
# import argparse



from lib.BoidsClass import boid

import pygame
import argparse


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



    parser = argparse.ArgumentParser(description='boids simulation', \
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ggroup = parser.add_argument_group('General settings')
    ggroup.add_argument('--windowWidth', type = float, default = 1800,
                        help = 'Width of the pygame window in pixels')
    ggroup.add_argument('--windowHeight', type = float, default = 1200,
                        help = 'Height of the pygame window in pixels')
    ggroup.add_argument('--maxFPS', type = float, default = 60,
                        help = 'Maximum of frames per second')
    ggroup.add_argument('--nBoids', type = int, default = 80,
                        help = 'number of boids to be created')

    bgroup = parser.add_argument_group('Boid settings')
    bgroup.add_argument('--color01', type = tuple, default = (120, 120, 40),
                        help = 'color01 of the boids')
    bgroup.add_argument('--velocity', type = float, default = 6,
                        help = 'movement velocity')
    bgroup.add_argument('--separationDistance', type = float, default = 20,
                        help = 'maximum distance for the separation force to take effect')
    bgroup.add_argument('--fieldOfVisionRadius', type = float, default = 50,
                        help = 'maximum distance for all forces to take effect')
    bgroup.add_argument('--alignmentStrength', type = float, default = 1,
                        help = 'weigthing of the alignment vector')
    bgroup.add_argument('--separationStrength', type = float, default = 1.5,
                        help = 'weigthing of the separation vector')
    bgroup.add_argument('--cohesionStrength', type = float, default = 1,
                        help = 'weigthing of the cohesion vector')
    bgroup.add_argument('--weightingPreviousMovementVector', type = float, default = 0.96,
                        help = 'weighting of the previous movement vector; lower values result in more agility')



    args = parser.parse_args()

    return args



def run():
    """Runs the script.

    The :mod:`main.run` method performs the following actions:

    - Parses command-line arguments
    - Creates boids
    - iteratively computes boid positions
    - iteratively visualizes boids

    Args:
        visualize (boolean): Whether to create a visualization.
    """



    # Parse command line arguments.
    args = parse_cmd_arguments()

    # open a pygame window
    pygame.init()
    window = pygame.display.set_mode([args.windowWidth, args.windowHeight])

    clock = pygame.time.Clock()
    running = True

    # create a set of boids
    swarm = [boid(args) for i in range(args.nBoids)]

    while running:
        clock.tick(args.maxFPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # empty the screen
        window.fill((0, 0, 0))


        ### update boids
        for i in swarm:
            i.move(args, window, swarm)
            i.drawShape(args, window)

        ### flip the screen
        pygame.display.flip()


    ### close
    pygame.quit()



if __name__ == '__main__':
    run()
