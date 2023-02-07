

"""Lecture 6 Exercise 1: Write a function is_pangram(s), which determines
 if an input string s is a
pangram and returns True or False accordingly. Recall that a pangram is a
string in which each alphabetical characters appear at least once."""

# def is_pangram(s):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for char in alphabet:
#         if char not in s.lower():
#             return False
#     return True
#
# print(is_pangram("The quick brown fox jumps over the lazy dog"))
#
# for i in range(3):
#     print(i)
#
# for l in range(3):
#     print(l, end=" ")
#
# for j in range(0, 10, 2):
#     print(j, end=" ")  ## Why do we have to write end=' '? - he explains 1hr 4 mins into lec
#
# print(type(range(0, 10)))  # tell me what type is ??
#
# print(range(0, 10)[2])  # give me what is at index 2 in this range
#
# for k in range(0, 10, -1):
#     print(k, end=" ")

"""Lecture 6 Exercise 2 The Fibonacci Sequence - 
Write a function that gets an integer n via input()
and using for loop generates a list with the first n Fibonacci numbers."""

# n = int(input("Number of elements in Fibonacci Series, n, (n>=2): "))
# fibonacci_list = [0,1] # initialize the list with starting elements: 0, 1
# # if n > 2: # this line is not needed b/c if n was less than 2 then the for loop would never take off
# for i in range(2, n):
#     next_element = fibonacci_list[i-1] + fibonacci_list[i-2]  # next element in series = sum of its previous two numbers
#     fibonacci_list.append(next_element)    # append the element to the series
# print(fibonacci_list)

"""you could condense the code into one line by doing this but the 
lecturer prefers the 2 lines because it looks neat."""
# for i in range(2, n):
#     fibonacci_list.append(fibonacci_list[i-1] + fibonacci_list[i-2])
# print(fibonacci_list)

# Lecture 6 - Nested for loops - example code that checks whether numbers
# between 1 and 10 are prime.

# for num in range(1, 11):
#     prime = True
#     for x in range(2, 5):
#         if not (num % x):
#             prime = False
#     if prime:
#         print(num, "is a prime")
#     else:
#         print(num, "is not a prime")
# a prime number is one that is only divisible by 1 and itself


"""Lecture 6 challenges:
1) Convert this code to a functionally equivalent piece of code that uses while 
loops instead of for loops. Original code:"""
n = int(input('enter a number: '))
for i in range(1, n+1):
    for j in range(1, n+1):
        print(i, j)
print("Good bye")
# answer:
n = int(input('enter a number: '))
i = 1
while i < n+1:
    while j < n+1:
        print(i, j)
        j = j + 1
    i = i + 1
print("Good bye")


"""2) Modify exercise 1 solution so that the function instead returns a 
list containing all characters that don't appear in the string. 
If the string is a pangram, then return an empty list."""

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    string = []
    for char in alphabet:
        if char not in s.lower():
            string.append(char)
    return string

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Something goes here"))
# lecturer's answer:

def is_pangram(s):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    dont_appear = []

    for char in alphabet:
        if char not in s.lower():
            dont_appear.append(char)

    return dont_appear

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Something goes here"))
print(is_pangram(""))

"""3) Write a program that uses a while loop to print out each individual 
character in a given string line by line."""
my_string = 'alsdhflkahsdfkahsd'
char_index = 0
while char_index < len(my_string):
    char = my_string[char_index]
    print(char)
    char_index += 1

#lecturer's answer
my_string = "asdfsdfsd"

i = 0
while i < len(my_string):
    print(my_string[i])
    i += 1

