import numpy as np

def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    #Interval was given as [x_vals[0], x_vals[-1]]
    a, b = x_vals[0], x_vals[-1]
    #Find the width of each sub-interval
    n = len(x_vals) - 1
    delta_x = (b - a) / n
    # Calculate left-endpoint sum
    left_sum = np.sum(func(x_vals[:-1]) * delta_x)
    return left_sum

def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    a, b = x_vals[0], x_vals[-1] # intervals was given as [x_vals[0], x_vals[-1]]
    n = len(x_vals) - 1 #trying to get the positioning
    delta_x = (b - a) / n # change of x over a given interval/ midpoint formula
    trapezoid_formula = (1 / 2 * delta_x) * (func(x_vals[0]) + 2 * np.sum(func(x_vals[1:n])) + func(x_vals[-1])) #the trapezoidal riemann sum formula - calculates the left sum
    return trapezoid_formula

def simpson(x_vals: np.ndarray, func: np.ufunc) -> float:
    # returns an estimation of area under curve/riemann integrals using simpson estimation. parameters include a 1D array that contains x values, and a universal function chosen to solve integral
    
    # calculating dx or change in x. np.diff calculates the change between each x_val
    change_in_x = np.diff(x_vals)
    # calculating midpoint needed for formula by taking the right endpoint and adding to left endpoint and dividing by 2
    midpoint = (x_vals[:-1] + x_vals[1:]) / 2
    # returning the formula given, f(a) takes in all the left endpoints, which in the end, will be every x_val besides the last. and f(b) takes all the right endpoints except the very first
    return np.sum((change_in_x / 6) * (func(x_vals[:-1]) + 4 * func(midpoint) + func(x_vals[1:])))
