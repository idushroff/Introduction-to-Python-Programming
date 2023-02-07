# Input function

name = input("What is your name? ")
age = input("What is your age? ")
print("I know that", name, "is", age, "years old!")

# Worksheet 4 notes:
# list[start:end:step]
# String slicing and dicing :


text = input("How much did you spend?: ")
total_cost = 100 * int(text[1:3]) + int(text[4:6])
print(total_cost)
number = int(text[-3:-1])
print(number)
cost = total_cost // number
print(cost)
cents = cost % 100
print(cents)
if cents >= 10:
    print(str(cost//100))
    print("$" + str(cost//100) + "." +  str(cents))
else:
    print("$" + str(cost//100) + ".0" +  str(cents))


# Why is this solution not valid?
text = input("How much did you spend?: ")
total_cost = 100 * int(text[1:3]) + int(text[4:6])
print(total_cost)
number = int(text[-3:-1])
print(number)
cost = total_cost // number
print(cost)
cents = cost % 100
print(cents)
if cents >= 10:
    print(str(cost//100))
    print("$" + str(cost//100) + "." +  str(cents))
else:
    print("$" + str(cost//100) + ".0" +  str(cents))

# Worksheet 4: The culprit: Method 1:

a = [("Max Zorin", "Kills with guns", "Chip Tycoon"), ("Hugo Drax",), ("Jaws", "Bites people", "Mutant"),("Nick Nack", "Really short"),("Le Chiffre", "Good at poker", "Really evil"),("Francisco Scaramanga", "Has a Golden Gun", "Probably will melt"),("Mr Big", "Also the name of a rock band", "Dictator of San Monique")]

b = int(input("WHO DID IT HUGO!? "))
if b == 7:
    print("It was", a[0][0])
    print("Data:", a[0][1:])
else:
    print("It was", a[b][0])
    print("Data:", a[b][1:])

# Worksheet 4: The culprit: Method 2:
a = [("Max Zorin", "Kills with guns", "Chip Tycoon"), ("Hugo Drax",), ("Jaws", "Bites people", "Mutant"),("Nick Nack", "Really short"),("Le Chiffre", "Good at poker", "Really evil"),("Francisco Scaramanga", "Has a Golden Gun", "Probably will melt"),("Mr Big", "Also the name of a rock band", "Dictator of San Monique")]
b = int(input("WHO DID IT HUGO!? "))
c = b % 7
print("It was", a[c][0])
print("Data:", a[c][1:])
# def dodgy_inventorise(i, p, v):
#     return f"{i[0]:<20.20}{p[1]:10.2f}{v[2]:>6}"
#
# item = "rust bucket car"
# price = 1500000.00
# volume = 1
# print(dodgy_inventorise("rust bucket car", 150000, 1))
#
# def cookie_cook(cook):
#     return f('How many cookies could a', cook, 'cook if a good cook could cook cookies')
# print(cookie_cook("Tasmanian cook"))


def cookie_cook(string):
    if string startswith('a' or 'e' or 'i' or 'u'):
        return 'How many cookies could an {} cook if a good cook could cook cookies'.format(string)
    else:
        return 'How many cookies could a {} cook if a good cook could cook cookies'.format(string)

print(cookie_cook(string))

# Worksheet 6 - Goldilocks List
def between_len(word_list, minlen, maxlen):
    return minlen <= len(word_list) <= maxlen

print(between_len(["python", "is", "boring"], 4, 7))
# False
print(between_len(["python", "is", "amazing"], -1, 20))
# True
print(between_len(["python", "is", "amazing"], minlen=3, maxlen=4))
# True

# Worksheet 6 - Word counter
def word_count(input_str):
    return len(input_str.split())
>>> word_count("There are 44 cows on a hill")
# 7
>>> word_count("Quotes are handy things to have about, saving one from thinking for oneself which is always hard.")
# 17
>>> word_count("")
# 0

# Worksheet 7 - chess problem v2
def check_move(column, row):
    if len(column) == 1 and 'A' <= column <= 'H' and 1 <= row <= 8:
        return f'The piece is moved to {column}{row}.'
    else:
        return 'The position is not valid.'
print(check_move('b'.upper(), 4))

# The above solution didn't work b/c actual solution has no print command
# Therefore here is solution option 1:
def check_move(column, row):
    upper_column = column.upper()
    if len(column) == 1 and 'A' <= upper_column <= 'H' and 1 <= row <= 8:
        return f'The piece is moved to {upper_column}{row}.'
    else:
        return 'The position is not valid.'

# here is solution option 2:
def check_move(column, row):
    upper_column = column.upper()
    if len(column) == 1 and upper_column in 'ABCDEFGH' and 1 <= row <= 8:
        return f'The piece is moved to {upper_column}{row}.'
    else:
        return 'The position is not valid.'

# Chess problem v3
def check_move(column, row):
    upper_column = column.upper()
    if len(column) == 1 and upper_column not in 'abcdefghABCDEFGH':
        return 'The column value is not in the range a-h or A-H!'
    if row not in range(1,9):
        return 'The row value is not in the range 1 to 8!'
    elif len(column) == 1 and upper_column in 'ABCDEFGH' and 1 <= row <= 8:
        return f'The piece is moved to {upper_column}{row}.'
>>> check_move('I', 4)
'The column value is not in the range a-h or A-H!'
>>> check_move('F', 9)
'The row value is not in the range 1 to 8!'
>>> check_move('I', 9)
'The column value is not in the range a-h or A-H!'
>>> check_move('B', 4)
'The piece is moved to B4'

# chess problem #4



'grok worksheet 9 Q: longest word method 1''
def longest_sentence_length(text):
    text = text.split('. ')
    z = 0
    count = []
    while z in range(len(text)):
        sentence = text[z]
        sentence = sentence.split(' ')
        x = 0
        i = 0
        for word in range(len(sentence)):
            word = sentence[i]
            i += 1
            x += 1
        z += 1
        count.append(x)
    x = sorted(count, reverse = True)
    return x[0]


text = 'Hello world. My name is Plargleflarp.'
print(longest_sentence_length(text))


