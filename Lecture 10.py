# """Declare and assign the following to a variable named my_var:"""
# Revision Question 1
# my_var = ['apple', 'pear', 'orange', 'lemon']
# Revision Question 2
# my_var = '54'
# Revision Question 3
# my_var = [('apple', '$4.40'), ('pear', '$4.40'), ('orange', '$4.40'), ('lemon', '$4.40')]
# Revision Question 4
# ((2**3)*8)+6 = 6+8*2**3
# = 8*8+6
# = 64+6
# = 70
# Revision Question 5
# -> return 'spree'
s = "spam and green eggs"
print(s[0:2] + s[10:13])
#alternatively
print(s[0:2] + s[-9:-6])

# Revision Question 6
a = True
b = False

print((a and b) or not a)
# ans = false

# Revision Question 7
print(('pi' in 'sky') or ('3.14'.isdigit()))
# false or false = false

# Revision Question 8
def acceptance(atar, workexp, age):
    if atar > 85:
        return True
    elif atar > 75 and workexp >= 2:
        return True
    elif age > 25 and workexp >= 5:
        return True
    else:
        return False


# NOTE isdigit only works with strings and if every character of that string is numeric i.e.'314' ->  not floats like '3.15'

# Revision Question 9 = aka = Revision Questions 4
"""Write a function that takes as input a list of integers and prints the next four even numbers for each item in the list."""

def next_4_even(num_lst):
    for num in num_lst:
        print('the next 4 even numbers of ' + str(num) + ' are:')
        if num % 2: # if num is odd
            num += 1
        else: # else num is even
            num += 2

        for x in range(num, num+8, 2):
            print(x)

lst = [0, 1, 2, 3]
print(next_4_even(lst))
# output should = 0,2,4,6,8. 1, 2,4,6,8. 2,4,6,8,10. 3,4,6,8,10

# 1 hour 27 mins into L10
# there is a difference b/w copying a list and copying a list by going through each element in that list.
# copying using copy() example:

import copy

old_list = [123, ['four', 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

new_list2 = []
new_list2.append(old_list[0])
new_list2.append(copy.copy(old_list[1], old_list[2]))
# new_list2.append(copy.copy(old_list[2]))



old_list.append([10])
new_list.append([11])
old_list[1][0] = 4
old_list[0] = 321

print("old_list:", old_list)
print(id(old_list))
print()
print("new_list:", new_list)
print(id(new_list))
print()
print("new_list2:", new_list2)
print(id(new_list))