# --Tute 7 Week 7---

"""Q1b"""
# squares = [0, 1, 4, 9, 16, 25, 36, 49]
# for i in squares:
#     print(squares.index(i), i)

# their solution:
# for i in range(5):
#     print(i, squares[i])

"""Q2"""
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# print('{} is {} years old.'.format(name, age))

# alternative solution 1
# print(f'{name:s} is {age:d} years old.')  # d stands for decimal

# alternative solution 2
# print('{0:s} is {1:d} years old.'.format(name, age)) # 0 is the name and 1 is the age

"""Q3"""
amounts = [45.05, 137.02, 0.01]
for i in amounts:
    print('{:8.2f}'.format(i))
"""Here the {0:...} says we want to replace part of the string to be printed with a formatted version of
the 0th (first) argument to format. Then, the format specification 8.2f means it should be printed as a
float with a width of 8 characters total, and 2 digits after the decimal point."""

"""Q4a"""
while True:
    meal = input('What would you like to eat? ')
    if meal == 'sandwiches' or meal == 'chicken' or meal == 'rice':
        break
    print('We only have sandwiches, chicken or rice.')

"""Q4b"""
fries = input('Would you like fires with that?: ')
while fries != 'yes':
    fires = input('Would you like fires with that?: ')

"""Q5"""
"""Q6"""
"""Q7"""
"""Q8"""
"""Q9"""

