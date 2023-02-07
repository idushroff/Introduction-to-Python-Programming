# --- Tute 8 ---
"""Q1b"""
# interesting piece of code!
mylist = [1, 2, 3]
for mylist[1] in mylist:
    print(mylist, mylist[1])

"""Q2"""
# products = [('cups', 5.), ('saucers', 3.5), ('plates', 6.), ('bowls', 3.5)]
# new_list = []
# for name, price in products:
#     new_list.append((price,name))
# print(new_list)
# 'Q2b'
# print(sorted(new_list))
# 'Q2c'
# print(sorted(new_list, reverse = True))
# 'Q2d'
# new_list2 = []
# for name, price in products:
#     new_list2.append((-price,name))
# print(new_list2)

# new_list3 = []
# for neg_price, name, in sorted(new_list2):
#     new_list3.append((-neg_price, name))
# print(new_list3)

"""Q3"""
# products = [('cups', 'homewares'), ('saucers', 'homewares'), ('chairs', 'furniture'),
#         ('tables', 'furniture'), ('sheets', 'bedding'),
#         ('pillows', 'bedding'), ('doonas', 'bedding')]
# category_to_product = {}
# for product, category in products:
#     if category not in category_to_product:
#         category_to_product[category] = []
#     category_to_product[category].append(product)
#     print(category_to_product)

"""Q4"""

"""Q5"""
from collections import defaultdict


def isogram(word):
    stock = defaultdict(int)

    for ch in word:
        stock[ch] += 1

    counts = list(stock.values())
    for count in counts[1:]:
        if count != counts[0]:
            return False
    return True

print(isogram('hello'))