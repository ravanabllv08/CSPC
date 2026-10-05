
# CSPC - Computer Science for Physics and Chemistry

My coursework repository. Each practical is under `PW<n>/Lab <X>/`.

## Setup

Create the environment for a given lab:

```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
```

---

## PW1 - Lab A: Reproducible Foundations

**What I built:**

- I set up the Conda environment and worked with the radioactive decay simulation.
- I added tests and compared the Python loop with the NumPy version.

**Speed comparison (loop vs NumPy):**

- loop : 4.3097 s
- numpy : 0.0004 s
- speed-up: 10381.32 x faster

**Tests:** all passing? **yes**

**Conclusion:**

- All three tests passed. I also learned how to test for errors and check the simulation result.
- The NumPy version was much faster than the Python loop. I also got more familiar with Conda, pytest and working with Git.



## PW1 - Lab B

What the data showed:

The observed count decreased over time, from 5000 at time 0 to 17 at time 19.5.
The decrease was rapid at the beginning and became slower as the count approached zero.

Comparison with the analytical law:

The observed data followed the expected exponential decay trend. There were some small fluctuations in the observed values, but overall the data matched the analytical law reasonably well.

Snakemake pipeline:

The Snakemake pipeline automatically runs plot.py using decay_observed.csv as input and produces figure.png as the output.







## PW2 - Lab A

-The mean acceleration was -8.58 m/s**2
-The acceleration was noisier because taking derivatives makes the noise bigger
-Integrating the acceleration back to velocity and then position showed that the recovered position was close to the original position. The largest difference was 0.78 m, which is within about 1 metre

## PW2 -Lab B 

### PART 2
Starting from x0 = 0, gradient descent and SLSQP gave almost the same result, around x = -1.30. Newton gave x = 0.17. Since the second derivative is negative there (g''(x) = -5.65), this point is a maximum, not a minimum
When I started from x0 = 2 the gradient descent and Newton both converged to x = 1.13. For Newton, g''(x) = 9.35, so this time it found a minimum. SLSQP still found the minimum around x = -1.30
So the three methods do not always give the same result. The starting point can affect where the method ends up. Newton can even find a maximum instead of a minimun, depending on the starting point

### Part 3 — Reaction rate

The fitted first order reaction rate constant was:
k = 0.2618

The fitted curve closely matched the measured concentration data

### Part 4 — Chemical equilibrium

For the reaction H2 + I2 -> 2HI, the equilibrium extent was approximately:
x = 0.6638

The equilibrium amounts were

- H2 = 0.3362 mol
- I2 = 0.3362 mol
- HI = 1.3277 mol

Newton's method and SLSQP gave almost the same equilibrium extent

### Part 5 — Titration equivalence point

The equivalence point was found using the maximum slope of the pH curve
Equivalence point = 50.0 ml


