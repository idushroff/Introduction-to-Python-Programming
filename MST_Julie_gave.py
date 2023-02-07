# Q2
# my ans =
print(7*3*4)

# Q3
text = 'the quick brown fox jumps over the lazy dog'
# output should = "brown dog"
print(text[10:16] + text[-3:])
# my ans = add ':' to expression

# Q4
# my ans = username = string, age = int, balance = float, rate_exempt = boolean

# Q5
# my ans = create_bank_user(username, age, balance = 10.00, rate_exempt = )
# ans = First three are ok, next two are not ok (option d has an
# invalid variable name 'age#', and option e does not call the full
# function name correctly)

# # Q6 - given code:
# def print_magic_number(nums):
#     for i in range(len(nums)):
#         curr_num = nums[i]
#         digits = list(str(curr_num))
#         total = 0
#         for j in range(len(digits)):
#             total += int(digits[j])
#         if total * 2 == curr_num:
#             print(curr_num, 'is a magic number')
#         else:
#             print(curr_num, 'is NOT a magic number')
#
# print('p1', print_magic_number('64'))
#
# # my ans =
# def print_magic_numbers(nums):
#     i = 0
#     while i < len(nums):
#         curr_num = nums[i]
#         digits = list(str(curr_num))
#         total = 0
#         j = 0
#         while j < len(digits):
#             total += int(digits[j])
#         if total * 2 == curr_num:
#             print(curr_num, 'is a magic number')
#         else:
#             print(curr_num, 'is NOT a magic number')
#         j += 1
#         i += 1
#
#
# print('p1', print_magic_numbers('64'))
#
# j = 0
# j += 1
# i = 0
# i += 1
# while i < len(nums):
# while j < len(digits):


# Q7
def print_magic_number(nums):
    for i in range(len(nums)):
        curr_num = nums[i]
        digits = list(str(curr_num))
        total = 0
        for j in range(len(digits)):
            total += int(digits[j])
        if total * 2 == curr_num:
            print(curr_num, 'is a magic number')
        # else:
        #     print(curr_num, 'is NOT a magic number')

# how to print numbers 1 to 1000 method 1
l = [i for i in range(1001)]
# print('p10', l)
print('p5', print_magic_number(l))
# my ans = 18

# how to print the numbers 1 to 1000 method 2
digits = []
for x in range(1000):
    digits.append(x)


# Q8
# my ans =
# def devowel(sentence):
#     output = ''
#     for ch in sentence:
#         if ch.lower() not in 'aeiou':
#             output += ch
#     return output
#
# text = input('Text: ')
# print(devowel(text))

# Q9 = similar as alternative mst Q discussed in L11

def valid_password(pwd):
    letter_count = 0
    if len(pwd) == 8:
        for ch in pwd:
            if ch.isalpha():
                letter_count += 1
        if letter_count == 4:
            return True
    return False

# 5 -> 7 -> 1 -> 3 -> 8 -> 2 -> 4 -> 9 -> 6 ==> option 9

pwd0 = 'hals9999'
pwd1 = 'ah00'
pwd2 = 'ha808999'

print('t1', valid_password(pwd0))
print('t2', valid_password(pwd1))
print('t3', valid_password(pwd2))
