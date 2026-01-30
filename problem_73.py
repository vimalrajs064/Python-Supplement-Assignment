# Problem 73: Find maximum difference between elements
# Find and fix the error

def max_difference(arr):
    if len(arr) < 2:
        return 0
    min_val = arr[0]
    max_diff = float('-inf')   # start with negative infinity
    for num in arr[1:]:
        max_diff = max(max_diff, num - min_val)
        min_val = min(min_val, num)
    return max_diff if max_diff > 0 else 0  # ensure non-negative

numbers = [7, 1, 5, 3, 6, 4]
print(f"Max difference: {max_difference(numbers)}")