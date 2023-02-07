
# --- tute week 5 ----
# Exercises
# 1. (a) What happens when a function returns? What happens if the function was called from inside a
# complicated expression, as in i = 5 * (2 + min(3, 4))?
# - i = 25
#
# (b) Is it possible for a function to call another function? Why would this be a useful feature?
# How does Python keep track of all the work in progress?
# - yes a function can call another function
#
# (c) Is it possible for a function to call itself ? What is the name for this feature? What happens to the
# private variables of the function in this case?
# - yes a function can call itself - this is called a recursion. for example:
# def countdown (i):
#     if i == 1:
#         print (1)
#     else:
#         print (i)
#         countdown (i-1)
# countdown(7)
#
# - print and return are diff: print prints it out a return sends it back
# def countdown (i):
#     return (i-2)
# i = countdown(7)
#
# (d) What happens if you try to use return in your main program rather than in a function? Would this
# be a ‘syntax’ or a ‘run-time’ error?
# - you would get a syntax error!
#
# 2. Given the string x = ’Tqbfjotld’, or equivalently the list with the same elements in longer form, x =
# [’The’, ’quick’, ’brown’, ’fox’, ’jumps’, ’over’, ’the’, ’lazy’, ’dog’]:
# (a) Suppose I use the slice x[a:b:c]. What are meaning of the a, b, c? What happens when each
# of these is (i) positive or 0, (ii) negative, or (iii) missing?
# ### list[start:end:step]
# (i) positive = read left to right
# (ii) negative = read right to left
# (iii) if a is missing - presume it = index 0, if b is missing presume it means last position of array, if c is missing presume it = 1.
#
# x = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# print(x[1:5:1])
# # quick brown fox jumps
# print(x[5:1:-1])
# # over jumps fox brown
# print(x[:1:1])
#
# (b) Reverse the string (or list) using slicing. Use Python’s default behaviour to make the slice notation
# as compact as possible. Why and how does this work?
# ans -> print(x[::-1])
# (c) Repeat part 2b but this time exclude the first and last characters. Thus for x = ’Tqbfjotld’ we
# would get ’ltojfbq’ and equivalently for the list version of the problem.
# x = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# #       0       1       2       3        4      5       6       7       8
# print(x[7:0:-1])
# print(x[-2:0:-1])
# print(x[-2:-9:-1])
# 3. Suppose we have a list containing floats, such as prices = [137.10, 72.0, 1.015].
# (a) How to use str.format() to print these items right-aligned on separate lines so that there are 4
# digits, a decimal point, and then 2 digits?
#
# prices = [137.10, 72.7, 1.015]
# s = " is the price"
# for price in prices:
#     print("{0:7.2f} {1}".format(price, s))
# # the f stands for floating point number
#
# (b) Repeat part 3a, but this time do not use str.format() or similar functions. Instead, format the
# strings according to the following algorithm:
#
# i. Multiply the price by 100.0 to get the price into cents;
# ii. Use round() to get the price into whole cents;
# iii. Convert the rounded price from a float to an int;
# iv. Use str() to obtain a string representing the cents;
# v. Put leading zeros onto the string until its length is at least 3;
# vi. Put leading spaces onto the string until its length is at least 6;
# vii. Print all but the last 2 characters, then a ’.’, then the rest.
#
# (c) How to modify your solution to part 3b to handle negative numbers?
# # add an absolute value commandline
#
# for price in prices:
#         price *= 100  #this is the same as price = price * 100
#         price = round(price)
#         price = abs(price)          # why does this line have to go here?
#         price = int(price)
#         price = str(price)
#         while len(price) < 3:
#             price = "0" + price
#         while len(price) > 6:           # this one doesn't make sense to me
#             price = " " + price
#         print(price[:-2] + "." + price[-2:])
#         print(price)
#
# 4. Given a really large int, such as num = 123000000000000000000:
# (a) Design a program to print the int in an exponential format as an integer without trailing zeros, an
# ’e’, then a count of how many trailing zeros there would be. Produce your output using print()
# without worrying too much about the exact formatting.
#
# num = 123000000000000000000
# exp = 0
# num = str(num)
# while num[-1] == '0':
#     exp += 1 # same as exp = exp + 1
#     num = num[:-1]
#     print(num, "e+", exp)
#
# 5. The for statement repeats a block of statements, where usually you use range to tell how many repeats
# you want. Use for i in range(...) to write the following programs:
#
# (a) Print out three cheers, that is, print Hip hip, hooray three times on separate lines.
# cheer = "hip, hip, hooray"
# for i in range(3):
#     print(cheer)
#
# # (b) Print the counting numbers 1, 2, . . . , 10, each on a separate line. Hint: use the loop counter i.
# for g in range(1, 11):
#     print(g)
#
# # (c) Roll 2 dice, printing each die roll on a separate line. Then on a third line, print their sum (between
# # 2 and 12 inclusive). Use random.randint(), and you are not allowed multiple call sites!
# import random
# total = 0
# for j in range(2):
#     roll = random.randint(1,6)
#     print(roll)
#     total = total + roll
# print(total)
#
# 6. Next, we will try some methods. Methods are functions, except that they are attached to something,
# e.g. a string. So we first give the owner of the method, then a period (.), and then the function call, with
# any arguments separated by commas (,) as usual. What do these do?
# (a) ’hello’.capitalize()
# print("hello world".capitalize())
# (b) ’hello’.index(’e’)
# print("hello world".index('e'))
