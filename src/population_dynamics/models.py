import numpy as np


def lotka_volterra(t, y, r, alpha, beta, d):
    """Classic predator-prey Lotka-Volterra system."""
    N, P = y
    return np.array([
        r * N - alpha * N * P,
        beta * N * P - d * P,
    ], dtype=float)


def lotka_equilibrium(r, alpha, beta, d):
    """Non-trivial equilibrium (prey, predator)."""
    return np.array([d / beta, r / alpha], dtype=float)


def logistic_two_species(t, y, r1, r2, K1, K2, a12, a21):
    """Two-species logistic competition model."""
    N1, N2 = y
    return np.array([
        r1 * N1 * (1.0 - (N1 + a12 * N2) / K1),
        r2 * N2 * (1.0 - (N2 + a21 * N1) / K2),
    ], dtype=float)


def logistic_coexistence_equilibrium(K1, K2, a12, a21):
    """Interior coexistence equilibrium when the denominator is non-zero."""
    den = 1.0 - a12 * a21
    if abs(den) < 1e-14:
        raise ValueError("No unique interior equilibrium when 1 - a12*a21 = 0")
    return np.array([
        (K1 - a12 * K2) / den,
        (K2 - a21 * K1) / den,
    ], dtype=float)
