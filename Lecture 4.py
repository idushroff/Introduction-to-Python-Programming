# Lecture 4 challenges:
# 1. write a program to devowel a given string and print the result.
# Devowelling is the process of removing vowels (a,e,i,o,u) from a string.
# x = "aksjdhflakjsdhfaahhh"
# y = ""
# for char in x:
#     if char not in "aeiou":
#         y = y + char
# print(y)

# second attempt at this challange from the future
text = "my dog has my name"
devowel_text = ""
for char in text:
    if char not in 'aeiou':
        devowel_text += char
print(devowel_text)

# alternative solution:

# y = x.replace('a', "").replace('e', "").replace('i', "").replace('o', "").replace('u', "")
# print(y)

# 2. Determine whether a given string contains a double consecutive occurrence of any characters (eg: 'ee', 'oo', '11').
# string = "askldjfhakhdaa"
# previous_character = ""
# for character in string:
#     if previous_character == character:
#         print(previous_character + previous_character + " is in the string!")
#     previous_character = character


# lecture notes
s = "testing slicing 101"
print(s[4:-7])
print(s[-7:-1])
print(s[-6:len(s)])

# Exercise 3 - deciding if a password is secure
"""An organization defines a valid password as follows: 
1. it must be 8-15 characters in length
2. it must contain at least one uppercase char(A-Z)
3. it must contain at least one lowercase char(a-z)
4. it must contain at least one digit

write a program that takes a password string and returns if it is valid or not."""
password = "alskdA69as"

has_lower = False
has_upper = False
has_digit = False
count = 0

if 15 < len(password) < 8:
    print('invalid password')
else:
    for char in password:
        if char.islower():
            has_lower = True
            count += 1
        if char.upper():
            has_upper = True
        if char.isdigit():
            has_digit = True
    if has_upper and has_digit and has_lower:
        print('valid password')
    else:
        print('invalid password')

print(count)

