import random
# Deterministic Selection
def deterministic_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k-1]
    
    # Step 1: Divide into groups of 5 and find medians
    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    
    # Step 2: Find the median of medians recursively
    pivot = deterministic_select(medians, len(medians)//2 + 1)
    
    # Step 3: Partition the array
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    # Step 4: Recurse into the correct partition
    if k <= len(lows):
        return deterministic_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return deterministic_select(highs, k - len(lows) - len(pivots))

# Example Usage
if __name__ == "__main__":
    test_array = [7, 2, 1, 6, 8, 5, 3, 4, 3, 5]
    k = 5
    
    print(f"Array: {test_array}")
    print(f"{k}-th smallest (Deterministic): {deterministic_select(test_array, k)}")
    
    # Edge case with duplicates
    test_array2 = [4, 2, 4, 1, 3, 2, 5, 4]
    k2 = 4
    print(f"\nArray with duplicates: {test_array2}")
    print(f"{k2}-th smallest (Deterministic): {deterministic_select(test_array2, k2)}")
