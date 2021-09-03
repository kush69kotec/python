while True:
    print('Для остановки введите вместо арифметической операции ноль')
    num_one = float(input('Введите первое число: '))
    sign = input('Введите арифметическую операцию: ')
    if sign == '0':
        print('Конец')
        break
    while sign != '+' and sign != '-' and sign != '/' and sign != '*' and sign != '0':
        sign = input('Введите корректную арифметическую операцию: ')
    num_two = float(input('Введите второе число: '))
    if sign == '/' and num_two == 0:
        print('На ноль нельзя делить')
    elif sign == '+':
        result = num_one + num_two
        print(f'Результат: {result}')
    elif sign == '-':
        result = num_one - num_two
        print(f'Результат: {result}')
    elif sign == '/' and num_two != 0:
        result = num_one / num_two
        print(f'Результат: {result}')
    elif sign == '*':
        result = num_one * num_two
        print(f'Результат: {result}')


