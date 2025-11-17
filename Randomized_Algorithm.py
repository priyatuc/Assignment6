import random
# Randomized Selection
def randomized_select(arr, k):
    # Base case: if the array has only one element, return it
    if len(arr) == 1:
        return arr[0]
    
    # Step 1: Randomly select a pivot element from the array
    pivot = random.choice(arr)
    
    # Step 2: Partition the array into three lists: lows, highs, and pivots
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]
    
    # Step 3: Determine which partition contains the k-th smallest element
    if k <= len(lows):
        return randomized_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        # Adjust k to account for elements removed from lows and pivots
        return randomized_select(highs, k - len(lows) - len(pivots))

# Example Usage
if __name__ == "__main__":
    test_array = [7, 2, 1, 6, 8, 5, 3, 4, 3, 5]
    k = 5
    
    print(f"Array: {test_array}")
    print(f"{k}-th smallest (Randomized): {randomized_select(test_array, k)}")
    
    # Edge case with duplicates
    test_array2 = [4, 2, 4, 1, 3, 2, 5, 4]
    k2 = 4
    print(f"\nArray with duplicates: {test_array2}")
    print(f"{k2}-th smallest (Randomized): {randomized_select(test_array2, k2)}")
