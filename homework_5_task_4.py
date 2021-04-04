# самый очевидный метод рещения методом append и списка

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
for i in range(1, len(src) - 1):
    if src[i] > src[i - 1]:
        result.append(src[i])
print(result)

# что вполне можно привести к такому виду
result = [src[i] for i in range(1, len(src)) if src[i] > src[i - 1]]

# далее оптимизируем выполнение кода по скорости с помощью генератора и выводим полученные значения
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[i] for i in range(1, len(src)) if src[i] > src[i - 1])
for i in range(6):  # написал 6 просто чтобы было сразу видно, что выводятся те же значения
    print(next(result))

# и оптимизируем выполнение по памяти с помощью множества:
result = {src[i] for i in range(1, len(src)) if src[i] > src[i - 1]}
print(list(result))
