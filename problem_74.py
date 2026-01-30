# Problem 74: Find first non-repeating character
# Find and fix the error
from collections import Counter

def first_non_repeating(text):
    char_count = Counter(text)
    for char in text:   # preserve order
        if char_count[char] == 1:
            return char
    return None

word = "programming"
print(f"First non-repeating: {first_non_repeating(word)}")