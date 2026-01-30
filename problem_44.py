# Problem 44: Print Fibonacci sequence
# Find and fix the error

def fibonacci(n):
    if n <= 0:
        return []          # no numbers for non-positive n
    elif n == 1:
        return [0]         # only the first Fibonacci number
    elif n == 2:
        return [0, 1]      # first two Fibonacci numbers
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(f"First 10 Fibonacci numbers: {fibonacci(10)}")