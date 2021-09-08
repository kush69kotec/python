from random import random
list_one = []
for i in range(10):
    list_one.append(int(random() * 100))

print(list_one)
hv = list_one.index(max(list_one))
lv = list_one.index(min(list_one))
list_one[hv], list_one[lv] = list_one[lv], list_one[hv]
print(list_one)


