# У меня 2 варианта решения, практически идентичные, но первый несколько более понятен. Очень большая просьба
# конкретно это задание прокомментировать - что Вы думаете по поводу моего решения.
# 1 вариант
from random import random
task_list = []
counted_list =[]
for i in range(5):
    task_list.append(int(random() * 3))
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
print(f'{max_elem} : {max_count}')

# 2 вариант
# у меня почему то есть ощущение, что, возможно, он менее ресурсозатратный
from random import random
task_list = []
# Создаём массив
for i in range(5):
    task_list.append(int(random() * 3))
print(task_list)
# Создаём переменные максимального счета и наиболее часто встречающегося числа и переменные для двух циклов,
# а также переменную для длинны списка
max_count = 0
i = 0
n = 0
max_elem = 0
list_length = len(task_list)
# В цикле i всегда 0, но для понятности я выношу её отдельно в переменную
# Счетчик и вторая переменная цикла обнуляются при каждой итерации
while i < list_length:
    elem = task_list[i]
    count = 0
    n = 0
    while n < list_length:
        # В случае совпадения значения элементов счетчик увеличивается а сам элемент массива удаляется,
        # чтобы не проверять его в дальнейшем, также переменная, хранящая длину списка уменьшается на 1.
        if task_list[n] == elem:
            count += 1
            task_list.pop(n)
            list_length -= 1
        else:
            # В случае несовпадения - переходим к следующему элементу.
            n += 1
    else:
        # При завершении вложенного цикла проверяем не больше ли наш счетчик максимального ранее,
        # при первой итерации он и является максимальным, поэтому записываем его в переменную max count
        if count > max_count:
            max_count = count
            max_elem = elem

else:
    print(f'{max_elem} : {max_count}')

