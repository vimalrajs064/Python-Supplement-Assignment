# Problem 72: Count uppercase and lowercase letters
# Find and fix the error
def count_case(text):
    upper = sum(1 for char in text if char.isupper())
    lower = sum(1 for char in text if char.islower())
    return upper, lower

sentence = "Hello World"
u, l = count_case(sentence)
print(f"Uppercase: {u}, Lowercase: {l}")