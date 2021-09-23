from random import randint
ary = []
N = int(input('enter list size: '))
for i in range(N):
    ary.append(randint(-100, 100))


def reversed_bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


print(ary)
print(reversed_bubble_sort(ary))
