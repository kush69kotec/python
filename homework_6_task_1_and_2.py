result = []


# функция для конвертирования изначальной строки файла логов в нужный нам вид
def line_convert():
    end_ip_index = line.find(' -')
    type_index_start = line.find('"')
    type_index_end = line.find(' /')
    resource_index_end = line.find('HT')
    return line[: end_ip_index], line[type_index_start + 1: type_index_end],
    line[type_index_end: resource_index_end]


# функция для нахождения ключа значения IP, с которого было больше всего запросов
def find_spammer():
    spam_values = list(spam.values())
    spam_keys = list(spam.keys())
    return spam_keys[spam_values.index(max(spam_values))]


with open('nginx_logs.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        result.append(line_convert())

print(*result, sep='\n')
print(f'Мы создали список запросов состоящий из кортежей, доказываю - {type(result)}')
spam = {}
#  здесь мы создаём словарь, в котором ключи - IP запроса, а значения - количество запросов с этого ID
for elem in result:
    if elem[0] in spam:
        spam[elem[0]] += 1
    else:
        spam[elem[0]] = 1

spammer = find_spammer()
print(f'Спаммером является IP {spammer}, количество запросов с этого адреса равно {spam[spammer]}')
