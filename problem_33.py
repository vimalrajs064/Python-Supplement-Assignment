# Problem 33: Check if string contains only digits
# Find and fix the error

def is_all_digits(text):
    for char in text:           # Check each character
        if not char.isdigit():  # If any non-digit found
            return False
    return True                 # All digits passed

test_str = "12345"
print(f"Is all digits: {is_all_digits(test_str)}")  # True
