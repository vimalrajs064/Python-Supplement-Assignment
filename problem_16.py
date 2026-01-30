# Problem 16: Find the second largest number in a list
# Find and fix the error

numbers = [45, 89, 12, 78, 34]

# Create a sorted list of unique numbers
unique_numbers = sorted(set(numbers))

if len(unique_numbers) < 2:
    print("List does not have a second largest element")
else:
    second_largest = unique_numbers[-2]
    print(f"Second largest: {second_largest}")
