from .linear_regression import linear_regression

def linear_regression_line(mb_tuple):
    """
    Given the output of ``linear_regression()`` function, or provided with
    a tuple of ``(m, b)``, where ``m`` is the slope and ``b`` is the intercept,
    ``inear_regression_line()`` returns a function that calculates y values
    based on given x values.

    Args:
        mb_tuple: A tuple of (m, b) where m is the slope and b is the y intercept.

    Returns:
        A function that accepts ints, floats, lists, or tuples of x values
        and returns y values.

    Examples:
        >>> linear_regression_line(linear_regression([0, 1], [0, 1]))(1)
        1.0
        >>> linear_regression_line(linear_regression([1,3,5,7,9], [10,11,12,13,14]))([1, 2, 3])
        [10.0, 10.5, 11.0]
        >>> linear_regression_line([.5, 9.5])([1, 2, 3])
        [10.0, 10.5, 11.0]
    """

    m = mb_tuple[0]
    b = mb_tuple[1]

    def line_function(x):
        # if int or float, return one value
        if type(x) in [int, float]:
            return((x * m) + b)

        # otherwise
        elif type(x) in [list, tuple]:
            y_values = []

            for ii in x:
                y_values.append(((ii * m) + b))

            return(y_values)

    return(line_function)
