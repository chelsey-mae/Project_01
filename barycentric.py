import numpy as np
# import matplotlib_inline
def get_barycentric_coordinates():
    pass
def get_cartesian_coordinates():
    pass
import numpy as np
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




