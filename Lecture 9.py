
# NOTES
# how to open a file:
# Default (read): file_object = open("filename.txt")
# To read from: file_object = open("filename.txt", "r")
# to write to: file_object = open("filename.txt", "w")
# To add data to (append): file_object = open("filename.txt", "a")
#
# how to close a file: file_pointer.close()

# the rstrip function:

# Exercise 1:
"""Given a file of tram stops and their routes, print a list of
routes for each stop. Each line of the file has two
comma-separated values, the stop and then the route.

For example:
Tennis Centre,3
Tennis Centre,38
Aquarium,38
Docklands,3

With this sample, Route 38 stops at both the Tennis
Centre and Aquarium. The Tennis Centre has two
routes (3 and 38) passing through it.

Hint: split() method and rstrip() methods may be useful
"""
from collections import defaultdict as dd

filename = 'Lecture  9_stops_routes.txt'
stops_dict = dd(list)

for lines in open(filename).readlines():
    # strip the newline character
    lines = lines.rstrip('\n')
    line = lines.split(',')
    stops_dict[line[0]].append(line[1])

print(stops_dict)


""" Exercise 2: Write code that opens 
Lecture 9_rainfall.csv and prints out the 
maximum rainfall record value"""

import csv
filename = 'Lecture 9_rainfall.csv'


def max_rainfall(data):
    max_rain = None

    for row in data:
        rain = float(row["Rain_mm"])
        if max_rain == None or max_rain < rain:
            max_rain = rain
    return max_rain


data = csv.DictReader(open(filename))
max_rain = max_rainfall(data)

if not max_rain is None:
    print(f"The maximum rainfall from data was {max_rain}mm.")
else:
    print("The file does not contain any rainfall data.")

""" write csv """
import csv

data_2d = [['header1', 'header2', 'header3'], [1, 2, 3], [4, 5, 6]]
csv_file = open("2d-data.csv", "w", newline='')
writer = csv.writer(csv_file)
writer.writerows(data_2d)
csv_file.close()

# Exercise 3:
"""Write some code to return the 3 least used 
alphabetic characters from a string variable 
named text. Ties should be broken 
alphabetically; for example, if ‘a’ and ‘b’ 
appeared the same number of times, ‘a’ would 
be returned before ‘b'"""

from collections import defaultdict as dd
import pprint


def char_freq(text):
 # count chars in text & store in a dictionary
    freq_char = dd(int)
    for c in text:
        if c.isalpha():
            freq_char[c.lower()] += 1
    return freq_char


def least_3_char(text):
    # get char counts
    char_counts = char_freq(text)
    print('(a)', char_counts)   #this prints default dict
    #or can print using pprint
    pprint.pprint(dict(char_counts))
    key_value_pairs = [pair for pair in char_counts.items()]
    print('(c)', key_value_pairs)
    # create list sorted by counts
    ordered_char = sorted([(v, k) for k, v in char_counts.items()])
    # return first three chars in list
    return [c[1] for c in ordered_char[:3]]


text = "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, the design philosophy of Python emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects."
print('(d)', least_3_char(text))


# How to write Recursive functions [i.e. factorials,  ]

"""RECURSION EXAMPLES"""

"""factorial"""


def factorial(n):
    # base case
    if n == 1:
        return 1

    # recursive case
    return n * factorial(n-1)


def factorial_iteration(n):
    # base case
    factoriall = 1

    # loop down from the input number until 1
    for number in range(n, 1, -1):
        # multiply current number with produce of previous numbers
        factoriall = factoriall * number
    return factoriall


"""calculate max num of list"""

# calcultes the max num of list


def recursion_max(my_list, curr_max=0):
    # check to see if we've reached the end of the list
    if my_list == []:
        return curr_max
    # check to see if current head element is greater than the current max
    elif my_list[0] > curr_max:
        return recursion_max(my_list[1:], my_list[0])
    # head element isn’t greater than `curr_max` so check rest of my_list
    else:
        return recursion_max(my_list[1:], curr_max)


"""calculate the second max of list"""

# Exercise 4:
"""• The Fibonacci Sequence is the series of 
numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
• Starting with 0 and 1, the next number is 
found by adding up the two numbers before 
it.
• Write a recursive function that accepts one 
input argument, an integer n, and returns the 
n
th Fibonacci number. If n = 0 then return 0, 
the 0th number, if n = 1 then return 1, the 1st
number, and if n = 2, then return 1, which is 
also the 2nd number"""
#iterative way


def fibonacci(n):

    fib_lst = [0, 1]
    if n in fib_lst:
        return n

    for i in range(2, n+1):
        next_element = fib_lst[i-1] + fib_lst[i-2]
        fib_lst.append(next_element)

    return fib_lst[-1]


print(fibonacci(7))


#recursive method


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(7))

#iterative approach


def fib_iterative(n):
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    return b


# Lec 9 Challange 1:
"""Write a function file_compare(file1, file2), 
which receives the path names of two files 
and checks whether they have identical 
content. If they do not have identical content, 
then append the content of file2 to file1"""


def file_compare(file1, file2):
    file_object1 = open(file1, "r")
    file_object2 = open(file2, "r")

    text1 = file_object1.read()
    text2 = file_object2.read()

    file_object1.close()
    file_object2.close()

    if text1 != text2:
        file_object1 = open(file1, "a")
        file_object1.write('\n' + text2)
        file_object1.close()


file_1 = 'Lecture 9_file1.txt'
file_2 = 'Lecture 9_file2.txt'
file_compare(file_1, file_2)

# Lec 9 Challange 2:
"""Write a recursive function sum_nums(n) that 
accepts an integer n and returns the sum of 
integers from 1 to n."""


def sum_nums(n):
    if n == 1:
        return 1
    return n + sum_nums(n - 1)


print(sum_nums(6))

# Lec 9 Challange 3:
"""Write a recursive function reverse(string), 
that accepts a string input and returns that 
string in reverse order"""


def reverse(string):
    if string == '':
        return string

    else:
        return reverse(string[1:]) + string[0]


print('anssss', reverse("Hello World!"))

# my Question is that - why can't we just do this instead:


def reverse(string):
    reversed_s = string[::-1]
    return reversed_s


print('anssss', reverse("Hello World!"))
