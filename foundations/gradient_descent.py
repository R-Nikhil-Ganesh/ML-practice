import random
class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        x = init
        def f(x):
            return x**2
        def df(x):
            return 2*x
        while iterations > 0:
            old = x
            x = old - (learning_rate*df(old))
            iterations -= 1
        return round(x,5)