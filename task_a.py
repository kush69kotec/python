# Задание 4 из урока 3.

from random import random

task_list = []
counted_list = []
for i in range(10):
    task_list.append(int(random() * 10))
print(task_list)
max_elem = 0
max_count = 0
for elem in task_list:
    if elem not in counted_list:
        count = task_list.count(elem)
        if count > max_count:
            max_count = count
            max_elem = elem
        counted_list.append(elem)
    else:
        continue
print(task_list.__sizeof__())
print(counted_list.__sizeof__())
print(max_elem.__sizeof__())
print(max_count.__sizeof__())
print(f'{max_elem} : {max_count}')

# В результате выполнения программы мы видим, что на переменные суммарно затрачено 232 бита памяти. Количество
# использованной памяти напрямую зависит от размера начального списка, а поскольку в задании было указано,
# что как раз со списком и нужжно работать, то я считаю, что программа довольно эффективна, посколько выводные данные
# всегда имеют одно количество использованной памяти
