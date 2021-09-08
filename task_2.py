from random import random
list_one = []
list_two = []
for i in range(10):
    list_one.append(int(random() * 100))

i = 0
for elem in list_one:
    if elem % 2 == 0:
        list_two.append(list_one.index(elem))

print(list_one)
print(list_two)