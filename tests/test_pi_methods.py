import unittest
import math
from pipy.calculators.pi_calculator import PiCalculator

class TestPiMethods(unittest.TestCase):
    def test_calculate_pi_monte_carlo(self):
        calculator = PiCalculator(num_samples=100000)
        pi_estimate = calculator.calculate_pi_monte_carlo()
        self.assertAlmostEqual(pi_estimate, 3.14, places=1)

    def test_calculate_pi_nilakantha(self):
        calculator = PiCalculator(num_samples=1000)
        pi_estimate = calculator.calculate_pi_nilakantha()
        self.assertAlmostEqual(pi_estimate, math.pi)

    def test_calculate_pi_leibniz(self):
        calculator = PiCalculator(num_samples=1000)
        pi_estimate = calculator.calculate_pi_leibniz()
        self.assertAlmostEqual(pi_estimate, math.pi, places=1)

    def test_calculate_pi_monte_carlo_numpy(self):
        calculator = PiCalculator(num_samples=100000)
        pi_estimate = calculator.calculate_pi_monte_carlo_numpy()
        self.assertAlmostEqual(pi_estimate, math.pi, places=1)

if __name__ == '__main__':
    unittest.main()
