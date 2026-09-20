
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
