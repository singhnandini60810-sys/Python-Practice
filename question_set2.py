# ==========================================
# PYTHON BASICS – 10 MORE QUESTIONS
# ==========================================

print("----- PYTHON BASICS PRACTICE PART 2 -----")

# 1️⃣ Swap two numbers
print("\n1. Swap Two Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("First:", a)
print("Second:", b)


# 2️⃣ Check Armstrong number
print("\n2. Check Armstrong Number")
num = int(input("Enter a number: "))
power = len(str(num))
total = sum(int(digit) ** power for digit in str(num))
if total == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")


# 3️⃣ Count digits in a number
print("\n3. Count Digits")
num = input("Enter a number: ")
print("Total digits:", len(num))


# 4️⃣ Find sum of first n natural numbers
print("\n4. Sum of First N Natural Numbers")
n = int(input("Enter n: "))
print("Sum:", n * (n + 1) // 2)


# 5️⃣ Convert Celsius to Fahrenheit
print("\n5. Celsius to Fahrenheit")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)


# 6️⃣ Simple calculator
print("\n6. Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


# 7️⃣ Find GCD of two numbers
print("\n7. Find GCD")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b:
    a, b = b, a % b
print("GCD:", a)


# 8️⃣ Print star pattern
print("\n8. Star Pattern")
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)


# 9️⃣ Check if a number is positive, negative or zero
print("\n9. Check Number Type")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# 🔟 Find LCM of two numbers
print("\n10. Find LCM")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
lcm = abs(a*b)
temp_a, temp_b = a, b
while temp_b:
    temp_a, temp_b = temp_b, temp_a % temp_b
gcd = temp_a
print("LCM:", lcm // gcd)

print("\n----- END OF PROGRAM -----")
