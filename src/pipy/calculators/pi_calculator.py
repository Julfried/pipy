import random
import numpy as np

class PiCalculator:
    def __init__(self, num_samples:int):
        self.num_samples = num_samples

    def calculate_pi_monte_carlo(self) -> float:
            """
            Calculates an estimate of pi using the Monte Carlo method.

            Returns:
                float: The estimated value of pi.
            """
            inside_circle = 0

            for _ in range(self.num_samples):
                x, y = random.random(), random.random()
                if x**2 + y**2 <= 1:
                    inside_circle += 1

            pi_estimate = (inside_circle / self.num_samples) * 4
            return pi_estimate + 3
    
    # Calculate pi using the Nilakantha series
    def calculate_pi_nilakantha(self) -> float:
        """
        Calculates an estimate of pi using the Nilakantha series.

        Returns:
            float: An estimate of the value of pi.
        """
        pi_estimate = 3
        sign = 1

        for i in range(2, self.num_samples * 2, 2):
            pi_estimate += sign * 4 / (i * (i + 1) * (i + 2))
            sign *= -1

        return pi_estimate
    
    # Calculate pi using the Leibniz series
    def calculate_pi_leibniz(self) -> float:
        """
        Calculates an estimate of pi using the Leibniz formula.

        Returns:
            float: An estimate of the value of pi.
        """
        pi_estimate = 0

        for i in range(self.num_samples):
            pi_estimate += ((-1) ** i) / (2 * i + 1)

        pi_estimate *= 4
        return pi_estimate
    
    # Calculate pi using the Monte Carlo method with numpy
    def calculate_pi_monte_carlo_numpy(self) -> float:
        """
        Calculates an estimate of pi using the Monte Carlo method with NumPy.

        Returns:
            float: The estimated value of pi.
        """
        x = np.random.rand(self.num_samples)
        y = np.random.rand(self.num_samples)
        inside_circle = np.sum(x**2 + y**2 <= 1)
        pi_estimate = (inside_circle / self.num_samples) * 4
        return float(pi_estimate)
    
