
""" Question 5a: Write a program to report how many characters are in each of the user’s first name and last name,
given the user types it like Firstname Lastname."""
# # myName = input('Please input your name: ')
# myName = 'Jane-August Austine'
# n = myName.index(" ")
# print("Your first name has", n, "characters")
# print("Your last name has", len(myName) - n - 1, "characters")


""" Question 5b: Write a program to determine (i) how many characters are in the
 user’s first name, then (ii) based on this number of characters, whether the 
 first name is hyphenated."""
# hyphen = myName.find('-')
# print('pp', hyphen)
# if hyphen < n:
#     print("First name is hyphenated")
# else:
#     print("First name is not hyphenated")
#
# if hyphen > n:
#     print("Last name is hyphenated")
# else:
#     print("Last name is not hyphenated")

""" Question 5c: Write a program to determine (i) how many characters are in the 
user’s first name, then (ii) based on this, whether the last name is hyphenated. 
Hint: Consider all possible inputs carefully!"""
# Question 5b+c
# hy = myName.index("-", n+1) #this could also be hy = myName.find("-", n+1, len(myname)-1)
# if (hy > n):
#     print("last name is hyphenated")
# else:
#     print("Last name is not hyphenated")

""" Question 5d: Assuming the user types either one or two or three words, that is either Lastname or Firstname
Lastname or Firstname Middlename Lastname or Mr/s Firstname Lastname), determine
where the last name begins and use this to check whether the last name is hyphenated. Hint: There
are a finite number of cases to consider, how can you distinguish them?"""
# myName = input('Please input your name: ')
myName = 'Jane Saint August-D'
n = myName.find(" ")
if (n == -1):
    st = 0
else:
    ss = myName.find(" ", n+1)
    if (ss == -1):
        st = n+1
    else:
        st = ss + 1
hy = myName.find("-", st)  # this could also be hy = myName.find("-", n+1, len(myname)-1)
if (hy > st):
    print("Last name is hyphenated")
else:
    print("Last name is not hyphenated")
"""An elif statement can be used here instead of the if else under else."""

# Question 6b - 6e
# print(ord('a'))
# # print(ord('aa')) --> error
# print(chr(97))
# print(chr(65))

"""Question 7: Given a variable num containing a float, write a program to calculate 
the number of digits in its printed form (including the exponent if it prints with 
one, and any .0 suffix added by Python to identify float numbers). Make sure your 
code can handle negative numbers."""
# Question 7 - Solution Method 1
# num = float(input("Enter a number: "))
# strnum = str(abs(num))
# digits = len(strnum)
# if '.' in strnum:
#     digits = digits - 1
# if 'e-' in strnum:
#     digits = digits - 2
# elif 'e+' in strnum:
#     digits = digits - 2
# print(num, digits)
#
# # Question 7 - Solution Method 2 - using isdigit() and for loop
# num = -6.0E10
# count = 0
# for element in str(num):
#     if element.isdigit():
#         count += 1
# print(count)
