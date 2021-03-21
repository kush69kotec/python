import copy
# первый вариант решения с заданием переменной, которая хранит строку которую нужно в итоге получить
# не сказать, чтобы очень изящное решение, но с задачей справляется
meteo_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
step = 0
task_string = ''
while step < len(meteo_words):
    a = meteo_words[step]
# на просторах альтернативных источников я наткнулся на try, exception и решил попробовать реализовать
# задание таким образом, мне понравилась сама идея, к тому же не было сказано что можно использовать,
# а что нет :)
    try:
        b = int(meteo_words[step])
    except ValueError:
        step += 1
        task_string += a + ' '
    else:
        if 1 <= b < 10 and len(a) > 1 and '0' not in a or b < 1:
            meteo_words[step] = (a[:1] + '0' + a[1:])
            meteo_words.insert(step + 1, '"')
            meteo_words.insert(step, '"')
            task_string += '"' + meteo_words[step + 1] + '" '
            step += 3
        elif b >= 10:
            meteo_words[step] = a
            meteo_words.insert(step + 1, '"')
            meteo_words.insert(step, '"')
            task_string += '"' + meteo_words[step + 1] + '" '
            step += 3
        elif b < 10:
            meteo_words[step] = ('0' + a)
            meteo_words.insert(step + 1, '"')
            meteo_words.insert(step, '"')
            task_string += '"' + meteo_words[step + 1] + '" '
            step += 3

print(meteo_words)
print(task_string)

# pussy вариант решения задачи, не придумал как ещё использовать метод replace,
# чтобы получилось универсально:)
task_string_second = ' '.join(meteo_words)
print(task_string_second)
task_string_second = task_string_second.replace('в " ', 'в "', 2).replace(' " ', '" ', 2).replace(' " ',' "', 1).replace(' " ','" ')
print(f'{task_string_second} строка')

# и ещё такой вариант с изменением исходного списка, добавил переменную keep_var
# для хранения исходного списка
keep_var = copy.copy(meteo_words)
for i in range((len(meteo_words) + 1)):
    if meteo_words[i] == '"':
        meteo_words[i + 1] = '"' + meteo_words[i + 1] + '"'
        del meteo_words[meteo_words.index('"') + 2]
        del meteo_words[meteo_words.index('"')]
    elif '"' not in meteo_words:
        break
print(' '.join(meteo_words))

meteo_words = keep_var

