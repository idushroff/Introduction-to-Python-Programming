# mean Question
"""Write a function definition that takes a list of integers called
ages[ ] and returns the mean of those integers. Assume that you
cannot use any existing statistical functions. Note:  the mean of
a group of values is defined as the total divided by the total
number of values."""


def mean_age(ages):
    total = 0
    for age in ages:
        total += age
    mean = total / len(ages)
    return mean


ages = [0,1,2,3,4]
print(mean_age(ages))

"""suggested solution for mean question: """


def ages_average(ages):
    total = 0
    count = 0

    for age in ages:
        total = total + age
        count = count + 1
    if not count:
        return 0
    else:
        return total / count


# median Question
"""Write a function definition that takes a list of integers called 
ages[ ] and returns the median of those integers. Assume that you 
cannot use any existing statistical functions. Note:  the median of 
a group of values is defined as the middle value if the values are 
placed in order (in the case of an odd number of values); or the mean 
of the middle two values (in the case of an even number of values)."""


def median_age(ages):
    s_ages = sorted(ages)
    if len(ages) % 2 == 0: # then that means there are an even num of values
        i = int((len(s_ages)/2) - 1)
        j = int((len(s_ages)/2))
        middleval1 = s_ages[i]
        middleval2 = s_ages[j]
        mean = (middleval1 + middleval2) / 2
        return mean
    else:
        k = int((len(s_ages)/2) - 0.5)
        median = s_ages[k]
        return median


ages = [0,1,2,3,4,8]
print('myans', median_age(ages))

"""suggested solution for median Q: """


def ages_median(ages):
    ages_sorted = sorted(ages)
    len_list = len(ages_sorted)

    if len_list % 2 == 0:
        return (ages_sorted[int(len_list / 2) - 1] + ages_sorted[int(len_list / 2)]) / 2
    else:
        return ages_sorted[len_list // 2]


ages = [0,1,2,3,4,8]

print('their ans', ages_median(ages))

# mode Question
"""Write a function definition that takes a list of integers called
ages[ ] and returns the mode of those integers. Assume that you
cannot use any existing statistical functions. Note: the mode of
a group of values is defined as the most frequently occurring value
in the group."""
# The list for which you need to find
# the Mode
y= [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8]

# First you sort it
# You will get numbers arranged from 3 to
# 11 in asc order
y.sort()

# Now open an empty list.
# What you are going to do is to count
# the occurrence of each number and append
# (or to add your findings to) L1
L1=[]

# You can iterate through the sorted list
# of numbers in y,
# counting the occurrence of each number,
# using the following code

i = 0
while i < len(y) :
    L1.append(y.count(y[i]))
    i += 1

# your L1 will be [1, 2, 2, 1, 3, 3, 3, 1, 3, 3, 3, 1],
# the occurrences for each number in sorted y

# now you can create a custom dictionary d1 for k : V
# where k = your values in sorted y
# and v = the occurrences of each value in y

# the Code is as follows

d1 = dict(zip(y, L1))

# your d1 will be {3: 1, 4: 2, 5: 1, 6: 3, 7: 1, 8: 3, 11: 1}
# now what you need to do is to filter
# the k values with the highest v values.
# do this with the following code

d2={k for (k,v) in d1.items() if v == max(L1) }

print("Mode(s) is/are :" + str(d2))


# above code compressed and polished:
y= [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8]
y.sort()
L1=[]
i = 0
while i < len(y):
    L1.append(y.count(y[i]))
    i += 1

d1 = dict(zip(y, L1))

d2 = {k for (k, v) in d1.items() if v == max(L1)}
set_to_dict = list(d2)
print(set_to_dict)

print("Mode(s) is/are : " + str(set_to_dict[0]))

"""suggested solution for mode question: """


def ages_mode(ages):
    ages_dict = {}

    for age in ages:
        if age in ages_dict:
            ages_dict[age] = ages_dict[age] + 1
        else:
            ages_dict[age] = 1
    count_pairs = [(ages_dict[key], key) for key in ages_dict]
    count_pairs = sorted(count_pairs)
    return count_pairs[-1][1]


y = [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8]
print(ages_mode(y))

"""pin's solution: ~~~~better~~~~"""
from collections import defaultdict as dd


def ages_mode(ages):
    result_dict = dd(int)
    for num in y:
        result_dict[num] += 1

    result_list = []
    for key, value in result_dict.items():
        result_list.append((value, key))

    result_list = sorted(result_list)
    return result_list[-1][1]


y = [11, 8, 8, 3, 4, 4, 5, 6, 6, 6, 7, 8]
print(ages_mode(y))
