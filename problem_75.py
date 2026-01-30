# Problem 75: Check if parentheses are balanced
# Find and fix the error
def are_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in pairs.values():   # opening brackets
            stack.append(char)
        elif char in pairs:          # closing brackets
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return not stack  # cleaner check

expr = "((a + b) * [c - d])"
print(f"Balanced: {are_balanced(expr)}")