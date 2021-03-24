def thesaurus(*args):
    names_start = []
    dict = {}
    names = []
    for arg in args:
        names_start.append(arg[0])
        names.append(arg)
    dict = dict.fromkeys(names_start)
    for key in dict:
        dict[key] = []
        for arg in args:
            if arg[0] == key:
                dict[key].append(arg)
    return dict


"""
Функция thesaurus(*args) работает аналогично написанной в задании №3, кроме того, что в конце
вместо того, чтобы выводить значение словаря на экран, она возвращает его. Сделано это для её использования 
в функции thesaurus_adv.
"""


def thesaurus_adv(*args):
    dict_first_letter_names = thesaurus(*args)
    # словарь, в котором ключи-первые буквы имён людей,
    # а значения-списки из имён и фамилий тех людей,
    # у которых имя начинается с ключа
    surnames = []
    for arg in args:
        surnames.append(arg[arg.index(' ') + 1:][0])  # здесь я создаю список из первых букв фамилий,
        # для дальнейшего создания словаря
        dict_adv = dict.fromkeys(surnames)
        # создаётся словарь с ключами из списка первых букв фамилий
    for key_adv in dict_adv:
        dict_adv[key_adv] = {}
        # создаётся словарь, в котором ключи будут первыми буквами фамилий людей , а значения словари с ключами,
        # являющимися первыми буквами имён людей, а значения - имена и фамилии людей,
        # при условии, что имя начинается с ключа, но к первому ключу они присовокупляются только при условии,
        # что фамилия человека начинается с первого ключа
        for key in dict_first_letter_names:
            # входим в цикл первого уровня для перебора ключей значений последовательности имён и фамилий, в которых
            # имя начинается с ключа
            for surname in dict_first_letter_names[key]:
                # входим в цикл второго уровня для перебора фамилий в последовательности, являющейся значением ключа,
                # указанного в предыдущем входе в цикл
                if surname[surname.index(' ') + 1:][0] == key_adv:
                    empty_dict = {}
                    # создаётся пустой словарь, единственной парой "ключ-значение" которого является пара, которую
                    # необходимо добавить в целевой словарь функции, путём применения метода "dict.update()
                    empty_dict[key] = dict_first_letter_names[key]
                    dict_adv[key_adv].update(empty_dict)
                    break
    dict_keys_list = list(dict_adv.keys())
    # для сортировки словаря по ключам создаётся список, состоящий из ключей
    dict_keys_list.sort()
    # сортируется
    final_dict = {}
    for dict_key in dict_keys_list:
        final_dict[dict_key] = dict_adv[dict_key]
    # создаётся финальный словарь для вывода, отсортированный по ключам
    print(final_dict)

thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
