# ------------------------------------------------------------
# PYTHON STRING PROBLEMS WITH SOLUTIONS
# ------------------------------------------------------------


# ------------------------------------------------------------
# Problem 1:
# Write a Python program to count the number of vowels in a string.
# Example: "education" → 5
# ------------------------------------------------------------

text = "education"
vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowels:", count)



# ------------------------------------------------------------
# Problem 2:
# Write a Python program to reverse a string.
# Example: "Python" → "nohtyP"
# ------------------------------------------------------------

text = "Python"
reversed_text = text[::-1]

print("Reversed string:", reversed_text)



# ------------------------------------------------------------
# Problem 3:
# Write a Python program to check if a string is a palindrome.
# Example: "madam" → Palindrome
# ------------------------------------------------------------

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")



# ------------------------------------------------------------
# Problem 4:
# Write a Python program to count the number of words in a string.
# Example: "Python is easy to learn" → 5
# ------------------------------------------------------------

sentence = "Python is easy to learn"

words = sentence.split()
print("Word count:", len(words))



# ------------------------------------------------------------
# Problem 5:
# Write a Python program to convert a string to uppercase.
# Example: "hello world" → "HELLO WORLD"
# ------------------------------------------------------------

text = "hello world"
print("Uppercase:", text.upper())



# ------------------------------------------------------------
# Problem 6:
# Write a Python program to remove spaces from a string.
# Example: "hello world" → "helloworld"
# ------------------------------------------------------------

text = "hello world"
result = text.replace(" ", "")

print("Without spaces:", result)



# ------------------------------------------------------------
# Problem 7:
# Write a Python program to count the occurrence of a character
# in a string.
# Example: string="banana", char="a" → 3
# ------------------------------------------------------------

string = "banana"
char = "a"

count = string.count(char)

print("Occurrences:", count)



# ------------------------------------------------------------
# Problem 8:
# Write a Python program to find the longest word in a sentence.
# Example: "Python programming is powerful"
# Output: "programming"
# ------------------------------------------------------------

sentence = "Python programming is powerful"

words = sentence.split()
longest = max(words, key=len)

print("Longest word:", longest)



# ------------------------------------------------------------
# Problem 9:
# Write a Python program to replace a word in a sentence.
# Example: Replace "Python" with "Java"
# ------------------------------------------------------------

sentence = "Python is fun"

new_sentence = sentence.replace("Python", "Java")

print("Updated sentence:", new_sentence)



# ------------------------------------------------------------
# Problem 10:
# Write a Python program to check if two strings are anagrams.
# Example: "listen" and "silent" → Anagram
# ------------------------------------------------------------

str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")
