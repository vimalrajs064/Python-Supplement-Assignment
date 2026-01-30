# Problem 67: Remove nth element from list
# Find and fix the error
def remove_nth(lst, n):
    if 0 <= n < len(lst):   # check valid index
        return lst[:n] + lst[n+1:]
    return lst[:]           # return a copy if invalid index

numbers = [1, 2, 3, 4, 5]
result = remove_nth(numbers, 2)
print(f"After removing: {result}")