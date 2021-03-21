task_numbers = []
for i in range(1000):
    if i % 2 != 0:
        number = i ** 3
        task_numbers.append(number)
print(task_numbers)

sum = 0
task_sum = 0
for i in range(len(task_numbers)):
    sum = 0
    task_number = task_numbers[i]
    while task_number >= 10:
        sum += task_number % 10
        task_number //= 10
    else:
        sum += task_number
    if sum % 7 == 0:
        task_sum += task_numbers[i]
print(f'{task_sum} - сумма чисел по заданию 2.a')

for i in range(len(task_numbers)):
    task_numbers[i] += 17
print(task_numbers)

sum = 0
task_sum = 0
for i in range(len(task_numbers)):
    sum = 0
    task_number = task_numbers[i]
    while task_number >= 10:
        sum += task_number % 10
        task_number //= 10
    else:
        sum += task_number
    if sum % 7 == 0:
        task_sum += task_numbers[i]
print(f'{task_sum} - сумма чисел по заданию 2.b')
