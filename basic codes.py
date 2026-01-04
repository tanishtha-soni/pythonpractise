print("Hello World!")


a = int(input("enter first number:"))
b = int(input("Enter second number:"))
print("Sum =", a + b)


x = float(input("Enter first number:"))
y = float(input("Enter second number:"))
print("Product =" , x * y)


ch = input("Enter a character:")
print("ASCII value =", ord(ch))


import sys
a = 10
b = 10.5
c = "Python"
d = True
print("Integer:" , sys.getsizeof(a))
print("Float:", sys.getsizeof(b))
print("String:", sys.getsizeof(c))
print("Boolean:", sys.getsizeof(d))


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
temp = a
a = b
b = temp
print("After swapping:")
print("a =", a)
print("b =", b)


n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


ch = input("Enter a character: ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third  number: "))
if a > b and a> c:
    print("Largest =", a)
elif b > c:
    print("Largest =", b)
else:
    print("largest =", c)


    year =  int(input("Enter a year: "))
    if year % 400 == 0:
      print("Leap year")
    else:

      print("Not a leap year")


n = int(input("Enter a number:"))
if n > 0:
    print("Positive number")
elif n < 0:
    print("Negative number")
else:
    print("Zero")


ch = input("Enter a character:")
if ch.isalpha():
    print("Alphabet")
else: 
    print("Not  an alphabet")


    n = int(input("Enter n: "))
    sum = n * (n + 1) // 2
    print("Sum =", sum)



    n = int(input("Enter a number:"))
    fact = 1
    for i in range (1, n + 1):
        fact = fact * i
        print("Factorial =", fact)


        n = int(input("Enter number of terms:"))
        a, b = 0, 1
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b



a = int(input("Enter first number: "))
b = int(input("Enter second number"))
while b != 0:
    a, b = b, a % b
    print("GCD =", a)



a = int(input("ENTER FIRST NUMBER:"))
b = int(input("ENTER SECOND NUMBER"))
lcm = (a * b) // __import__('math').gcd(a, b)
print("LCM =", lcm)


for i in range(65, 91):
    print(chr(i), end=" ")


    n = int(input("Enter a number: "))
    count = 0
    while n != 0:
        count += 1
        n //= 10
        print("Number of digits =" , count)














