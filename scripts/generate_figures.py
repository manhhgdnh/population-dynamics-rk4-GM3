from pathlib import Path
import sys
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))

from population_dynamics.experiments import simulate_lotka, simulate_logistic, LOTKA_DEFAULT, LOGISTIC_DEFAULT
from population_dynamics.models import lotka_equilibrium, logistic_coexistence_equilibrium

OUT = ROOT / 'results' / 'figures'
OUT.mkdir(parents=True, exist_ok=True)


def save(name):
    plt.tight_layout()
    plt.savefig(OUT / name, dpi=180, bbox_inches='tight')
    plt.close()

# Lotka time dynamics
lt, ly = simulate_lotka()
plt.figure(figsize=(9, 4.8))
plt.plot(lt, ly[:,0], label='Prey N(t)')
plt.plot(lt, ly[:,1], label='Predators P(t)')
plt.xlabel('Time'); plt.ylabel('Population'); plt.title('Lotka–Volterra population dynamics')
plt.grid(True, alpha=.3); plt.legend(); save('lotka_time_series.png')

# Lotka phase portrait
E = lotka_equilibrium(**LOTKA_DEFAULT)
plt.figure(figsize=(6.3, 5.8))
plt.plot(ly[:,0], ly[:,1], label='RK4 trajectory')
plt.scatter([E[0]], [E[1]], marker='x', s=100, label='Non-trivial equilibrium')
plt.xlabel('Prey N'); plt.ylabel('Predators P'); plt.title('Lotka–Volterra phase portrait')
plt.grid(True, alpha=.3); plt.legend(); save('lotka_phase_portrait.png')

# Step-size sensitivity
plt.figure(figsize=(6.6, 5.8))
for h in [1.0, 0.5, 0.1, 0.01]:
    _, y = simulate_lotka(h=h)
    plt.plot(y[:,0], y[:,1], label=f'h={h}')
plt.scatter([E[0]], [E[1]], marker='x', s=90, label='Equilibrium')
plt.xlabel('Prey N'); plt.ylabel('Predators P'); plt.title('RK4 step-size sensitivity')
plt.grid(True, alpha=.3); plt.legend(); save('lotka_step_size.png')

# Logistic time dynamics
lg_t, lg_y = simulate_logistic()
plt.figure(figsize=(9, 4.8))
plt.plot(lg_t, lg_y[:,0], label='Species 1')
plt.plot(lg_t, lg_y[:,1], label='Species 2')
plt.xlabel('Time'); plt.ylabel('Population'); plt.title('Two-species logistic competition')
plt.grid(True, alpha=.3); plt.legend(); save('logistic_time_series.png')

# Logistic phase portrait with theoretical equilibrium
Leq = logistic_coexistence_equilibrium(LOGISTIC_DEFAULT['K1'], LOGISTIC_DEFAULT['K2'], LOGISTIC_DEFAULT['a12'], LOGISTIC_DEFAULT['a21'])
plt.figure(figsize=(6.3, 5.8))
plt.plot(lg_y[:,0], lg_y[:,1], label='RK4 trajectory')
plt.scatter([Leq[0]], [Leq[1]], marker='x', s=100, label='Coexistence equilibrium')
plt.xlabel('Species 1'); plt.ylabel('Species 2'); plt.title('Logistic competition phase portrait')
plt.grid(True, alpha=.3); plt.legend(); save('logistic_phase_portrait.png')

# Competition sensitivity
plt.figure(figsize=(7, 5.8))
for a12, a21 in [(0.5,0.5),(0.9,0.1),(0.1,0.9),(1.3,1.3)]:
    _, y = simulate_logistic(a12=a12, a21=a21)
    plt.plot(y[:,0], y[:,1], label=f'a12={a12}, a21={a21}')
plt.xlabel('Species 1'); plt.ylabel('Species 2'); plt.title('Effect of interspecific competition')
plt.grid(True, alpha=.3); plt.legend(); save('competition_sensitivity.png')

print(f'Figures written to {OUT}')
