from random import random
import cProfile


def main():
    task_list = []
    for i in range(1000000):
        task_list.append(int(random() * 100))
    max_count = 0
    i = 0
    n = 0
    max_elem = 0
    list_length = len(task_list)
    while i < list_length:
        elem = task_list[i]
        count = 0
        n = 0
        while n < list_length:
            if task_list[n] == elem:
                count += 1
                task_list.pop(n)
                list_length -= 1
            else:
                n += 1
        else:
            if count > max_count:
                max_count = count
                max_elem = elem

    else:
        print(f'{max_elem} : {max_count}')


cProfile.run('main()')

# При анализе этого алгоритма я выяснил, что он значительно медленнее первого, а в определённый момент
# увеличения входных данных время выполнения вырастает настолько, что я даже не дождался пока он выполнится до конца.
# Соответственно его сложность даже не кубическая, а вообще какая то заоблочная.
