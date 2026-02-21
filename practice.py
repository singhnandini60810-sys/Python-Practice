# ✅ Question 1
# Write a program to print the sum of digits of a number.
num = input("Enter a number: ")

total = 0
for digit in num:
    total += int(digit)
print("Sum of digits:", total)


# ✅ Question 2
# Write a program to print the reverse of a number.
num = input("Enter a number: ")

reverse = num[::-1]
print("Reverse of number:", reverse)


# ✅ Question 3
# Write a program to check whether a number is a palindrome.
num = input("Enter a number: ")

if num == num[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


# ✅ Question 4
# Write a program to print the sum of even digits of a number.
num = input("Enter a number: ")

total = 0
for digit in num:
    if int(digit) % 2 == 0:
        total += int(digit)
print("Sum of even digits:", total)


# ✅ Question 5
# Write a program to print the product of odd digits of a number.
num = input("Enter a number: ")

product = 1
found = False

for digit in num:
    if int(digit) % 2 != 0:
        product *= int(digit)
        found = True

if found:
    print("Product of odd digits:", product)
else:
    print("No odd digits found.")


# ✅ Question 6
# Capitalize the first letter of each word.
text = input("Enter a sentence: ")

words = text.split()
new_sentence = ""

for word in words:
    new_sentence += word.capitalize() + " "

print("Capitalized sentence:", new_sentence.strip())


# ✅ Question 7
# Longest substring containing only consonants.
text = input("Enter a string: ")

vowels = "aeiouAEIOU"
longest = ""
current = ""

for char in text:
    if char.isalpha() and char not in vowels:
        current += char
        if len(current) > len(longest):
            longest = current
    else:
        current = ""

print("Longest consonant substring:", longest)


# ✅ Question 8
# Capitalize every other letter.
text = input("Enter a string: ")

result = ""
for i in range(len(text)):
    if i % 2 == 0:
        result += text[i].lower()
    else:
        result += text[i].upper()

print("Modified string:", result)


# ✅ Question 9
# Count words, characters, and percentage of alphanumeric characters.
text = input("Enter a sentence: ")

words = text.split()
total_words = len(words)
total_characters = len(text)

alnum_count = 0
for char in text:
    if char.isalnum():
        alnum_count += 1

percentage = (alnum_count / total_characters) * 100

print("Total words:", total_words)
print("Total characters:", total_characters)
print("Percentage of alphanumeric characters:", round(percentage, 2), "%")


# ✅ Question 10
# Extract two list slices and calculate sum and average.
numbers = list(range(1, 21))

first_slice = numbers[5:16:2]
second_slice = numbers[::4]

print("First slice:", first_slice)
print("Sum of first slice:", sum(first_slice))

print("Second slice:", second_slice)
print("Average of second slice:", sum(second_slice) / len(second_slice))


# Continue same pattern for remaining questions...
