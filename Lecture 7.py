"""Exercise 1 Write a function middle() that returns the middle
element(s) from a given input list:"""

# def middle(lst):
#     len_list = len(lst)
#     if len_list % 2 == 0:
#         return lst[int(len_list / 2) - 1:int(len_list / 2) + 1]
#     else:
#         return lst[len_list // 2]
#
# # 5 / 2 = 2.5
# # 5 // 2 = 2
#
# print(middle([1, 2, 3, 4, 5, 6]))
import collections

"""Instead of going through the list with a for loop to double each element in a list
you can use list comprehension. :list comprehension example: double all elements in list: """

# lst1 = [1, 2, 3, 4]
# lst1_duplication = [item for item in lst1]
# print(lst1)
# lst2 = [(item * 2) for item in lst1]
# print(lst2)

# NOTES:
'you can add conditionals to list comprehensions = range(), %, ==,  in side '
# examples:
# number_lst = [x for x in range(21)]
# print(number_lst)
#
# number_lst_even = [x for x in range(21) if x % 2 == 0]
# print(number_lst_even)

"""Exercise 2: Write a function palindromes() that receives a list of string as
input and prints a list of all those strings which are palindromes using list
comprehension (a palindrome is a word that is the same in reverse order, eg: "dad")."""

# def palindromes(lst):
#     palindromes_list = [x for x in lst if x == x[::-1]]
#     print(palindromes_list)
#
# palindromes(['dad', 'hello', 'goodbye', 'mum', 'rotator'])

"""OBJECT IDENTITIY - 45 MINS INTO LEC
MUTABILITY - 47 MINS INTO LEC - when you try to print a mutable list which might
have been redifned in a local
setting globally then it will print the global definition.
HOWEVER IF YOU CHANGE ONE ITEM IN THE LIST LOCALLY THEN TRY OT PRINT IT
GLOBALLY IT WILL PRINT THE OUTPUT WILL BE THE LOCALLY CHANGED LIST"""

# code from L7 Slide 21
# copying using the equals assignment [where two things point to one thing]
# old_list = [1, 2, 3, 4, 'a']
# new_list = old_list
# new_list[4] = 5
# new_list.append(6)

# print() # spacer
# print('p1', 'old_list:', old_list)
# print('ID of old_list:', id(old_list))
# print() # spacer
# print('new_list:', new_list)
# print('ID of new_list:', id(new_list))

# copying using the copy method (true copy)
import copy

# old_list = [1, 2, 3, 4]
# new_list = copy.copy(old_list)
# old_list[3] = 'four'
# new_list.append(5)

# print() # spacer
# print('p2', "old_list:", old_list)
# print(id(old_list))
# print() # spacer
# print("new_list:", new_list)
# print(id(new_list))


# L7 slide 23
"""here note how the 123 changes to 321 for old list only and 'four' 
changes to 4 for both old and new list even though we only asked for it 
to be changed in the new list!"""
# old_list = [123, ['four', 5, 6], [7, 8, 9]]
# new_list = copy.copy(old_list) # this is same as new_list = old_list[:]
# old_list.append([10])
# new_list.append([11])
# old_list[1][0] = 4
# old_list[0] = 321
#
# print("old_list:", old_list)
# print(id(old_list))
# print()
# print("new_list:", new_list)
# print(id(new_list))
# print()

# NOTE: comment out the code above before running the code below!
# L7 slide 24:To ensure all items, even mutable ones are completely duplicated
old_list = [123, ['four', 5, 6], [7, 8, 9]]
new_list = copy.deepcopy(old_list)
old_list.append([10])
new_list.append([11])
old_list[1][0] = 4
old_list[0] = 321
print("old_list:", old_list)
print(id(old_list))
print()
print("new_list:", new_list)
print(id(new_list))

# Exercise 3:
"""write a function word count that takes as input a string of text
and a word and returns the number of times that word appears in the text."""


def word_count(text, word):
    pure_text = ''
    for x in text:
        if x.isalpha() or x.isnumeric() or x == " ":
            pure_text += x
    print(pure_text)

    count = 0
    for y in pure_text.split():
        if y == word:
            count += 1
    return count


text = "one thousand two thousand three thousand four thousand one"
print(word_count(text, "thousand"))

# L7 Challange 1
'''Write a function that de-vowels and returns an input string using list comprehension.
Note that you will want to convert the input string to a list to do this, 
then reconstruct the de-voweled string from the list comprehension result before 
returning it.'''
# list comprehension form:
output1 = ''.join([x for x in text if x not in 'aeiou'])
print(output1)

# same code in normal form
output = ''
for x in text:
    if x not in 'aeiou':
        output += x
print(output)

# L7 Challange 2
'''Write a function that takes one tuple as input, returning 
True if all tuple items are of the same type, and False otherwise.'''


def tupp_checker(inputt):
    for i in range(len(inputt) - 1):
        if type(tupp[i]) != type(tupp[i + 1]):
            return False
    return True


# tupp = (1, '2', 3.0, [9, 10], True)
tupp = (1, 2, 4, 6, 7)
print(tupp_checker(tupp))

# L7 slide 40: Exception handling example 1:
# while True:
#     try:
#         x = int(input("Enter a number: "))
#         break
#     except ValueError:
#         print("Try again")

# L7 slide 41: Exception handling example 2:
try:
    x = 0
    y = 5
    # a = b
    # print(y/x)
    lst = [1, 2, 3]
    print(lst[5])
except ZeroDivisionError:
    print("You cannot divide by zero")
except IndexError:
    print("Item must exist at index")
except:
    print("Some other error")
