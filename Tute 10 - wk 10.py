d = {}
for elem in '':
    if elem not in d:
        d[elem] = 1
    else:
        d[elem] +=1


form collections import defaultdict


dd = defaultdict(int)

def gen_list(n):
    result = []
    for row in range(n):
        result.append([])
        for col in range(10):
            result[row].append((row+col)%2)
    return result

pprint.pprint(gen_list(5))

def flip_list(L):
    for row in range(len(L)):
        for col in range(len(L([row])):
            L[row][col] = 1 - L[row][col]

pprint.pprint(L)

def avg_col(L,index):
    total = 0
    for row in range(len(L)):
        total+=L[row][index]
    return total/len(L)

print(avg_col(L, 2))
print(avg_col(L, 3))
print(avg_col(L, 4))

