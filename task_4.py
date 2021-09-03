n = int(input('Enter num of divisions'))
result = 1
for i in range(n):
    result = result * (-0.5)
print(f'Your result is {result}')



# Лично мне больше нравится вариант решения функцией
# def task_function(n):
#     result = 1
#     for i in range(n):
#         result = result * (-0.5)
#     return result
#
#
# print(task_function(0))

