"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


def test_rejects_negative_rate():
    # Check that calling simulate with a negative rate raises a ValueError
    with pytest.raises(ValueError):
        simulate(1000, -0.1)


def test_matches_law():
    n0 = 1000
    lam = 0.5
    dt = 0.05
    t = 5

    seeds = range(50)
    simulations = [simulate(n0, lam, dt=dt, seed=s) for s in seeds]
    final_atoms = [sim[t] for sim in simulations]
    average_result = np.mean(final_atoms)

    expected = n0 * np.exp(-lam * (t * dt))

    assert average_result == pytest.approx(expected, rel=0.5)