from pathlib import Path
import argparse, sys
ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / 'src'))

from population_dynamics.experiments import simulate_lotka, simulate_logistic
from population_dynamics.models import lotka_equilibrium, logistic_coexistence_equilibrium
from population_dynamics.experiments import LOTKA_DEFAULT, LOGISTIC_DEFAULT

p = argparse.ArgumentParser(description='Run the GM3 population-dynamics simulations.')
p.add_argument('--model', choices=['lotka','logistic'], default='lotka')
p.add_argument('--h', type=float, default=0.01)
args = p.parse_args()

if args.model == 'lotka':
    t, y = simulate_lotka(h=args.h)
    eq = lotka_equilibrium(**LOTKA_DEFAULT)
else:
    t, y = simulate_logistic(h=args.h)
    eq = logistic_coexistence_equilibrium(LOGISTIC_DEFAULT['K1'], LOGISTIC_DEFAULT['K2'], LOGISTIC_DEFAULT['a12'], LOGISTIC_DEFAULT['a21'])

print(f'model={args.model}')
print(f'steps={len(t)-1}')
print(f'final_state={y[-1]}')
print(f'theoretical_equilibrium={eq}')
