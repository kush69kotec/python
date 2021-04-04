tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А',
]


def gen(first_list, second_list):
    for i in range(len(first_list)):
        if i > (len(second_list) - 1):
            yield first_list[i], None
        else:
            yield first_list[i], second_list[i]


pairs = gen(tutors, klasses)
print(type(pairs))
for i in range(len(tutors) + 1):
    print(next(pairs))
