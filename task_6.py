letters = 'abcdefghijklmnopqrstuvwxyz'
letter_num = int(input('Введите порядковый номер буквы: ')) - 1
while letter_num < 0 or letter_num > 26:
    print('Вы ввели некорректное число, введите число больше 0 и меньше 26')
    letter_num = int(input('Введите порядковый номер буквы: ')) - 1
print(f'Буква под порядковым номером {letter_num + 1} это {letters[letter_num]}')

