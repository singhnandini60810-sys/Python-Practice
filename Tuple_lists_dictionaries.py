# ======================================================
#                     TUPLE
# ======================================================

# ✅ Question 1
# Write a Python program to convert a tuple to a string.
tup = ('P', 'Y', 'T', 'H', 'O', 'N')

result = ''.join(tup)
print("String:", result)


# ✅ Question 2
# Write a Python program to find repeated items in a tuple.
tup = (1, 2, 3, 2, 4, 5, 1, 6)

repeated = set()
for item in tup:
    if tup.count(item) > 1:
        repeated.add(item)
print("Repeated items:", repeated)


# ✅ Question 3
# Write a Python program to check whether an element exists within a tuple.
tup = (10, 20, 30, 40, 50)

element = int(input("Enter element to search: "))
if element in tup:
    print("Element exists in tuple.")
else:
    print("Element does not exist in tuple.")


# ✅ Question 4
# Write a Python program to convert a tuple to a dictionary.
tup = (('a', 1), ('b', 2), ('c', 3))

result = dict(tup)
print("Dictionary:", result)


# ✅ Question 5
# Write a Python program to reverse a tuple.
tup = (1, 2, 3, 4, 5)

reversed_tup = tup[::-1]
print("Reversed tuple:", reversed_tup)


# ======================================================
#                     LIST
# ======================================================

# ✅ Question 1
# Find the second smallest number in a list.
numbers = [10, 20, 4, 45, 99]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second smallest:", unique_numbers[1])
else:
    print("Second smallest does not exist.")


# ✅ Question 2
# Find the second largest number in a list.
numbers = [10, 20, 4, 45, 99]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("Second largest does not exist.")


# ======================================================
#                  DICTIONARY
# ======================================================

# ✅ Question 1
# Create and display all combinations of letters selecting each letter from a different key.
data = {'1': ['a', 'b'], '2': ['c', 'd']}

for i in data['1']:
    for j in data['2']:
        print(i + j)


# ✅ Question 2
# Find the highest 3 values of corresponding keys in a dictionary.
data = {'a': 45, 'b': 12, 'c': 78, 'd': 23, 'e': 90}

sorted_values = sorted(data.values(), reverse=True)
print("Highest 3 values:", sorted_values[:3])
