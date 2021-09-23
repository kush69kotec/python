from random import randint
lst = []
m = int(input('enter m: '))
for i in range(2 * m + 1):
    lst.append(randint(0, 5))

print(lst)


for i in range(len(lst)):
    med = lst[i]
    lower = []
    higher = []
    for elem in lst:
        if elem < med:
            lower.append(elem)
        elif elem > med:
            higher.append(elem)
        else:
            lower.append(med)
            higher.append(med)
    if len(lower) == len(higher):
        print(f'median is {med}')
        break
print('there is no median')

print(lower)
print(higher)
