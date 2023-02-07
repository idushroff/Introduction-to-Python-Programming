"""List comprehensions"""

"""to list numbers b/w 0 and 20 into a list"""
Num_lst = [x for x in range(21)]

"""to list EVEN numbers b/w 0 and 20 into a list"""
Num_lst_even = [x for x in range (21) if x % 2 == 0]

"""to create lists from other lists"""
# normally we do this:
words = ['HeLLo', 'GooDBYe']
lower_words = []
for w in words:
    lower_words.append(w.lower())

# alternatively:
lower_words = [w.lower() for w in words]

"""Create a list of only the even numbers in list n"""
n = [45, 2, 36, 77, 32, 19]
events = [x for x in n if x%2 == 0]

"""Create a list of the squares of integers 1-10."""
squares = [x**2 for x in range (1, 11)]


"""Practice Question 1: An "abecedarian" word is one where all of its letters are 
in alphabetical order. For eg: the words 'deep' and 'adept' are abecedarian.
Write a function is_abecedarian(word), which returns True or False depending 
on whether the input words is an abecedarian word."""


def is_abecedarian(word):
    word = word.lower()

    i = 0
    # prev_ch = word[0]
    for ch in word:
        if ch == word[0]:
            prev_ch = ch
        elif ch == prev_ch:
            continue
        elif ord(ch) > ord(prev_ch):
            prev_ch = ch
        else:
            return False
    return True


print(is_abecedarian('hello'))  # should result in false
print(is_abecedarian('adept'))  # should result in true
print(is_abecedarian('abecedarian'))  # should result in false
print(is_abecedarian('deep'))  # should result in true


"""Suggested solution: simple and concise! ~best approach!"""


def is_abecedarian_sol(word):
    for i in range(len(word)-1):  # why the -1? why not go all the way to the end?
        if word[i].lower() > word[i+1].lower():
            return False  # easier to falsify then verify
    return True


print(is_abecedarian_sol('hello'))  # should result in false
print(is_abecedarian_sol('adept'))  # should result in true
print(is_abecedarian_sol('abecedarian'))  # should result in false
print(is_abecedarian_sol('deep'))  # should result in true

""" Alternative Suggested solution: longer to write and so probably
better to write the one above"""


def is_abecedarian_sol2(word):
    for i in range(len(word)-1):
        if word[i].lower() <= word[i+1].lower():
            continue
        else:
            return False
            # is_ab = False
            # break
    else:
        is_ab = True
    return is_ab


print(is_abecedarian_sol2('hello'))  # should result in false
print(is_abecedarian_sol2('adept'))  # should result in true
print(is_abecedarian_sol2('abecedarian'))  # should result in false
print(is_abecedarian_sol2('deep'))  # should result in true


"""Practice Question 2: Write a function second_largest() which takes a list of 
numbers as input and returns the second largest number. Note that if the 
maximum/largest element occurs more than once in the list, then the function 
should still return the numerically second largest number. For example, if the 
list is [9,9,8,5], then the function would return 8."""


def second_largest(s):
    y = list(s)
    if len(y) == 1:
        return None
    z = sorted(y, reverse=True)
    largest = max(y)
    second_largest = None
    i = 0
    char = z[i]
    for char in z:
        if char < largest:
            second_largest = char
            return second_largest
            i += 1

    if char == largest:
        return None


x = '02873450274'
print('p0', second_largest(x))
print('p1', second_largest('777'))
print('p2', second_largest('5589'))
print('p4', second_largest('1'))


# similar to second_smallest from Actual MST

# def second_smallest(s):
#     y = list(s)
#     if len(y) == 1:
#         return None
#     z = sorted(s)
#     smallest = min(y)
#     second_smallest = None
#     i = 0
#     char = z[i]
#     for char in z:
#         if char > smallest:
#             second_smallest = char
#             return second_smallest
#             i += 1
#
#     if char == smallest:
#         return None
#
#
# x = '02873450274'
# print('p0', second_smallest(x))
# print('p1', second_smallest('777'))
# print('p2', second_smallest('5589'))
# print('p4', second_smallest('1'))


"""suggested solution: """


def second_largest_sol(lst):
    max1 = None
    if len(lst):
        max1 = max(lst)

    lst2 = [element for element in lst if element != max1]

    max2 = None
    if len(lst2):
        max2 = max(lst2)
    return max2


""" Alternative code for within this function: 
    while max1 in lst:
        lst.remove(max1)
    max2 = None
    if len(lst):
        max2 = max(lst)
    return max2
"""

x = '02873450274'
print('p0', second_largest_sol(x))
print('p1', second_largest_sol('777'))
print('p2', second_largest_sol('5589'))
print('p4', second_largest_sol('1'))

"""Alternative MST Questions"""
"""Q1 : see MSt_Actual_2022_Sem_1.py"""
"""Q2: Given the string variable text = 'happy as a clam'. 
Select the expression(s) that will produce the output 'py'."""
# myans: text[3:5],
text = 'happy as a clam'
print(text[3:5])  # ans
print(text[text.index('a')+2:-10])  # ans
print(text[text.find('p'):5])  # not ans
print(text[-len(text)+4:7])  # not ans

"""Q3: find 'map' from text = 'happy as a calm'. Using only the string 
variable text write an expression."""
print(text[-1] + text[-2] + text[2])
print(type(text[-1] + text[-2] + text[2]))
# actual answers => text[-1] + text[-2] + text[2]  Or see below
print(text[-1:-3:-1] + text[2])
print(text[-1] + text[1] + text[2])

"""Q4: Given the string variable text = 'happy as a clam'. 
Select the expression(s) that will produce the output 'py'."""
# given options:

# print(int('b'))
# if x == 'a' or 'b' or 'c':
# total = str(price*qty)
# print(f'{price} x {qty*2} = fantastic savings!!!')
# 'mary'[5:8:2]
# print(f"Hellow, {name], Welcome friend!!")

# syntax error = print(f"Hellow, {name], Welcome friend!!") # ] closing bracket has to be }
# runtime error = print(int('b'))
# logic error =  if x == 'a' or 'b' or 'c':

"""Q5: The function valid_password(pwd) takes a string pqd and checks 
whether it is valid. If the password is valid the function returns True, 
otherwise False. Valid password must be:
 1. 8 characters long
 2. 6 letters from A to Z or a to z
 3. digits from 0 to 9 
 Rearrange given lines of code for answer:"""


def valid_password(pwd):
    num_count, letter_count = 0, 0

    if len(pwd) == 8:
        for ch in pwd:
            if ch.isdigit():
                num_count += 1
            if ch.isalpha():
                letter_count += 1

        if num_count == 2 and letter_count == 6:
            return True
    else:
        return False

"""Q6: Fill in the blanks."""

# def calculate_pay(hours_worked, rate=25.5, tax_exempt=False):

# answers:
# The data type of hours_worked is int
# the data type of rate is float
# the data type of tax_exempt is boolean

"""Quiz Exam: screenshots from L11"""

"""Q1: which of the following best describes what we know about the variable something? 
if something: 
    print("conditional has been activated")"""""

if '1.0':
    print("conditional has been activated")

# myans: something is a boolean, integer, float, string

"""Q2: 
possible = True
nums = [1,435,6,6]
These are both egs of which of the following?"""
# myans: assignments

"""Q3: which of the following statement is false in Python?
id(110) == 110  # True
int('110') == 110  # False
int(110.0) == 100  # True
int(110) == 110  # True
ord('n') == 110  # True
"""
# if id(110) == 110:
#     print(True)
#
# print(ord('n'))

# myans: int('110') == 110,

"""Q4: In a nested for loop, which kind of error has occurred if a 
statement attempts to increase the value of an integer variable which
has not yet been referred to before in the code."""
# myans: name error?

"""Q5: Which of the following is true about variable age that is created 
and assigned within a function called is_eligible()?"""
# myans: age will only be interpreted by python once is_eligible()
# has been called from elsewhere in the program

"""Q6"""
# myans: x = str, y = list, z = dict/set ==> last op: int str list dict set

"""Q7"""
# myans: 7*3*4

"""Q8"""
# myans: set

"""Q9"""
# import random
#
# rand_num = random.randint(0, 10)
# numbers = [1, 4, 6, 20, 17, 18, 9, 28, 3, 7]
# if numbers[rand_num] % 2 == 0:
#     print("chosen number is " + numbers[rand_num])

# myans: logic error and syntax error??

"""Q10"""
# myans: data = rabbit.read()

"""Q11"""
# myans: option b
ans = [x for x in range(1, 100) if x % 3 ==0]
print(ans)
# opd = [for x in range(1, 101) if x % 3 ==0]
# print(opd)

"""Q12"""
# myans: catch
# uncomment for testing:
        # raise
        # catch
        # except
        # try
        # assert

"""Q13: """

"""Q13 Ans: logic error = will only be noticeable when you start getting 
incorrect answers to your test codes and won’t be something that python 
picks up on so it might be the last kind of error you might pick up on."""

"""Q14: We sometimes refer to ‘global variables’. Write ONE sentence to 
explain what is meant by the word ‘global’ in this context. (2 marks)"""

""" myans: Global variables, as the name implies, are variables that are 
accessible globally, or everywhere throughout the program. Once declared, 
they remain in memory throughout the runtime of the program."""

"""Q15: what are two disadvantages of a recursion approaches 
compared ot an iteration approach? (2 marks)"""
""" myans: usually more expensive (memory cost) for the computer to perform 
recursion and also slower in some cases (lag). 
"""

"""Q16"""
# myans: has_read = False, topic = 'psychology' and pages < 200 or topic topic = 'philosophy'

"""Q23: re-write code replacing for to while loops:
n = 1 
for i in range(5):
    for j in range(n):
        print('*', end='-')
    n += 2
    print()
"""
# myans:
n = 1
for i in range(5):
    for j in range(n):
        print('*', end='-')
    n += 2
    print('done org')

n = 1
i = 0
while i < 5:
    j = 0
    while j < n:
        print('*', end='-')
        j += 1
    n += 2
    print('done')
    i += 1

"""Q24"""
# myans:


def remove_dups(lst):
    uniq_lst = []
    dup_items = set()
    for x in lst:
        if x not in dup_items:
            dup_items.add(x)
            uniq_lst.append(x)
    return uniq_lst

lst = [1, 4, 6, 7, 8, 7]
print(remove_dups(lst))


"""Q25: Take the following code, which provides an iterative solution to 
determining whether an input list is sorted from lowest to highest: 
Write another function is_sorted(lst), which also determines whether an 
input list is sorted from lowest to highest, but does os useing 
a recursive approach. (4 marks)"""


def is_sorted_iter(lst):
    n = len(lst)
    if n == 0 or n == 1:
        return True

    for i in range(1, n):
        if lst[i - 1] > lst[i]:
            return False
    return True

# myans:


def is_sorted(lst):
    n = len(lst)
    if n == 0 or n == 1:
        return True
    for i in range(1, n):
        if lst[i - 1] > lst[i]:
            return False
    return True


print(is_sorted_iter([]))
print(is_sorted([]))


"""Q26 The geometric mean/average of a collection of n numbers is
defined as the nth root of the product of those n numbers:
formula = (x1*x2*x3)**(1/n) 

write a definition for a single function that takes a list of int vales as a 
parameter and calculate the geo mean of the values that are less than or equal
to 100, and the geo mean of the vals that are greater than or equal to 200, 
and returns both means rounded to 2 decimal places. if there are no integers
for either of the two ranges, then return the value None for that mean. (4 marks) """
# myans:
#
# my_list = [1, 2, 3, 6, 8]
# def calculate_mean(lst):
#     return sum(my_list)/len(my_list)
#
# print(calculate_mean(my_list))


# def calculate_geo_means(integer_list):
#     values_less = [num for num in integer_list if num <= 100]
#     values_more = [num for num in integer_list if num >= 200]
#     if len(values_less) != 0 or len(values_more) != 0:
#         mean_less = sqrt([x*x for x in values_less])
#         mean_more = sum(values_more) / len(values_more)
#         return f'{mean_less:.2f}, {mean_more:.2f}'
#     else:
#         return None
#
#
# lst1 = [1, 5, 8]  # ans should equal = 3.42
# lst2 = [2, 3, 4, 5]  # ans should equal = 3.31
# print(calculate_geo_means(lst1))
# print(calculate_geo_means(lst2))

# suggested solution Q26:

def split_list_geo_mean(lst):
    lower_lst = []
    upper_lst = []

    for item in lst:
        if item <= 100:
            lower_lst.append(item)
        if item >= 200:
            upper_lst.append(item)

    if len(lower_lst):
        lower_lst_geo_mean = 1
        for item in lower_lst:
            lower_lst_geo_mean = lower_lst_geo_mean * item  # note it is multiply not add
        lower_lst_geo_mean = lower_lst_geo_mean ** (1/len(lower_lst))
        lower_lst_geo_mean = round(lower_lst_geo_mean, 2)
    else:
        lower_lst_geo_mean = None

    if len(upper_lst):
        upper_lst_geo_mean = 1
        for item in upper_lst:
            upper_lst_geo_mean = upper_lst_geo_mean * item  # note it is multiply not add
        upper_lst_geo_mean = upper_lst_geo_mean ** (1 / len(upper_lst))
        upper_lst_geo_mean = round(upper_lst_geo_mean, 2)
    else:
        upper_lst_geo_mean = None

    return lower_lst_geo_mean, upper_lst_geo_mean


lst1 = [1, 5, 8]  # ans should equal = 3.42
lst2 = [2, 3, 4, 5]  # ans should equal = 3.31
print(split_list_geo_mean(lst1))
print(split_list_geo_mean(lst2))

# suggested solution to calculate the geo mean without the value sorting:


def calculate_geo_mean(lst):
    geo_mean = 1
    for item in lst:
        geo_mean = geo_mean * item

    geo_mean = geo_mean ** (1/len(lst))

    return geo_mean