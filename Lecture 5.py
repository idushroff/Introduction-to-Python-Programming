# Lecture 5 Exercise 2:
# Write a function that takes two arguments: a block of text and a word.
# The function should return True if the word is found in the text, otherwise false.
# Note: Only exact matches should return True. For eg: "sub" is not found exactly in "There are substrings".
# def is_word_in_text (word, text):
#     if ' ' + word + ' ' in text:
#         return True
#     if word + ' ' in text and text.startwith(word):
#         return True
#     if ' ' + word in text and text.endwith(word):
#         return True
#     return False
# if you don't want everything to be case-sensitive then change everything to upper or lower case

# Lec 5 challenges:
# 1) Write a function ascii_match(), which accepts two required input arguments, an integer and a string.
# If the ASCII numbers of all the characters in the string add up to the value of the input integer, return True.
# Otherwise, return False."""
# def ascii_match(integer, string):
#     ord_sum = 0
#
#     for char in string:
#         ord_sum = ord_sum + ord(char)
#
#     if ord_sum == integer:
#         return True
#     else:
#         return False
#
# # Python ord() function returns the Unicode code from a given character
# print(ascii_match(197, "ad")) # True
# print(ascii_match(197, "aa")) # False
# print(ord('d')) # d = 100
# print(ord('a')) # a = 97
# print(97+97) # 194


# 2) Write a function avg_three() that returns the average (mean) of three integers between 1 and 9.
# The function should allow for three optional input arguments (num1, num2,  num3) but if any of these arguments
# is not provided when the function is called, then a random number is generated for that value.
# See w3 schools for how to generate random integers.
# def avg_three(num1=None, num2=None, num3=None):
#     import random
#     if num1 is None:
#         num1 = random.randint(1, 9)
#     if num2 is None:
#         num2 = random.randint(1, 9)
#     if num3 is None:
#         num3 = random.randint(1, 9)
#
#     return (num1 + num2 + num3) / 3

# print(avg_three())


# future udi tries to solve lec 5 challenge 1
# def ascii_match(int1, string2):
#     count = 0
#     for char in string2:
#         count += ord(char)
#     print(count)
#     if count == int1:
#         return True
#     return False
#
# int1 = 76
# string2 = 'hi how are'
# print(ascii_match(int1, string2))
# #code below if for testing purposes
# for char in string2:
#     print(ord(char), end=' + ')

# future udi tries to solve lec 5 challenge 2
import random

def avg_three(num1, num2, num3):
    if num1 is None:
       num1 =  random.randint(1, 9)
    if num2 is None:
        num2 = random.randint(1, 9)
    if num3 is None:
       num3 =  random.randint(1, 9)
    else:
        mean = (num1 + num2 + num3)/ 3
        return mean

print(avg_three(3,4,5))
