import numpy as np


def rk4(f, t0, y0, T, h, params=()):
    """Integrate y' = f(t, y, *params) with the classical fourth-order RK scheme."""
    if h <= 0:
        raise ValueError("h must be positive")
    if T <= t0:
        raise ValueError("T must be greater than t0")

    n = int(np.ceil((T - t0) / h))
    t = np.empty(n + 1, dtype=float)
    y0 = np.asarray(y0, dtype=float)
    y = np.empty((n + 1, y0.size), dtype=float)
    t[0] = t0
    y[0] = y0

    for i in range(n):
        hi = min(h, T - t[i])
        k1 = f(t[i], y[i], *params)
        k2 = f(t[i] + hi / 2, y[i] + hi * k1 / 2, *params)
        k3 = f(t[i] + hi / 2, y[i] + hi * k2 / 2, *params)
        k4 = f(t[i] + hi, y[i] + hi * k3, *params)
        y[i + 1] = y[i] + (hi / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        t[i + 1] = t[i] + hi

    return t, y
