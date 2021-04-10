from sys import argv
from sys import exit

try:
    arg_list = [int(elem) for elem in argv[1:]]
except ValueError:
    exit('Неверные параметры')
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(argv) == 1:
        for line in f:
            print(line.strip())
    elif len(argv) == 2:
        for i in range(arg_list[0] - 1):
            f.readline()
        for line in f:
            print(line.strip())
    elif len(argv) == 3:
        for i in range(arg_list[0] - 1):
            f.readline()
        for i in range(arg_list[1] - arg_list[0] + 1):
            print(f.readline().strip())
    else:
        exit('Неверные параметры')
