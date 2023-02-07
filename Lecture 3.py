# Lecture 3 Homework Problems:
# 1) Write code to determine if a given number x is even.
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("This number is even!")
# else:
#     print("This number is not even!")

## 2) Write code to calculate the ceiling of a given number x, without using math.ceil().
# x = 5.9
# if float(x) == int(x):
#     print(int(x))
# else:
#     print(int(x + 1))
#
## 3) Write code to calculate the area of a circle with a given radius r.
# import math
# radius = float(input("Enter a radius: "))
# area_of_circle = math.pi * (r ** 2)
# print(area_of_circle)

print(abs(7))
print(abs(-7))
print(abs(-5.4))
print(abs(-True))
# abs("aaa") -> error
# len(22) -> error

import math
print(math.ceil(4))
print(math.ceil(5))
print(math.ceil(4.5))
print(math.ceil(4.7))

import datetime
print(dir(datetime))

print(dir(math))

x = datetime.datetime.now()
print(x)


# Exercise 2 Solution
# num1 = int(input("Input first number: "))
# num2 = int(input("Input second number: "))
num1 = 60
num2 = 70

if num1 >= num2:
#nested if
    if num1 == num2:
        max_num = min_num = num1
#nested else
    else:
        max_num = num1
        min_num = num2
else:
    max_num = num2
    min_num = num1
print("Max is " + str(max_num))
print("Min is " + str(min_num))

# Exercise 3 Solution
"""Leap years have 29 days in feb instead of 28. Evaluate whether a given 
year expressed as an int(yyy) is a leap year. The rules for determining leap years: 
1. with the exception of century years (years ending with 00) all years divisible 
    by 4 are leap years)
2. a century year is a leap year if and only if it is divisible by 400."""

year = 2000
if year % 400 == 0:
    print('{} is a century leap year'.format(year))
elif year % 100 == 0:                                       #SMART!
    print('{} is a century not a leap year'.format(year))
elif year % 4 == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is a not a leap year'.format(year))

# ---- simplifying the above code to just an if else statement
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is a not a leap year'.format(year))
