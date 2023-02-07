
# # Tute 4 week 4
# # 1a) True
# a = False
# print(a)
# # 1c) False
# print(int(True))
# # 1d) 1
# print(False + True + True)
# # 1e) 2
# """What is meant by a literal in Python and what is a Boolean literal? -> literal = true and flase - basic string"""
# print(False or True)
# # 2a) True
# print(False and True)
# # 2b) False
# print(False or True or False)
# # 2c) True
# print(not False)
# # 2d) True
# """Which of the logical operators are binary operators and which are unary operators?"""
# # 3. Fully parenthesize the following Boolean expressions, to show how Python would interpret the expression.
# # Then calculate the answers to the expressions.
# print(not True and False)
# # 3a) False
# print(False and True or False)
# # 3b) False
# """Given an expression such as False and (True or False), is it necessary to calculate the right-hand
# side of the and operator when the left-hand side is already known?"""
# No
# # 4. Comparison operators combine both arithmetic and reasoning. Generally the operands to a comparison
# # operator can be of any type, but the result will always be Boolean. What do these return?
# # 4a) 5.0 < 10
# # 4b) x >= 5 and x <= 10
# # 5. More on strings. What would happen if we did this:
# # 5a) a[2]
# # 5b) print(’Hello\nGoodbye\n’)
# # 5c) 'Hello’ * 3
# # 6. We have seen that the operators are very useful in Python. For example, we type ‘5 + 2’ in order to do some addition.
# # There are also other things we do commonly in Python, such as taking the minimum of a pair of numbers,
# # but which are not as common as addition and therefore are not written as operators.
# # Instead, Python provides built-in functions for these kinds of activities. Evaluate:
# # 6a) min(5, 2) -> ans: 2
# # 6b) random.randint(1, 5) -> import random -> means randomly generate an integer b/w 1 and 5
# # Note that the numbers or objects passed to a function are called arguments rather than operands.
# # 7. Assuming the assignment s = ’internationalization’ has been made, evaluate:
# # 7a) s[1] -> n
# # 7b) s[:-1] -> will give everything expect the last letter #note: nothing before the : means 0
# # 7c) s[:6] + s[11:13] -> inter + nal
# # 7d) s[25] -> error
# # 7e) s[::-1] -> #note: :: means count in reverse
# # 7f) s[:25] -> whole word
# # 8. Assuming the assignments
# a = 1
# b = 2
# c = 3.0
# d = 0
# # have been made, evaluate:
# bool(d and not b or a)
# # ans: false and not true or true = false and false or true -> true
# bool((d and not b) or a)
# # ans: true
# bool(d and not (b or a))
# # ans: false and false -> false

# notes:truth tables:
# exclusive or: x or -> only or not both -> so if a and b are both true then its false [used in cryptography]
