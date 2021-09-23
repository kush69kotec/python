from random import uniform


def merge_lists(left, right):
    final = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            j += 1
    if i < len(left):
        final += left[i:]
    if j < len(right):
        final += right[j:]

    return final


def merge_sort(lst):
    if len(lst) == 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge_lists(left, right)


ary = []
N = int(input('enter list size: '))
for i in range(N):
    ary.append(round(uniform(0, 50), 2))

print(ary)
print(merge_sort(ary))
