# 2-D Lists
# L8 - slide 8 - collapse a 2d list into a 1D list
# twodlist = [[1,2,3,4,5], [6,7,8,9,10]]
# onedlist = []
#
# for lst in twodlist:
#     for item in lst:
#         onedlist.append(item)
#
# print(onedlist)

# the same can be achieved using list comprehensions:

# onedlist = [item for lst in twodlist for item in lst]
# print(onedlist)
#
# # How can tables be represented in python?
# headers = ["Product Name", "Quantity in Stock", "Price", "How Many Sold"]
# prod1 = ["Product1", 5, 45.5, 10]
# prod2 = ["Product2", 8, 10.2, 50]
# prod3 = ["Product3", 9, 6.4, 20]
# prod4 = ["Product4", 20, 8.6, 20]
# prod5 = ["Product5", 15, 10, 30]
# products = [headers, prod1, prod2, prod3, prod4, prod5]
# import pprint #pretty printer
# pprint.pprint(products)

# change the price of product 1 to $50 and change the quantity of Prod 3 to 10:
# products[1][2] = 50 #diff to lec notes
# products[3][1] = 10
# pprint.pprint(products)

# Print each Row
# for i in range(len(products)):
#     list_row = []
#     for j in range(len(products[i])):
#         list_row.append(products[i][j])
#     print('p1', list_row)
#
# # alternatively you can print the rows by:
# for product in products:
#     print('p2', product)
#
# # Print each Column as a list - notice you are just swapping i and j
# for i in range(len(products[0])):
#     list_column = []
#     for j in range(len(products)):
#         list_column.append(products[j][i])
#     print('p3', list_column)

# Exercise 1
"""A valid table is one where each row has the same number of 
columns. Write a function table_valid(), which takes as input 
a 2-D list (the list represents a table of the form 
[row1, row2, row3] and returns True or False) ==> in other words 
a table is only valid if each row has the same no. of elements. 
so there are the same no of columns."""

# def table_valid(table):
#     num_columns = len(table[0])
#     for row in table:
#         if len(row) != num_columns:
#             return False
#     return True

# Dictionaries, including Default Dict
# see slide 17-19 for other dict functions

"""Strings, numbers, and tuples work as keys, and any type can 
be a value. Other types may or may not work correctly as 
keys (strings and tuples work cleanly since they are immutable)"""
# eg of dict in dict: my_d = {"a":{"b": 2, "c": False}, "d":3.00}
# slide 23 Extracting info from dict

# Exercise 2
"""Write a function lookup_capital(), that receives 
as input one string (a country name) and 
returns the capital city of that country.

There will be a global dictionary called 
CAPITALS that contains a collection of country 
names as keys with their capital city as 
corresponding value."""

# CAPITALS = {'Australia': 'Canberra', 'Italy': 'Rome', 'England': 'London', 'China': 'Beijing'}
#
# def lookup_capital(country):
#     # global CAPITALS   # is this line of code necessary?
#     if country in CAPITALS:
#         return CAPITALS[country]
#     else:
#         return "I don't know that capital"
#
# print(lookup_capital("Greece"))
# print(lookup_capital("Australia"))


# Exercise 3 [similar to exercise 3 from lecture 7]
"""Write a function word_count2() that takes as 
input a string of text and returns a dictionary 
containing an occurrence count for each word 
in the text."""

#
# def word_count(text):
#     pure_text = ''
#     for x in text:
#         if x.isalpha() or x.isnumeric() or x == " ":
#             pure_text += x
#     # print(pure_text)
#
#     pure_lst = pure_text.split()
#     my_dict = {}
#     for word in pure_lst:
#         if word in my_dict:
#             my_dict[word] += 1
#         else:
#             my_dict[word] = 1
#     return my_dict
#
#
# text = "one thousand two thousand three thousand four thousand one"
#
# print(word_count(text))

# alternatively you can use defaultdict

# from collections import defaultdict
#
#
# def word_counter(text):
#     wd_count = defaultdict(int)  # default is the empty string ""
#
#     for word in text.split():
#         wd_count[word] += 1
#     return wd_count
#
#
# print(word_counter(text))
# print(dict(word_counter(text)))
#
#
# def count_digits(num):
#     """count the occurrences of individual digits in a number"""
#     digit_count = defaultdict(int)  # default is the integer 0
#     for digit in str(num):
#         digit_count[digit] += 1
#     return digit_count
#
#
# print(count_digits(134313452346))
# print(dict(count_digits(134313452346)))

# Sets
# Exercise 4
"""Given two sets, their symmetric difference is 
the set of elements that belong to either one or 
the other set but not both. so, S1 + s2 - intersection
Write a function symmetric_difference(), that 
takes two sets as input and returns the set that 
is their symmetric difference."""


# def symmetric_difference(s1, s2):
#     symmetric_diff = s1.union(s2) - s1.intersection(s2)
#     sym_diff = len(s1.difference(s2)) + len(s2.difference(s1))
#     return symmetric_diff, sym_diff
#
#
# s1 = {0, 1, 2, 3, 4}
# s2 = {4, 5, 6, 7, 8}
# print(symmetric_difference(set(s1), set(s2)))

# alternatively you can write all the methods out like this as well!

def symmetric_difference(s1, s2):
    symmetric_diff = len((s1 | s2) - (s1 & s2))
    sym_diff = (len(s1 - s2) + len(s2 - s1))
    return symmetric_diff, sym_diff


s1 = {0, 1, 2, 3, 4}
s2 = {4, 5, 6, 7, 8}
print(symmetric_difference(set(s1), set(s2)))

# Lecture 8 Challenge 1
"""Write a function swap_dict(), which takes 
one dictionary as input and returns another 
dictionary resulting from swapping the keys 
and values around. For example, if the input 
is {'a':1, 'b':2}, the output would be {1:'a', 
2:'b'}."""

def swap_dict(d):
    pairs = d.items()
    print(pairs)
    new_dict = {}
    for pair in pairs:
        new_dict[pair[1]] = pair[0]
    return new_dict

d = {1:'a', 'b':2}
print(swap_dict(d))

# Lecture 8 Challenge 2
"""Write a function cartesian_product(), which 
takes two sets, A and B, as inputs. The 
function then returns the Cartesian product 
(x) of A and B. For example, if A = {1,2} and 
B = {3,4}, then A x B = {(1,3), (1,4), (2,3), 
(2,4)}"""


# def cartesian_product(set1, set2):
#     product = set()
#     for item1 in set1:
#         print(item1)
#         for item2 in set2:
#             print(item2)
#             product.add((item1, item2))
#     return product


# A = {1, 2}
# B = {3, 4}
# print(cartesian_product(A, B))

# note the resulting product is unordered because it's a set
