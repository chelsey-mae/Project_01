import numpy as np
def get_cartesian_coordinates(triangle_coordinates, barycentric_coordinates):
    # x and y coordinates for triangle vertices
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]

    # Barycentric coordinates
    v1, v2, v3 = barycentric_coordinates

    # Calculate Cartesian coordinates (x, y)
    x = v1 * x1 + v2 * x2 + v3 * x3
    y = v1 * y1 + v2 * y2 + v3 * y3

    return np.array([x, y])