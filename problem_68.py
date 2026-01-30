# Problem 68: Find sum of even indexed elements
# Find and fix the error

def sum_even_indices(lst):
    return sum(lst[::2])   # take every 2nd element starting at index 0

numbers = [1, 2, 3, 4, 5, 6]
print(f"Sum of even indices: {sum_even_indices(numbers)}")