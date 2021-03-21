user_number=int(input('Введите количество процентов от 1 до 20: '))
if user_number == 1:
    print(f'{user_number} процент')
elif 1< user_number < 5:
    print(f'{user_number} процента')
else:
    print(f'{user_number} процентов')

print('Все склонения для проверки:')

for user_number in range(20):
    if user_number == 1:
        print(f'{user_number} процент')
    elif 1 < user_number < 5:
        print(f'{user_number} процента')
    else:
        print(f'{user_number} процентов')