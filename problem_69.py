# Problem 69: Convert temperature Fahrenheit to Celsius
# Find and fix the error
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_f = 98.6
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c:.2f}°C")  # format to 2 decimals