def thesaurus(*args):
    names_first_letter = []
    # создаю пустой список, в котором буду хранить первые буквы имён
    final_dict = {}
    # создаю пустой словарь, который буду возвращать в конце функции
    for arg in args:
        names_first_letter.append(arg[0])
        # создал список с первыми буквами имён
    final_dict = final_dict.fromkeys(
        names_first_letter)
    # преобразовал список с буквами в словарь с аналогичными ключами
    for key in final_dict:
        final_dict[key] = []
        # первый уровень цикла - работаем с ключами в итоговом словаре
        for arg in args:
            # второй уровень цикла - работаем с ключами в словаре и заданными аргументами
            if key in arg:
                final_dict[key].append(arg)
                # проверяем начинается ли какой-нибудь из заданных аргументов с ключа в словаре
    print(final_dict)


thesaurus("Иван", "Мария", "Петр", "Илья")

