import random
import time
import math

# Randomized Selection (QuickSelect)
def randomized_select(arr, k):
    if len(arr) == 1:
        return arr[0]
    
    pivot = random.choice(arr)
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    
    if k < len(lows):
        return randomized_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))

# Deterministic Selection (Median of Medians)
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # divide arr into sublists of 5 elements each
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    
    # pivot is the median of medians
    pivot = deterministic_select(medians, len(medians)//2)
    
    lows = [el for el in arr if el < pivot]
    highs = [el for el in arr if el > pivot]
    pivots = [el for el in arr if el == pivot]
    
    if k < len(lows):
        return deterministic_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# Testing function
def run_experiment():
    input_sizes = [1000, 5000, 10000] 
    distributions = ['random', 'sorted', 'reverse']
    
    print(f"{'Size':>10} {'Dist':>12} {'Randomized(ms)':>15} {'Deterministic(ms)':>18}")
    
    for n in input_sizes:
        for dist in distributions:
            # generate array
            if dist == 'random':
                arr = [random.randint(0, n*10) for _ in range(n)]
            elif dist == 'sorted':
                arr = list(range(n))
            else:  # reverse
                arr = list(range(n, 0, -1))
            
            k = n // 2  # median
            
            # randomized selection
            start = time.time()
            randomized_select(arr.copy(), k)
            rand_time = (time.time() - start) * 1000  # ms
            
            # deterministic selection
            start = time.time()
            deterministic_select(arr.copy(), k)
            det_time = (time.time() - start) * 1000  # ms
            
            print(f"{n:>10} {dist:>12} {rand_time:>15.2f} {det_time:>18.2f}")

if __name__ == "__main__":
    run_experiment()
