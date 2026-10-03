import sys, unittest
from pathlib import Path
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from population_dynamics.rk4 import rk4
from population_dynamics.models import logistic_coexistence_equilibrium
from population_dynamics.experiments import simulate_logistic, LOGISTIC_DEFAULT

class TestPopulationDynamics(unittest.TestCase):
    def test_rk4_on_exponential(self):
        def f(t, y): return y
        t, y = rk4(f, 0.0, [1.0], 1.0, 0.01)
        self.assertAlmostEqual(y[-1,0], np.e, places=7)

    def test_logistic_equilibrium_formula(self):
        eq = logistic_coexistence_equilibrium(50.0, 40.0, 0.5, 0.4)
        self.assertTrue(np.allclose(eq, [37.5, 25.0]))

    def test_logistic_simulation_converges_to_equilibrium(self):
        _, y = simulate_logistic(T=80.0, h=0.02)
        eq = logistic_coexistence_equilibrium(LOGISTIC_DEFAULT['K1'], LOGISTIC_DEFAULT['K2'], LOGISTIC_DEFAULT['a12'], LOGISTIC_DEFAULT['a21'])
        self.assertTrue(np.linalg.norm(y[-1] - eq) < 1e-4)

if __name__ == '__main__': unittest.main()
