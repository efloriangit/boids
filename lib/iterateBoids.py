    """Iterates boids for one new timestep.

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
