# Problem 34: Copy a list
# Find and fix the error

original = [1, 2, 3, 4, 5]
copy = original.copy()      # Fixed: Creates new list
copy.append(6)
print(f"Original: {original}")  # [1, 2, 3, 4, 5]
print(f"Copy: {copy}")          # [1, 2, 3, 4, 5, 6]

