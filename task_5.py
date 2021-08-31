letters = 'abcdefghijklmnopqrstuvwxyz'
lv = input('Введите букву с которой начинается диапазон').lower()
hv = input('Введите букву которой заканчивается диапазон').lower()
while letters.index(lv) >= letters.index(hv) or lv not in letters or hv not in letters:
    print('Введите диапазон заново')
    lv = input('Введите букву с которой начинается диапазон').lower()
    hv = input('Введите букву которой заканчивается диапазон').lower()
print(f'Первая ваша буква находится на {letters.index(lv) + 1} позиции, вторая - на {letters.index(hv) + 1} '
      f'позиции\nМежду ними {letters.index(hv) - letters.index(lv)} букв')