import numpy as np
import matplotlib.pyplot as plt

def calculate_z_scores(values, ddof=0):
    """Calculate z-scores; ddof=0 uses population SD, ddof=1 sample SD."""
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or x.size < 2 or not np.all(np.isfinite(x)):
        raise ValueError("Provide at least two finite, one-dimensional values.")
    sd = np.std(x, ddof=ddof)
    if sd == 0:
        raise ValueError("Z-scores are undefined when SD is zero.")
    return (x - np.mean(x)) / sd

def five_point_summary(values):
    """Return min, Q1, median, Q3, and max."""
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or x.size == 0 or not np.all(np.isfinite(x)):
        raise ValueError("Provide non-empty, finite, one-dimensional data.")
    names = ["Minimum", "Q1", "Median", "Q3", "Maximum"]
    return dict(zip(names, np.percentile(x, [0, 25, 50, 75, 100]).tolist()))

def iqr_outliers(values, multiplier=1.5):
    """Return lower fence, upper fence, and a Boolean outlier mask."""
    x = np.asarray(values, dtype=float)
    if x.ndim != 1 or x.size == 0 or not np.all(np.isfinite(x)):
        raise ValueError("Provide non-empty, finite, one-dimensional data.")
    if multiplier < 0:
        raise ValueError("multiplier must be non-negative.")
    q1, q3 = np.percentile(x, [25, 75])
    iqr = q3 - q1
    lower, upper = q1 - multiplier * iqr, q3 + multiplier * iqr
    return lower, upper, (x < lower) | (x > upper)

if __name__ == "__main__":
    rng = np.random.default_rng(42)
    data = np.concatenate([rng.normal(50, 8, 50), [10, 105, 115]])
    z = calculate_z_scores(data)
    print("Five-point summary:", five_point_summary(data))
    lower, upper, mask = iqr_outliers(data)
    print(f"IQR fences: [{lower:.2f}, {upper:.2f}]")
    print("Potential outlier values:", data[mask])
    print("Z-scores:", np.round(z, 3))
    plt.figure(figsize=(9, 4))
    plt.boxplot(data, vert=False, showmeans=True)
    plt.title("Boxplot: potential outliers")
    plt.xlabel("Data value")
    plt.tight_layout()
    plt.show()
