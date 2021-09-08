from random import randint

task_list = []
for i in range(20):
    task_list.append(randint(0, 20))
print(task_list)

min_elem_one = min(task_list)
min_idx = task_list.index(min_elem_one)
print(task_list[:min_idx] + task_list[min_idx + 1:])
if min_idx > 0:
    min_elem_two = min(task_list[:min_idx] + task_list[min_idx + 1:])
    print(f'Min elements are {min_elem_one} and {min_elem_two}')
else:
    min_elem_two = min(task_list[min_idx + 1:])
    print(f'Min elements are {min_elem_one} and {min_elem_two}')

