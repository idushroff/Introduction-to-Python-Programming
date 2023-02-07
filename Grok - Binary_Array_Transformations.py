# This function is to determine new element values
def func_2(item, nb_total):  # nb_total stands for total of neighbours
    new_x_value = ''
    if item == 1:
        if nb_total == 0:
            new_x_value = 0
        if nb_total == 2 or nb_total == 1:
            new_x_value = 1
        if nb_total > 2:
            new_x_value = 0
    if item == 0:
        if nb_total == 2:
            new_x_value = 1
        else:
            new_x_value = item
    return new_x_value


# This function is to determine the value of an element's neighbour
def neighbours(list_x):
    list_5 = []
    nb_total = ''
    ll = len(list_3)  # ll stands for lenth of list
    for i in range(ll):
        item = list_3[i]
        nb_total = list_3[i - 1] + list_3[i - 2] + list_3[i + 1 - ll] + list_3[i + 2 - ll]
        list_5.append(func_2(list_3[i], nb_total))
    return list_5


list_1 = input("Enter input list: ").split(",")
cycles = int(input("Enter number of cycles: "))

valid_list = False
if len(list_1) >= 5:
    valid_list = True
    list_3 = []
    for i in range(0, len(list_1)):
        num = list_1[i]
        if num.isalpha():
            list_3.append(1)
        if num.isalpha() == False:
            num = int(list_1[i])
            if num > 1:
                list_3.append(1)
            if num == 0 or num == 1:
                list_3.append(num)
        i += 1
    # print(list_3)
else:
    print("Not enough items")

output_c1 = []
cycle = 1
while cycle < (cycles + 1):
    output_c1 = neighbours(list_3)
    list_3 = output_c1.copy()
    cycle += 1
print(output_c1)
