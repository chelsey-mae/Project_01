
import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    #Make x_vals a sorted array
    #x_vals = np.sort(x_vals)
    #Interval was given as [x_vals[0], x_vals[-1]]
    a, b = x_vals[0], x_vals[-1]
    #Find the width of each sub-interval
    n = len(x_vals) - 1
    delta_x = (b - a) / n
    # Calculate left-endpoint sum
    left_sum = np.sum(func(x_vals[n] * delta_x))
    return left_sum

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    a, b = x_vals[0], x_vals[-1]
    n = len(x_vals) - 1
    delta_x = (b - a) / n
    trapezoid_formula = (1 / 2 * delta_x) * (func(x_vals[0]) + 2 * np.sum(func(x_vals[1:n])) + func(x_vals[-1]))
    return trapezoid_formula
