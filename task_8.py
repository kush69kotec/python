sum_result = 0
i = 0
n = int(input('Enter "n": '))
while i != n:
    i += 1
    sum_result += i
    print(f'{sum_result = }, {n = }')
else:
    print(f'{sum_result} = {n * (n + 1) / 2}')
