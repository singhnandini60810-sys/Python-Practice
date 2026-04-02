# ================= PROGRAM 1 =================
# Convert tuple of integers into a single integer

t = tuple(map(int, input("Enter elements: ").split()))
result = 0
for i in t:
    result = int(str(result) + str(i))
print(result)


# ================= PROGRAM 2 =================
# Sum of elements of each tuple in list

n = int(input("Enter number of tuples: "))
lst = []
for i in range(n):
    t = tuple(map(int, input().split()))
    lst.append(t)

result = []
for t in lst:
    s = 0
    for i in t:
        s += i
    result.append(s)
print(result)


# ================= PROGRAM 3 =================
# Convert list of tuples to list of lists

n = int(input("Enter number of tuples: "))
lst = []
for i in range(n):
    t = tuple(map(int, input().split()))
    lst.append(t)

result = []
for t in lst:
    result.append(list(t))
print(result)


# ================= PROGRAM 4 =================
# Find items starting with specific character

lst = input().split()
ch = input()

result = []
for item in lst:
    if item[0] == ch:
        result.append(item)
print(result)


# ================= PROGRAM 5 =================
# Remove consecutive duplicates

lst = list(map(int, input().split()))
result = []
for i in lst:
    if len(result) == 0 or i != result[-1]:
        result.append(i)
print(result)


# ================= PROGRAM 6 =================
# Difference between consecutive numbers

lst = list(map(int, input().split()))
diff = []
for i in range(1, len(lst)):
    diff.append(lst[i] - lst[i-1])
print(diff)


# ================= PROGRAM 7 =================
# Frequency of dictionary values

n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

freq = {}
for v in d.values():
    freq[v] = freq.get(v, 0) + 1
print(freq)


# ================= PROGRAM 8 =================
# Combine dictionaries with list of values

n = int(input())
dicts = []
for i in range(n):
    temp = {}
    m = int(input())
    for j in range(m):
        k = input()
        v = input()
        if v.isdigit():
            v = int(v)
        temp[k] = v
    dicts.append(temp)

combined = {}
for d in dicts:
    for k, v in d.items():
        if k in combined:
            combined[k].append(v)
        else:
            combined[k] = [v]
print(combined)


# ================= PROGRAM 9 =================
# Key of max and min value

n = int(input())
d = {}
for i in range(n):
    k = input()
    v = int(input())
    d[k] = v

max_key = max(d, key=d.get)
min_key = min(d, key=d.get)
print(max_key, min_key)


# ================= PROGRAM 10 =================
# Student class

class Student:
    def __init__(self):
        self.name = ""
        self.roll = ""
        self.marks = 0

    def input(self):
        self.name = input()
        self.roll = input()
        self.marks = float(input())

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 75:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

    def display(self):
        print(self.name, self.roll, self.marks, self.grade())

s = Student()
s.input()
s.display()


# ================= PROGRAM 11 =================
# BankAccount class

class BankAccount:
    def __init__(self):
        self.name = ""
        self.balance = 0

    def input(self):
        self.name = input()
        self.balance = float(input())

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt

    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance -= amt

    def display(self):
        print(self.name, self.balance)

a = BankAccount()
a.input()
a.deposit(float(input()))
a.withdraw(float(input()))
a.display()


# ================= PROGRAM 12 =================
# Book class

class Book:
    def __init__(self, t, a, p):
        self.title = t
        self.author = a
        self.price = p

    def discount(self, d):
        self.price -= (d/100)*self.price

    def display(self):
        print(self.title, self.author, self.price)

b = Book(input(), input(), float(input()))
b.display()
b.discount(float(input()))
b.display()


# ================= PROGRAM 13 =================
# Polymorphism (Shape)

import math

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w

class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

r = Rectangle(float(input()), float(input()))
print(r.area())

c = Circle(float(input()))
print(c.area())


# ================= PROGRAM 14 =================
# Random string

import random, string
print(''.join(random.choices(string.ascii_letters + string.digits, k=5)))


# ================= PROGRAM 15 =================
# OTP

import random
print(''.join(str(random.randint(0,9)) for _ in range(6)))


# ================= PROGRAM 16 =================
# Fixed dice

import random
random.seed(1)
print(random.randint(1,6))


# ================= PROGRAM 17 =================
# Password

import random
u="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l="abcdefghijklmnopqrstuvwxyz"
d="0123456789"
s="!@#$%^&*()"

p = random.choices(u,k=2)+[random.choice(d)]+[random.choice(s)]
p += random.choices(u+l+d+s,k=6)
random.shuffle(p)
print(''.join(p))


# ================= PROGRAM 18 =================
# List to integer

n=int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))

res=""
for i in lst:
    res+=str(i)
print(int(res))


# ================= PROGRAM 19 =================
# Sort digits ascending

num=input()
digits=list(num)
digits.sort()
print(''.join(digits))


# ================= PROGRAM 20 =================
# ATM

card=input()
pin=input()
bal=0

if input()==card and input()==pin:
    while True:
        ch=input()
        if ch=='a':
            print(bal)
        elif ch=='b':
            pin=input()
        elif ch=='c':
            amt=int(input())
            if amt<=bal and amt<=10000:
                bal-=amt
        elif ch=='d':
            amt=int(input())
            if amt%100==0:
                bal+=amt
        elif ch=='e':
            break


# ================= PROGRAM 21 =================
# Hash display

def hash_display():
    try:
        f=open("matter.txt")
        print('#'.join(f.read()))
        f.close()
    except:
        print("Error")

hash_display()


# ================= PROGRAM 22 =================
# J to I

def JTOI():
    try:
        f=open("WORDS.TXT")
        print(f.read().replace('J','I'))
        f.close()
    except:
        print("Error")

JTOI()


# ================= PROGRAM 23 =================
# String status

s=input()
v="aeiouAEIOU"
uc=vc=cc=sc=sp=0

for ch in s:
    if ch.isupper(): uc+=1
    if ch in v: vc+=1
    elif ch.isalpha(): cc+=1
    elif ch.isspace(): sp+=1
    elif not ch.isalnum(): sc+=1

print(uc,vc,cc,sp,sc)


# ================= PROGRAM 24 =================
# Polygon

class Rectangle:
    def area(self):
        l=float(input())
        w=float(input())
        print(l*w)

class Triangle:
    def area(self):
        b=float(input())
        h=float(input())
        print(0.5*b*h)

while True:
    ch=input()
    if ch=='1':
        Rectangle().area()
    elif ch=='2':
        Triangle().area()
    else:
        break


# ================= PROGRAM 25 =================
# Filter words

words=input().split()
chars=input().split()

res=[]
for w in words:
    if not any(c in w for c in chars):
        res.append(w)
print(res)


# ================= PROGRAM 26 =================
# Largest string with consonant

words=input().split()
v="aeiouAEIOU"
largest=""

for w in words:
    if any(ch not in v and ch.isalpha() for ch in w):
        if len(w)>len(largest):
            largest=w
print(largest)


# ================= PROGRAM 27 =================
# Combinations

d={}
n=int(input())
for i in range(n):
    k=input()
    d[k]=input().split()

l=list(d.values())
for i in l[0]:
    for j in l[1]:
        print(i+j)


# ================= PROGRAM 28 =================
# Replace RED with GREEN

s=input()
res=""
i=0

while i<len(s):
    if s[i:i+3]=="RED":
        res+="GREEN"
        i+=3
    else:
        res+=s[i]
        i+=1

print(res)
