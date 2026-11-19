
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






## PW3-SESSION 1

### task 2- HISTOGRAM ANALYSIS

#### age:
Roughly bell-shaped, slightly skewed to the left
Most patients are between 53 and 67 years old, with a flatter part between 40 and 55
Few patients are under 35 or over 70

#### chol:
Skewed to the right.
Most values fall around 200-250
There is a long tail to the right, with a few values above 400 and one clear outlier near 560

#### trestbps:
Skewed to the right.
Most values fall between 120 and 140.
Values above 160 are rare

#### thalach:
Skewed to the left.
Peak is around 150-165
Values below 80 are very rare

## PW3 - SESSION 1

### Dataset
Heart Disease (Cleveland), UCI / Kaggle. 303 patients, 14 columns.
Continuous columns used: age, chol, trestbps, thalach.

### task 1 - loading
- Loaded with pd.read_csv("heart_disease.csv"), shape = (303, 14)
- Isolated the four continuous columns: age, chol, trestbps, thalach

### task 2 - shape of the variables
![histograms](session1_histograms.png)

#### age:
Roughly bell-shaped, peak at 55-65, shorter tail on the young side (range 29-77, median 56)

#### chol:
Skewed to the right. Most values are 200-300, long right tail, one extreme value at 564 (median 241)

#### trestbps:
Skewed to the right. Peak at 120-140, tail going up to 200 (median 130)

#### thalach:
Skewed to the left. Peak at 150-165, long tail towards low values, minimum 71 (median 153)

### task 3 - normality
Evidence used: Q-Q plots and the Shapiro-Wilk test (H0: data is normal, p < 0.05 rejects normality).
With n = 303 Shapiro-Wilk is very sensitive, so I also look at the plot and the skewness.

#### age:
Verdict: approximately normal
- Q-Q plot is almost a straight line, only small deviations at both ends
- Shapiro-Wilk p = 0.006, so it rejects normality
- But skew is small (-0.21) and the sample is big (303), so Shapiro-Wilk finds even tiny differences
- I treat age as roughly normal

#### chol:
Verdict: not normal
- Q-Q plot: right side goes far above the line, group of points near 400-420 and one outlier at 564
- Shapiro-Wilk p = 5.9e-09

#### trestbps:
Verdict: not normal
- Q-Q plot: right tail goes above the line (above 160, values 180 and 200)
- The points form steps because blood pressure is recorded in whole numbers
- Shapiro-Wilk p = 1.8e-06

#### thalach:
Verdict: not normal
- Q-Q plot: middle follows the line, but the left tail is much longer than normal (values 71, 88, 90) and the right end is slightly shorter
- Shapiro-Wilk p = 7.0e-05
- So in Session 2 I will use Mann-Whitney for thalach

![qq age](qq_age.png) ![qq chol](qq_chol.png)
![qq trestbps](qq_trestbps.png) ![qq thalach](qq_thalach.png)


## PW3 - SESSION 2

### task 4 - heart rate: disease vs healthy
Question: do patients with heart disease reach a different max heart rate (thalach)?
- Groups: disease (target = 1), n = 139, and healthy (target = 0), n = 164
- Method: Mann-Whitney U test, because thalach is not normal (Session 1)
- Result: p = 1.86e-13
- p < 0.05, so I reject H0: the two groups really differ

Mean +- standard error:
- disease: 139.26 +- 1.92
- healthy: 158.38 +- 1.50

![means](session2_means.png)

The error bars of the two groups are far apart and do not overlap, so the picture agrees
with the test: patients with heart disease reach a lower max heart rate (about 19 bpm lower).

### task 5 - age and thalach
- Method: Spearman correlation (thalach is not normal)
- Result: rho = -0.39, p = 1.5e-12

![age vs thalach](session2_age_thalach.png)

Interpretation: age and thalach move in opposite directions. Older patients tend to have
a lower max heart rate. The relationship is moderate (rho = -0.39), the points are quite
spread out, and it is not due to chance (p is very small).

## Dataset 2 - chemicals and cancer

### task 6 - naive analysis
Pearson correlation with malignancy (1000 patients):
- benzene: r = 0.385 (p = 1.3e-36)
- cadmium: r = 0.88 (p ~ 0)

Taken at face value, cadmium looks like the cause because its association is much stronger.

### task 7 - look again
Suspected third variable: pollution_index.
- pollution_index vs cadmium: r = 0.982
- pollution_index vs malignancy: r = 0.895
- pollution_index vs benzene: r = 0.054

Pollution is strongly linked to both cadmium and malignancy, so it can create a fake association.
To test this I kept only patients with similar pollution (40 < pollution_index < 60, 199 patients)
and recomputed the correlations:
- benzene vs malignancy: r = 0.702 (it became stronger)
- cadmium vs malignancy: r = 0.316 (it dropped a lot)

## Bonus - how unpredictable is target?

Proportions of the target column:
- 0 (healthy): 0.541
- 1 (disease): 0.459

Measure: Shannon entropy, H = -sum(p * log2(p)) = 0.995 bits.
The maximum for two categories is 1 bit (50/50), so the column is almost perfectly balanced.
It is hard to guess: always guessing "healthy" would be right only 54% of the time.


### Conclusion: 
benzene is the real cause of malignancy. Cadmium only looked guilty because it
follows pollution_index almost perfectly (r = 0.982), and pollution_index is linked to malignancy.
When pollution is held roughly constant, the cadmium effect mostly disappears and the benzene
effect stays strong. The remaining cadmium correlation (0.316) is because the pollution range
40-60 is still not narrow.


