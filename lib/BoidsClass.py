"""Defines the class boids.

    The :func:'iterateBoids' Takes a set of boids and updates their position
    for the next timestep.
    Note, the following functions are used:
    :func: 'initializeBoids' is used to create an initial set of boids.
    the loss.

    Args:
        args (argparse.Namespace): The command-line arguments.
        boidsData(DataFrame): Data frame containing position variables for each boid.

        - **ID**: Boid ID
        - **xCoordinate**: The boids position on the x axis
        - **yCoordinate**: The boids position on the y axis
        - **zCoordinate**: The boids position on the z
        - **direction**: The direction the boid is facing.

    Returns:
        boidsData(DataFrame): Data frame containing position variables for each boid.

    """

import pygame
import random


class boid:
    def __init__(self, args):
        self.position = pygame.math.Vector2(random.randint(0, args.windowWidth),
                        random.randint(0, args.windowHeight)) # position (x/y)
        self.color = (255, 255, 255) # color of the object
        self.size = 4 # size of the object
        self.movementVector = pygame.math.Vector2(0,0) # initial movement vector

        self.velocity = args.velocity # initial velocity of the object
        self.fieldOfVisionRadius = args.fieldOfVisionRadius # maximum distance for all forces to take effect
        self.separationDistance = args.separationDistance # maximum distance for the separation force
                                                     # to take effect

        self.alignmentStrength = args.alignmentStrength # weigthing of the alignment vector
        self.separationStrength = args.separationStrength # weigthing of the separation vector
        self.cohesionStrength = args.cohesionStrength # weighting of the cohesion vector

        self.stayWithinWindowStrength = 10 # weigthing of the stay within window vector

        self.weightingPreviousMovementVector = args.weightingPreviousMovementVector
                                            # weighting of the previous movement vector

    def move(self, args, screen, swarm):

        # find all boids within the field of vision
        neighbors = list(filter(lambda i: \
        pygame.math.Vector2(i.position - self.position).magnitude() \
            < self.fieldOfVisionRadius, swarm))

        # sum up vectors of different forces
        newMovementVector = \
            self.alignment(args, screen, neighbors) + \
            self.cohesion(args, screen, neighbors) + \
            self.separation(args, screen, neighbors) + \
            self.stayWithinWindow(args, screen)

        # take the previous movement vector
        self.movementVector = self.movementVector * self.weightingPreviousMovementVector

        # add the new movement vector
        if newMovementVector != pygame.math.Vector2(0, 0):
            self.movementVector = self.movementVector + \
                (1 - self.weightingPreviousMovementVector) * newMovementVector.normalize() * self.velocity

        # calculate the angle
        self.angle = pygame.math.Vector2(0,0).angle_to(self.movementVector)

        # calculate the new position
        self.position = self.position + self.movementVector


    def stayWithinWindow(self, args, screen):

        stayWithinWindowVector = pygame.math.Vector2(0,0)

        if self.position.x - self.fieldOfVisionRadius < 0:
            stayWithinWindowVector.x = 1

        if self.position.x + self.fieldOfVisionRadius > args.windowWidth:
            stayWithinWindowVector.x = -1

        if self.position.y - self.fieldOfVisionRadius < 0:
            stayWithinWindowVector.y = 1

        if self.position.y + self.fieldOfVisionRadius > args.windowHeight:
            stayWithinWindowVector.y = -1

        if stayWithinWindowVector != pygame.math.Vector2(0,0):
            stayWithinWindowVector = stayWithinWindowVector * self.stayWithinWindowStrength

        return stayWithinWindowVector



    def alignment(self, args, screen, neighbors):
        averageMovementVectorNeighbors = sum([i.movementVector for i in neighbors], \
        start = pygame.math.Vector2(0,0))/len(neighbors)

        alignmentVector = averageMovementVectorNeighbors
        if alignmentVector != pygame.math.Vector2(0,0):
                alignmentVector = alignmentVector.normalize() * self.alignmentStrength

        return alignmentVector



    def cohesion(self, args, screen, neighbors):

        averagePositionVectorNeighbors = sum([i.position for i in neighbors], \
            start = pygame.math.Vector2(0,0))/len(neighbors)

        cohesionVector = averagePositionVectorNeighbors - self.position
        if cohesionVector != pygame.math.Vector2(0,0):
            cohesionVector = cohesionVector.normalize() * self.cohesionStrength

        return cohesionVector



    def separation(self, args, screen, neighbors):

        allDistancesToNeighbors = [i.position - self.position for i in neighbors]

        smallDistancesToNeighbors = list(filter(lambda i: \
        i.magnitude() < self.separationDistance, allDistancesToNeighbors))

        separationVector = -sum([i for i in smallDistancesToNeighbors], \
            start = pygame.math.Vector2(0,0))

        if separationVector != pygame.math.Vector2(0,0):
            separationVector = separationVector.normalize() * self.separationStrength

        return separationVector


    def drawShape (self, args, screen):
        movementAngle = pygame.math.Vector2(0,0).angle_to(self.movementVector)
        tipOffset = pygame.math.Vector2(0.5*self.size, 0).rotate(self.angle)
        backOffset1 = pygame.math.Vector2(-2*self.size, 0.5 * self.size).rotate(self.angle)
        backOffset2 = pygame.math.Vector2(-2*self.size, -0.5 * self.size).rotate(self.angle)

        tipPosition = self.position + tipOffset
        backPosition1 = self.position + backOffset1
        backPosition2 = self.position + backOffset2

        pygame.draw.polygon(screen, color = self.color, points = [tipPosition, backPosition1, backPosition2])
        pygame.draw.circle(screen, color = (40, 120, 160), center = self.position, radius = 2)
