import math

# ---- Tute 6 week 6---------
"""Q2a+b) write a function for given geometry equation (see tute sheet)"""


def distance(x0, x1, y0, y1):
    x = x0-x1
    y = y0-y1
    return math.sqrt(x*x + y*y)  # or you could write math.sqrt(x**2 + y**2)


print(distance(1, 1, 4, 5))

"""Q3"""
# def even_odd (number, animal):
#     number = 4
#     if number % 2 == 0:
#         print("I have an even number of", animal)
#     else:
#         print("I have an odd number of", animal)
#
# cats = 27
# dogs = 13
# guinea_pigs = 4
#
# even_odd(cats, "cats")
# dogs += 1
# print("A puppy was born")
# even_odd(dogs, "dogs")
# even_odd(guinea_pigs, "guinea_pigs")


"""Q4"""
# def myrjust(s, w, c=' '):
#     while len(s) < w:
#         s = c + s
#     return s
# print(myrjust("Program", 20, "#"))
#
