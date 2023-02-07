# Mst
'''1. Suppose we see the following line of code in a working program:
print(x * 5). Which of the following data types could x be? '''
# Q1 Ans: an integer, float, string or boolean

'''(from L11) Alternative MST Q1. Suppose we see the following line of code in a working program:
print(x + 5). Which of the following data types could x be? '''
# Q1 Ans: an integer, float, or boolean

'''2. A programmer writes a function that contains THREE nested for-loops with 
the following iterables respectively: range(a), range(b), range(c). Each time 
the THREE for-loops are executed fully, the total number of iterations produced 
by the INNERMOST loop is 90. Which of the following contains possible values 
for a, b and c respectively?'''
# Q2 Ans: 3,5,6


'3: find red room from this string'
s = 'predict moor'
 #    0123456 891011
print(s[1:4] + s[7] + s[11:7:-1])

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
# Q5 Ans: def create_bank_user(username, age, balance, rate_exempt = False):


''' 6. Using the function print_special_numbers below, rewrite the function, replacing the for
loops with while loops, but preserving the remainder of the original code structure and
functionality.'''


def print_special_numbersorg(interger_range):
    for number in range(1, interger_range + 1):
        sum = 0
        for i in range(1, number):
            if (number % i == 0):
                sum = sum + i

        if (sum == number):
            print(f"{number} is a Special Number")


def print_special_numbers(interger_range):
    number = 1
    while number < (interger_range + 1):
        sum = 0
        number += 1
        i = 1
        while i < number:
            if (number % i == 0):
                sum = sum + i
            i += 1

        if (sum == number):
            print(f"{number} is a Special Number")

print('p1', print_special_numbersorg(60))
print('p1', print_special_numbers(60))

''' 7. - explain the for loop function and what it is special number:'''
# a special number is a positive integer that is equal to the sum of its divisors and produces a remainder of 0 when divided by its divisors. eg: 6 which produces a remainder of 0 when divided by  1, 2, and 3. 1+2+3 = 6.

''' 8. Write a function alpha_only() which takes a string as input and as output 
returns a string with only English alphabet characters (and spaces) remaining. 
For example, alpha_only('Python 4ever!') would return 'Python ever'''
def alpha_only(input_string):
    i = 0
    output_string = ''
    for char in input_string:
        char = input_string[i]
        if char.isalpha() or char == ' ':
            output_string += char
        i += 1
    return output_string

input_string = 'Python 4ever!'
print(alpha_only(input_string))

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

# GIVEN LINES

TRY AGAIN!

print(valid_order_string("abc987dez"))
# should return True
print(valid_order_string("zab"))
# should return False
print(valid_order_string("abc123"))
# should return False


'''10. Write a function second_smallest(s), which takes a string s consisting 
of numeric characters (digits 0 - 9) and returns the second smallest digit as an integer. 
Note that if the minimum element occurs more than once in the string, then the function 
should still return the numerically second smallest digit. For example, if the string is "
5589", then the function would return 8.
- If the string has one or less digits, then return None.
- If the string does not have a numerically second smallest digit (e.g., "777"), then return None.'''


def second_smallest(s):
    y = list(s)
    if len(y) == 1:
        return None
    z = sorted(s)
    smallest = min(y)
    second_smallest = None
    i = 0
    char = z[i]
    for char in z:
        if char > smallest:
            second_smallest = char
            return second_smallest
            i += 1

    if char == smallest:
        return None


x = '02873450274'
print('p0', second_smallest(x))
print('p1', second_smallest('777'))
print('p2', second_smallest('5589'))
print('p4', second_smallest('1'))