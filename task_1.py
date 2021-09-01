num = int(input('Введите трехзначное число:'))
if num < 100 or num > 999:
    num = int(input('Введите трехзначное число:'))
print(num)
a = num // 100
b = (num % 100) // 10
c = num % 10
print (f'Сумма чисел - {a + b + c}, произведение - {a * b * c}')