result_list = [0, 0, 0, 0, 0, 0, 0, 0]
elem = 0
for i in range(2, 100):
    elem = 0
    for n in range(2, 10):
        if i % n == 0:
            result_list[elem] += 1
            elem += 1
        else:
            elem += 1

for i in range(len(result_list)):
    print(f'Кратных {i + 2} чисел: {result_list[i]}')
