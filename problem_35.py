# Problem 35: Calculate percentage
# Find and fix the error

def calculate_percentage(obtained, total):
    percentage = (obtained / total) * 100
    return round(percentage, 2)  # Optional: 2 decimal places

marks = 45
total_marks = 50
result = calculate_percentage(marks, total_marks)
print(f"Percentage: {result:.1f}%")  # Clean output
