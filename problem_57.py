# Problem 57: Find LCM of two numbers
# Find and fix the error
def gcd(a, b):
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:   # handle zero case
        return 0
    return abs(a * b) // gcd(a, b)   # use abs for safety

print(f"LCM of 12 and 18: {lcm(12, 18)}")