from sys import argv
from sys import exit

# словарь с результатом функии по заданию. я выбрал словарь, так как мне кажется, что использование доступа по ключу,
# в виде фамилии наиболее практично, а данные словаря представленные в кортеже занимают меньше места я считаю.
people_dict = {}


# я создал функцию, для обработки файлов с данными о пользователях, данными об их хобби и адресом файла,
# куда записывается вывод функции. Значения аргументов по умолчанию файлы созданные внутри папки со скриптом. Функция
# протестирована на случай, если все файлы хранятся в разных папках
# ПЕРВЫЙ ПАРАМЕТР - АДРЕСС ФАЙЛА С ФИО
# ВТОРОЙ ПАРАМЕТР - АДРЕСС ФАЙЛА С ИНФОРМАЦИЕЙ О ХОББИ
# ТРЕТИЙ ПАРАМЕТР - АДРЕСС ФАЙЛА, В КОТОРЫЙ НУЖНО ЗАПИСАТЬ РЕЗУЛЬТАТ.
def result_dict(first_address='users.csv', second_address='hobby.csv',
                third_address='result.csv'):
    with open(first_address, 'r', encoding='utf-8') as f:
        for line in f:
            people_dict[line[:line.index(',')]] = tuple(line.replace('\n', '').split(','))
    f = open(second_address, 'r', encoding='utf-8')
    for key in people_dict:
        hobby_line = f.readline().strip()
        if len(hobby_line) != 0:
            people_dict[key] += tuple(hobby_line.split(','))
        else:
            people_dict[key] += (None,)
    f.close()
    print(people_dict)
    with open(third_address, 'w', encoding='utf-8') as f:
        f.write(str(people_dict))


# проверка на наличие параметров при запуске скрипта из терминала
args_list = [str(elem) for elem in argv[1:]]
try:
    if len(argv) == 1:
        result_dict()
    elif len(argv) == 2:
        result_dict(args_list[0])
    elif len(argv) == 3:
        result_dict(args_list[0], args_list[1])
    elif len(argv) == 4:
        result_dict(args_list[0], args_list[1], args_list[2])
except Exception:
    exit('Неверные параметры')
