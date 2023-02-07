### Lecture 2 Homework Problems:
## 1) Take four numbers from user input and print their mean (average) value.
# num_one = int(input("Enter a number here: "))
# num_two = int(input("Enter a number here: "))
# num_three = int(input("Enter a number here: "))
# num_four = int(input("Enter a number here: "))
# average = (num_one + num_two + num_three + num_four) / 4
# print(average)

## 2) Take three digits (0-9) from user input and print all possible combinations of the digits.
# num_one = int(input("Enter a number here:"))
# num_two = int(input("Enter a number here: "))
# num_three = int(input("Enter a number here: "))
# print(num_one, num_two, num_three)
# print(num_one, num_three, num_two)
# print(num_two, num_three, num_one)
# print(num_two, num_one, num_three)
# print(num_three, num_one, num_two)
# print(num_three, num_two, num_one)

## 3) Take two numbers from the user, the length of a rectangle and its height (in centimeters),
# then calculate and print out both the total perimeter of the rectangle and the area.
# length = int(input("Enter a number here: "))
# height = int(input("Enter a number here: "))
# perimeter = (2 * length) + (2 * height)
# area = length * height
# print("The perimeter is " + str(perimeter) + "cm.")
# print("The area is " + str(area) + "cm^2.")

print(int(34.56))
# 34
print(int(1.75))
# 1
print(int(-1.75))
# -1
# print(int('3.45'))
# ValueError: invalid literal for int() with base 10: '3.45'
print(str(34.56))
# '34.56'
print(str(10))
print(float(4))
print(float('3.45'))
# print(float('abc'))
# ValueError: could not convert string to float: 'abc'
print(bool(1))
print(bool(0))
print(bool('True'))
print(bool('False'))  #  **TRUE!!!!
print(bool(7))
print(bool(""))
print(bool(None))

print(chr(107))
print(ord('H'))
print(chr(ord('Q') + 4 ))
print(chr(8712))