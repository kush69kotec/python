import random

lv = int(input('Введите нижнюю границу(целое число)'))
hv = int(input('Введите верхнюю границу(целое число'))
while lv >= hv:
    print('Нижняя граница больше или равна верхней')
    lv = int(input('Введите нижнюю границу'))
    hv = int(input('Введите верхнюю границу'))
print(f'Случайное число в этом диапазоне: {random.randint(lv, hv)}')

lv = float(input('Введите нижнюю границу(вещественное число)'))
hv = float(input('Введите верхнюю границу(вещественное число'))
while lv >= hv:
    print('Нижняя граница больше или равна верхней')
    lv = float(input('Введите нижнюю границу'))
    hv = float(input('Введите верхнюю границу'))
print(f'Случайное вещественное число в этом диапазоне: {random.uniform(lv, hv)}')

letters = 'abcdefghijklmnopqrstuvwxyz'

lv = input('Введите букву с которой начинается диапазон')
hv = input('Введите букву которой заканчивается диапазон')
new_letters = letters[letters.index(lv):letters.index(hv) + 1]
while letters.index(lv) >= letters.index(hv):
    print('Неверный диапазон')
    lv = int(input('Введите нижнюю границу'))
    hv = int(input('Введите верхнюю границу'))
print(f'Случайная буква в этом диапазоне: {random.choice(new_letters)}')
