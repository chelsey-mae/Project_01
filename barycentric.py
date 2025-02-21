import numpy as np
# import matplotlib_inline
#I forgot to write in my comment, I also created the file barycentric too

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

def get_cartesian_coordinates():
    pass

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray  ):

    x, y = point_coordinates

    x_1,x_2,x_3 = triangle_coordinates[0]
    y_1,y_2,y_3 = triangle_coordinates[1]

    system = np.array([[x_1,x_2,x_3],
                      [y_1,y_2,y_3],
                        [1,1,1]
                       ])

    equals = np.array([x,y,1])

    uppercase_p = np.linalg.solve(system, equals)

    return uppercase_p[0:3] >= 0




