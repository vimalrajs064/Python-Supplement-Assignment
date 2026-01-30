# Problem 63: Find longest word in a sentence
# Find and fix the error
def find_longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)   # directly find longest by length

text = "The quick brown fox jumps"
print(f"Longest word: {find_longest_word(text)}")