# Problem 79: Calculate compound interest
# Find and fix the error
def compound_interest(principal, rate, time, n):
    # rate is given in percentage, so convert to decimal
    rate_decimal = rate / 100
    amount = principal * (1 + rate_decimal / n) ** (n * time)
    interest = amount - principal
    return interest

p = 1000
r = 5   # annual interest rate in %
t = 2   # time in years
n = 4   # compounding per year (quarterly)

print(f"Compound Interest: {compound_interest(p, r, t, n):.2f}")