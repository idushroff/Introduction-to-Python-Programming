# Q1: Evaluate each of the following expressions; what is the output in each case?
# 1. True
# 2. 11 was a door number, 22 was one too.
# 3. true?
# 4. index = 8
print('testing 123'.index('1'))

# Q2
# This code takes an input string and returns the number of digits
# and alphabetical characters in it. The output of this code is l = 7 and d = 2.

s = 'student 23'
d = 0
l = 0
for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1

print('l:', l)
print('d:', d)

# Q3 GIVEN CODE:
n = 10
sum = 0
for i in range(0, n):
    for j in range(0, n):
        print('{}{} '.format(i, j), end='')
        sum = sum + i + j
    print(sum)
print('End of program')

# ans:
n = 10
sum = 0
i = 0
while i < n:
    j = 0
    while j < n:
        print('{}{} '.format(i, j), end='')
        sum = sum + i + j
        j += 1
    print(sum)
    i += 1
print('End of program')

# Q4  my ans:
def anagrams(word, sentence):
    ssentence = sentence.split()
    letters = word.split()
    for chars in ssentence:
        if word == chars:
            return False
        else:
            s_chars = sorted(chars)
            s_word = sorted(word)
            if s_word == s_chars:
                return True
    return False


print(anagrams('cat', 'I will act in a movie'))
# >>> True
print(anagrams('tac', 'tic tac tic'))
# >>> False
# Identical word match should not return True
print(anagrams('mad', 'ma dad wants you'))
# >>> False

# their ans (so concise and beautiful)!
def anagrams(word, sentence):
    for w in sentence.split():
        if w != word and sorted(w) == sorted(word):
            return True
    return False
