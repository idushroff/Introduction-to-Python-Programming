# Practice MST:
# text = 'the cow jumped over the moon'
# print(text[6], text[2], text[0])
# print(text[6:21:11])
# import math
# def area_circle(radius):
#     return math.pi*radius**2
# print(area_circle(3))

# More practice MST Questions I found online:


'Q1) Evaluate each of the following expressions; what is the output in each case?'
# 1a) 'tom' now in 'optimist'
# ans = true
# 1b) ('{} was a door number, {} was one too'.format(11,22))
# ans = '11 was a door number, 22 was one too'
# 1c) print('COMP90059'.find('95'[::-1]))
# ans = 7
# 1d) print('testing 123'.index('1'))
# ans = 8


'''Q2 (4 marks): Consider the following piece of code. Briefly explain what this code does? If the variable
s = ‘student 23’, what is the output produced by this code?'''
# s = input("Input a string: ")
# d = 0
# l = 0
# for c in s:
#     if c.isdigit():
#         d = d + 1
#     elif c.isalpha():
#         l = l + 1
# print('l:', l)
# print('d:', d)
# ans -> It counts how many digits and how many alphabetic characters are in the string, into the int variables d and l
# respectively. Sample output is: l = 7 and d = 2 for an input of student 23.

'''Q3: Rewrite the following program code, replacing the two for loops with while loops, while preserving the
remainder of the original code structure and output:'''
# n = 10
# total = 0
# for i in range(0, n):
#     for j in range(0, n):
#         print('{}{}'.format(i, j), end=' ')
#         total = total + i + j
#     print(total)
# print('End the program')
#
# Q3 answer basic form:
# for var in range (start, stop):
#
# change to:
#
# var = start
# while var < stop
#     ...
#     var += 1
# as follows ==> Q3 answer
# n = 10
# total = 0
# i = 0
# j = 0
# while i < 10:
#     while j < 10:
#         print('{}{}'.format(i, j), end=' ')
#         total = total + i + j
#         j = j + 1
#     print(total)
#     i = i + 1
#     j = 0                                  # why do we need this line? to reset the j back to 0
# print('End the program')

"""# Q4: anagram - Note: identical word match should not return True.
# You only need to compare individual words in sentence with the word.

# Two words are said to be anagrams of each other is all the letters of one word are present in the other word,
and vice versa. for example the words 'ate' and 'eat' are anagrams of each other. similarly, 'lee and eel' are anagrams.
Write a function in Python that accepts two inputs: one that accepts a word and the other that accepts a sentence.
Your function must return True if the word has an anagram in the sentence and False if not. To receive full marks,
your code must be correct. make sure that your program is appropriately commented. For example:

word = input("Enter a word: ")
sentence = input("Enter a sentence: ")
def anagrams(word, sentence):

return True if word in sentence
"""

# def anagrams(word, sentence):
#     for w in sentence.split():
#         print(w)
#         print(sorted(w))
#         print(sorted(word))
#         if w != word and sorted(w) == sorted(word):
#             return True
#     return False
# print(anagrams('tac', 'tic tac tic'))
# print(anagrams('cat', 'I will act in a movie'))


# # option B:
# def anagram(word, sentence):
#     anagram = False
#     words = sentence.split()
#     for w in words:
#         print(w, 'this is w')
#         for i in word:
#             print(i, 'this is i')
#             print(word, 'this is word')
#             if i in w:
#                 print(i, w, 'this is i, w')
#                 j = w.index(w)
#                 print(j, 'this is j')
#                 w = w[:j] + w[j+1:]
#                 print(w, 'this is w')
#             else:
#                 break
#         else:
#             anagram = True
#             break
#     return(anagram)
# print(anagram('cat', 'I will act in a movie'))

