price_list = [10, 15.45, 9, 42.55, 16, 9.99, 25.50, 55, 98, 83.15, 50.50, 25.35, 18, 36, 99.99]
print(f'{price_list} - исходный список')


for i in range(len(price_list)):
    a = str(price_list[i])
    if '.' not in a:
        price_list[i] = f'{a} руб 00 коп'
    elif '.' in a and len(a[a.index('.') + 1:]) < 2:
        price_list[i] = f'{a[:a.index(".")]} руб {a[a.index(".") + 1:]}0 коп'
    elif '.' in a and len(a[a.index('.') + 1:]) == 2:
        price_list[i] = f'{a[:a.index(".")]} руб {a[a.index(".") + 1:]} коп'

print('Ниже будет изменённый список, преобразованный в денежный формат')
print(price_list)

print('Ниже будет строчка, содержащая элементы списка в денежном формате')
print(', '.join(price_list))
print(f'{id(price_list)} - идентификатор нашего списка')

for i in range(len(price_list)):
    a = price_list[i]
    if len(a[:a.index(" руб")]) == 1:
        price_list[i] = "0" + a
        price_list = sorted(price_list)
for i in range(len(price_list)):
    a = price_list[i]
    if '0' in a and a.index('0') == 0:
        price_list[i] = a.replace('0', '', 1)
    else:
        i += 1
print(price_list)
print(f'{id(price_list)} - идентификатор нашего отсортированного списка - '
              f'мы видим, что это тот же самый объект')
print(', '.join(price_list))

price_list_max_to_min = price_list[::-1]
print('Сейчас будет список отсортированный по убыванию')
print(price_list_max_to_min)

print('А сейчас пятёрка самых дорогих товаров по возрастанию:')
for price in price_list[:-6:-1][::-1]:
    print(price)
