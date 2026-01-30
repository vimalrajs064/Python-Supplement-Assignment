# Problem 80: Find mode (most frequent element)
# Find and fix the error
from collections import Counter

def find_mode(lst):
    freq = Counter(lst)
    max_freq = max(freq.values())
    modes = [key for key, value in freq.items() if value == max_freq]
    return modes if len(modes) > 1 else modes[0]

numbers = [1, 2, 2, 3, 3, 3, 4]
print(f"Mode: {find_mode(numbers)}")