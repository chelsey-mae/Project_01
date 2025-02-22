
import numpy as np


def get_barycentric_coordinates(triangle_coordinates, point_coordinates):

    #extracting the x and y coordinates from the 2x3 array
    x1, x2, x3 = triangle_coordinates[0]
    y1, y2, y3 = triangle_coordinates[1]

    #extracting the cartesian coordinates as x and y
    x, y = point_coordinates

    #constructing matrix that has the x and y coordinates of the vertices
    #adding row of 1's to ensure the barycentric coordinates add up to 1, which is a rule stated above
    b = np.array([
        [x1, x2, x3],
        [y1, y2, y3],
        [1, 1, 1]
    ])

    #added 1 to vector to maintain 3x1 and consistency with b matrix
    a = np.array(
        [x, y, 1]
    )

    #calculates barycentric as 1D array
    v = np.linalg.solve(b, a)

    return v

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

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray  ):


    x, y = point_coordinates # given coordinate points

    # x and y coordinates for the triangle vertices

    x_1,x_2,x_3 = triangle_coordinates[0]
    y_1,y_2,y_3 = triangle_coordinates[1]

    # creates a system of equations

    system = np.array([[x_1,x_2,x_3],
                      [y_1,y_2,y_3],
                        [1,1,1]
                       ])

    equals = np.array([x,y,1])

    # solves for said system

    uppercase_p = np.linalg.solve(system, equals)

    # returns a bool which checks to see if the solution of the system is equal to 1 and non-negative/ is within the bounds of the triangle - True if it is, False if not

    return np.all(uppercase_p >= 0)

    #I know I could have reused barycentric for my code
    # (i.e. bary_coord = get_barycentric_coordinates(triangle_coordinates, point_coordinates), return np.all(bary_coord >= 0).
    # However, I did not know if that was allowed, so I just wrote it all out
