import numpy as np
from .models import lotka_volterra, logistic_two_species
from .rk4 import rk4

LOTKA_DEFAULT = dict(r=1.0, alpha=0.1, beta=0.075, d=1.5)
LOGISTIC_DEFAULT = dict(r1=0.8, r2=0.6, K1=50.0, K2=40.0, a12=0.5, a21=0.4)


def simulate_lotka(y0=(10.0, 5.0), t0=0.0, T=60.0, h=0.01, **overrides):
    p = LOTKA_DEFAULT | overrides
    params = (p['r'], p['alpha'], p['beta'], p['d'])
    return rk4(lotka_volterra, t0, np.asarray(y0, dtype=float), T, h, params)


def simulate_logistic(y0=(10.0, 8.0), t0=0.0, T=50.0, h=0.01, **overrides):
    p = LOGISTIC_DEFAULT | overrides
    params = (p['r1'], p['r2'], p['K1'], p['K2'], p['a12'], p['a21'])
    return rk4(logistic_two_species, t0, np.asarray(y0, dtype=float), T, h, params)
