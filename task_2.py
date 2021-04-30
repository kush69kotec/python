class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите делимое'))
b = int(input('Введите делитель'))
try:
    if b == 0:
        raise MyException('Вы что пытаетесь делить на ноль? Серьёзно?')
    c = a / b
except MyException as err:
    print(err)
