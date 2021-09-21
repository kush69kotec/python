# Задача 5 из урока 3.

from random import randint
task_list = []
lower_zero = []
for i in range(20):
    task_list.append(randint(-10, 10))
print(task_list)

for elem in task_list:
    if elem < 0:
        lower_zero.append(elem)

max_lower_zero = max(lower_zero)
max_lower_zero_pos = lower_zero.index(max_lower_zero) + 1
print(f'max below zero element is {max_lower_zero}, and its index is {max_lower_zero_pos}')
print(task_list.__sizeof__())
print(lower_zero.__sizeof__())
print(max_lower_zero.__sizeof__())
print(max_lower_zero_pos.__sizeof__())

# В этой программе под переменные использовано 464 бита. Мне кажется, что это программа неэффективна, так как
# видится возможным сокращение количества переменных для освобождения оперативной памяти.