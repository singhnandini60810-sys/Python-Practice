# ==========================================
# PYTHON BASICS – 10 QUESTIONS IN ONE CODE
# ==========================================

print("----- PYTHON BASICS PRACTICE -----")

# 1️⃣ Check if a number is even or odd
print("\n1. Check Even or Odd")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2️⃣ Find factorial of a number
print("\n2. Find Factorial")
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print("Factorial:", factorial)


# 3️⃣ Check if a number is prime
print("\n3. Check Prime")
num = int(input("Enter a number: "))
if num < 2:
    print("Not Prime")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")


# 4️⃣ Reverse a number
print("\n4. Reverse a Number")
num = int(input("Enter a number: "))
print("Reversed:", int(str(num)[::-1]))


# 5️⃣ Count vowels in a string
print("\n5. Count Vowels")
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print("Total vowels:", count)


# 6️⃣ Find largest of three numbers
print("\n6. Largest of Three Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Largest:", max(a, b, c))


# 7️⃣ Fibonacci series up to n terms
print("\n7. Fibonacci Series")
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 8️⃣ Check palindrome string
print("\n8. Check Palindrome")
text = input("Enter a string: ")
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 9️⃣ Sum of digits
print("\n9. Sum of Digits")
num = input("Enter a number: ")
digit_sum = sum(int(d) for d in num)
print("Sum of digits:", digit_sum)


# 🔟 Multiplication table
print("\n10. Multiplication Table")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

print("\n----- END OF PROGRAM -----")
