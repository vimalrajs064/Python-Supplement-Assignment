numbers = [45, 12, 78, 34, 89]
minimum = numbers[0]      # Start with first element: 45
for num in numbers:       # Check all elements including first
    if num < minimum:     # 12 < 45 → update, 78 > 12 → skip, etc.
        minimum = num
print(f"Minimum: {minimum}") 
