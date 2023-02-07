
from itertools import combinations, permutations

def hack_it(start, middle, end):
    passwords = [start, middle, end]
    print('p2', passwords)
    password = list(itertools.product(*passwords))
    print('p1', password)
    tupples = []
    for tupple in password:
        tupple = tupple[0] + tupple[1] + tupple[2]
        tupples.append(tupple)
    return tupples

LIKELY_WORDS = ["Frenchy", "INTENSE", "ComputerScienceFTW", "HelloMrGumby"]
possible_starts = []
for j in permutations(LIKELY_WORDS, 2):
    # print(j)
    js = list(j)
    # print(js)
    k = (js[0] + js[1])
    possible_starts.append(k)

ages = []
for i in combinations("00123456789", 2):
    # print(i)
    i = list(i)
    age = (i[0] + i[1])
    ages.append(age)

START = possible_starts
MIDDLE = ['Horse20']
END = ages[:39]
print(hack_it(START, MIDDLE, END))


# ----
from itertools import combinations, permutations

def hack_it(start, middle, end):
    passwords = [start, middle, end]
    password = list(itertools.product(*passwords))
    tupples = []
    for tupple in password:
        tupple = tupple[0] + tupple[1] + tupple[2]
        tupples.append(tupple)
    return tupples

LIKELY_WORDS = ["Frenchy", "INTENSE", "ComputerScienceFTW", "HelloMrGumby"]
possible_starts = []
for j in permutations(LIKELY_WORDS, 2):
    js = list(j)
    k = (js[0] + js[1])
    possible_starts.append(k)

ages = []
for i in combinations("00123456789", 2):
    i = list(i)
    age = (i[0] + i[1])
    ages.append(age)

START = possible_starts
MIDDLE = ['Horse20']
END = ages[:39]
print(hack_it(START, MIDDLE, END))

