class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        def func(x):
            ans = x^2
            return ans
        def deriv(x):
            ans = 2*x
            return ans
        x=init
        # Update rule:        x = x - learning_rate * f'(x)
        for i in range(iterations):
            x = x-learning_rate*deriv(x)
        # Round final answer to 5 decimal places
        return round(x,5)