def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    while steps!=0:
        steps-=1 
        deltaX = 2*a*x0+b
        x0-=deltaX*lr
    return x0
    pass