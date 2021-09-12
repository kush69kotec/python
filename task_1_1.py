from random import random
import cProfile


def main():
    task_list = []
    counted_list = []
    for i in range(1000000):
        task_list.append(int(random() * 100))
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
    print(f'{max_elem} : {max_count}')


cProfile.run('main()')

# Используя библиотеку cProfile я проанализировал этот алгоритм и могу сказать, что он линейной сложности,
# потому что при увеличении количества входных данных в 10 раз, время его выполнения вырастает в 10 раз.