import random
import time
import statistics
import matplotlib.pyplot as plt

# 1. ALGORITHM IMPLEMENTATIONS
def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    pivot = random.choice(arr)
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))


def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

    pivot = median_of_medians(medians, len(medians)//2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows):
        return median_of_medians(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return median_of_medians(highs, k - len(lows) - len(pivots))

# 2. EXPERIMENT PARAMETERS
sizes = [1000, 5000, 10000]
distributions = ["random", "sorted", "reverse"]
trials = 30  # repeat each test 30 times

results = { "randomized": {}, "deterministic": {} }

# 3. RUN EXPERIMENTS
for dist in distributions:
    results["randomized"][dist] = []
    results["deterministic"][dist] = []

    for n in sizes:
        timings_randomized = []
        timings_deterministic = []

        for _ in range(trials):

            if dist == "random":
                arr = [random.randint(0, 1000000) for _ in range(n)]
            elif dist == "sorted":
                arr = list(range(n))
            elif dist == "reverse":
                arr = list(range(n, 0, -1))

            k = n // 2

            # Time randomized selection
            start = time.perf_counter()
            quickselect(arr.copy(), k)
            timings_randomized.append((time.perf_counter() - start) * 1000)

            # Time deterministic selection
            start = time.perf_counter()
            median_of_medians(arr.copy(), k)
            timings_deterministic.append((time.perf_counter() - start) * 1000)

        # Store mean values
        results["randomized"][dist].append((
            statistics.mean(timings_randomized),
            statistics.stdev(timings_randomized)
        ))
        results["deterministic"][dist].append((
            statistics.mean(timings_deterministic),
            statistics.stdev(timings_deterministic)
        ))

# 4. PRINT RESULTS TABLE
print(f"{'Size':>8} {'Dist':>10} {'Randomized Mean (ms)':>22} {'Deterministic Mean (ms)':>25}")

for i, n in enumerate(sizes):
    for dist in distributions:
        r_mean, r_std = results["randomized"][dist][i]
        d_mean, d_std = results["deterministic"][dist][i]
        print(f"{n:>8} {dist:>10} {r_mean:>15.2f}±{r_std:.2f} {d_mean:>15.2f}±{d_std:.2f}")

# 5. PLOT RESULTS WITH ERROR BARS
plt.figure(figsize=(10, 6))

for dist in distributions:
    r_means = [m for m, s in results["randomized"][dist]]
    r_stds  = [s for m, s in results["randomized"][dist]]

    d_means = [m for m, s in results["deterministic"][dist]]
    d_stds  = [s for m, s in results["deterministic"][dist]]

    plt.errorbar(sizes, r_means, yerr=r_stds, label=f"Randomized - {dist}",
                 fmt='-o', capsize=5)
    plt.errorbar(sizes, d_means, yerr=d_stds, label=f"Deterministic - {dist}",
                 fmt='--s', capsize=5)

plt.title("Empirical Comparison of Selection Algorithms (Mean ± Std Dev)")
plt.xlabel("Input Size (n)")
plt.ylabel("Running Time (ms)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
