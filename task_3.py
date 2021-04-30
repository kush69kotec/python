num_list = []


class StringException(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        elem = input('Введите число (введите stop для завершения): ')
        if elem == 'stop':
            break
        else:
            try:
                elem = int(elem)
                num_list.append(elem)
                print(num_list)
            except ValueError:
                raise StringException('Не строка')
    except StringException as err:
            print(err)





