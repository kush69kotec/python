from random import randint
task_list = []
for i in range(20):
    task_list.append(randint(0, 20))
print(task_list)

min_idx = task_list.index(min(task_list))
max_idx = task_list.index(max(task_list))

if min_idx < max_idx:
    cut = task_list[min_idx + 1: max_idx]
    print(cut)
else:
    cut = task_list[max_idx + 1: min_idx]
    print(cut)

print(f'sum of elements in cut list is {sum(cut)}')

