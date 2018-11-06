from ad import gh  # the gradient and hessian function generator

def objective(x):
    return (x[0] - 10.0)**2 + (x[1] + 5.0)**2


grad, hess = gh(objective)