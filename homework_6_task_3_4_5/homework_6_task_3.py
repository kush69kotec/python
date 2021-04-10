import sys  # чит для вывода кода "1" в завершении программы

people_dict = {}
# форматируем строки с данными о пользователях и создаём словарь с ключами - ФИО пользователей и значением None
with open('homework_6_task_3_4_5/users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        info_line = line.replace(',', ' ').replace('\n', '')
        people_dict[info_line] = None
# в этой адской конструкции мы создаём счетчик повторений цикла, чтобы в случае, если пользователей меньше, чем хобби
# прервать выполнение скрипта, а в случае, если хобби меньше - оставить значения None
i = 0
file_1 = open('homework_6_task_3_4_5/hobby.csv', 'r', encoding='utf-8')
for key in people_dict:
    hobby_line = file_1.readline().strip()
    i += 1
    if i >= len(people_dict) and len(hobby_line) != 0:
        sys.exit(1)
    elif len(hobby_line) != 0:
        people_dict[key] = hobby_line
file_1.close()

# записываем результат в текстовый файл
print(people_dict)
with open('homework_6_task_3_4_5/result_task_3.txt', 'w', encoding='utf-8') as result_file:
    result_file.write(str(people_dict))
