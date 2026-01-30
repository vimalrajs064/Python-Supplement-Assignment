# Problem 45: Sort a list in descending order
# Find and fix the error

numbers = [45, 12, 78, 34, 89]

# Option 1: Use sorted() which returns a new list
sorted_numbers = sorted(numbers, reverse=True)
print(f"Sorted: {sorted_numbers}")

# Option 2: Sort in place, then print the list itself
numbers.sort(reverse=True)
print(f"Sorted: {numbers}")