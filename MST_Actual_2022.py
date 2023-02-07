# Mst
'''1. Suppose we see the following line of code in a working program:
print(x * 5). Which of the following data types could x be? '''
# Q1 Ans: an integer, float, string, or boolean

'''2. A programmer writes a function that contains THREE nested for-loops with 
the following iterables respectively: range(a), range(b), range(c). Each time 
the THREE for-loops are executed fully, the total number of iterations produced 
by the INNERMOST loop is 90. Which of the following contains possible values 
for a, b and c respectively?'''
# Q2 Ans:

i = 0
sum = 0
for i in range (1,4):
    for j in range (1,6):
        for k in range(1,7):
            sum += 1
            print('p1', sum)

# n = int(input('enter a number: '))
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         for k in range(1, n+1):
#             print(i,k)
# print("Good bye")

'3'
s = 'predict moor'
#    0123456 78910
# my answer: print(s[1:4] + s[:7:-1]) # incorrect there should be a + sign instead of a comma. The comma was giving me the space
# still wrong if i had done the + sign -> print(s[1:4] + s[:7:-1])

# print(s[1:4] + s[7] + s[-1:-5:-1]) #correct answer!


'''4. The function create_bank_user takes four arguments:'''
# 1. username
# 2. age, as a whole number
# 3. balance, with default value of 50.0
# 4. rate_exempt, with default value False
# The data type of username is # string
# The data type of age is # integer
# The data type of balance is # float
# The data type of rate_exempt is # boolean

'''5. Write the complete function declaration (def) line for the function 
create_bank_user as described above (Q4).'''
# Q5 Ans:

# def create_bank_user(username, age, balance = 50.0, rate_exempt = False):



''' 6. Using the function print_special_numbers below, rewrite the function, replacing the for
loops with while loops, but preserving the remainder of the original code structure and
functionality.'''
# GIVEN code:
# def print_special_numbers(interger_range):
#     for number in range(1, interger_range + 1):  # for number in 1,4
#         sum = 0
#         print('p0', number)
#         for i in range(1, number):
#             print('p1', i, number)
#             if (number % i == 0):
#                 sum = sum + i
#
#         if (sum == number):
#             print('p2', f"{number} is a Special Number")
# print('p3', print_special_numbers(7))
# # print(print_special_numbers(24))

# Q6 ANSWER:
# def print_special_numbers(interger_range):
#     number = 1
#     while number < interger_range + 1:
#         i = 1
#         sum = 0
#         #print('z0', number)
#         while i < number:
#             #print('z1', i, number)
#             if (number % i == 0):
#                 sum = sum + i
#             i += 1
#         if (sum == number):
#             print('z2', f"{number} is a Special Number")
#         number += 1

# print('z3', print_special_numbers(7))
# print(print_special_numbers(29))
# print('p4', print_special_numbers(124))

''' 7. - explain the for loop function and what it is special number:'''
# my ans: 6 is sum of 1,2,3 and also divisible by all three.

# my submitted ans: A special number is a positive integer that is equal to the
# sum of its divisors and produces a remainder of 0 when divided by its divisors.
# eg: 6 which produces a remainder of 0 when divided by  1, 2, and 3. 1+2+3 = 6.

# their answer: A special number is one where its divisors sum up to the
# number itself; what are traditionally known in mathematics as perfect numbers.
# For example. 1+2+3 = 6.

''' 8. Write a function alpha_only() which takes a string as input and as output 
returns a string with only English alphabet characters (and spaces) remaining. 
For example, alpha_only('Python 4ever!') would return 'Python ever'''
# my answer 3 weeks after the actual mst:
# def alpha_only(text):
#     i = 0
#     s = ''
#     for char in text:
#         char = text[i]
#         if char.isalpha() or char == ' ':
#             s += char
#         i += 1
#     return s
#
#
# text = 'Python 4ever!'
# print(alpha_only(text))

''' 9. The function valid_order_string(s) takes a string s consisting 
of alphanumeric characters and checks whether it is valid according to the 
following order rules: 
* for each alpha character in the string (x), no alpha character after it (y) 
can be less than it according to Python ASCII character comparison (x <= y) 

* for each numeric character in the string (x), no numeric character after 
it (y) can be greater than it (x >= y)

If the string is valid the function returns True, otherwise False. For example, 
valid_order_string('abc987dex') would return True
valid_order_string('abc123') would return False

As presented, the lines of the function below are out of order. 
Put the lines in a correct order and introduce appropriate/correct indentation 
to get a correctly working function.'''
# Q9 Ans:
# def valid_order_string(string):
#     prev_char_alpha = prev_char_num = None
#     for char in string:
#         if char.isalpha():
#             if not (prev_char_alpha is None) and (char < prev_char_alpha):
#                 return False
#             prev_char_alpha = char
#
#         if char.isnumeric():
#             if not (prev_char_num is None) and (char > prev_char_num):
#                 return False
#             prev_char_num = char
#
#     return True
#
#
# print(valid_order_string('abc987dex'))  # should return True
# print(valid_order_string('abc123'))  # Should return False

'''10. Write a function second_smallest(s), which takes a string s consisting 
of numeric characters (digits 0 - 9) and returns the second smallest digit as an integer. 
Note that if the minimum element occurs more than once in the string, then the function 
should still return the numerically second smallest digit. For example, if the string is "
5589", then the function would return 8.

- If the string has one or less digits, then return None.

- If the string does not have a numerically second smallest digit (e.g., "777"), then return None.'''

# Q10 Ans option 1:
def second_smallest(s):
    h = sorted(s)
    first_smallest = None
    second_smallest = None
    for element in h:
        if first_smallest is None:
            first_smallest = element
        elif element != first_smallest:
            second_smallest = element
            return int(second_smallest)
    return None


x = '5589'
y = '777'
z = '1'
print(second_smallest(x))
print(second_smallest(y))
print(second_smallest(z))

# Q10 Ans option 2:
def second_smallest(s):
    if len(s) <= 1:
        return None
    min1 = min(s)
    s2 = s.replace(min1, "")
    if len(s2):
        min2 = min(s2)
        return int(min2)
    return None


x = '5589'
y = '777'
z = '1'
print(second_smallest(x))
print(second_smallest(y))
print(second_smallest(z))

# Q10 Ans option 3:

def second_smallest(s):
    if len(s) <= 1:
        return None
    first_smallest = None
    second_smallest = None
    for number in s:
        if first_smallest is None:
            first_smallest = number
        elif second_smallest is None and number > first_smallest:
            second_smallest = number
        elif number < first_smallest:
            second_smallest = first_smallest
            first_smallest = number
        elif not second_smallest is None and (number < second_smallest) and (numerb > first_smallest):
            second_smallest = number
    if not second_smallest is None:
        return int(second_smallest)
    else:
        return None

x = '5589'
y = '777'
z = '1'
print(second_smallest(x))
print(second_smallest(y))
print(second_smallest(z))