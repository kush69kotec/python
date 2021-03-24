import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(count, repeat_enable_or_disable = 'repeat_enable'):
    """ Функция get_jokes имеет 2 аргумента:
    1)количество комбинаций, созданных путём случайного выбора элементов из каждой последовательности и объединения их
    в элемент списка
    2)флажок значение которого либо "repeat_enable"-разрешающее любое количество использований элементов, заданных
    последовательностей, либо "repeat_disable"-запрещающее больше одного раза использовать элемент
    каждой последовательности
    :param count:
    :param repeat_enable_or_disable:
    """

    jokes_list = []
    # создаётся список, который будет состоять из заданного количества комбинаций
    i = 0
    # задаётся переменная i для контроля количества комбинаций
    if count > len(nouns):
        return print('Число шуток превышает количество слов в заданном списке')
    # проверка заданного количества комбинаций, вывод сообщения о возможной ошибке
    elif repeat_enable_or_disable == 'repeat_enable':
        while i < count:
            jokes_list.append(f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}')
            i += 1
    # в случае, если разрешёно повторение выполняется генерация нужного числа последовательностей методом f'string'
    elif repeat_enable_or_disable == 'repeat_disable':
        while i < count:
            # в случае если повторение запрещено в цикле при каждой итерации случайно выбираются элементы из
            # последовательностей методом random.choice
            noun = random.choice(nouns)
            adverb = random.choice(adverbs)
            adjective = random.choice(adjectives)
            jokes_list.append(
                f'{nouns.pop(nouns.index(noun))} {adverbs.pop(adverbs.index(adverb))} '
                f'{adjectives.pop(adjectives.index(adjective))}')
            # с целью неповторения использования элементов заданных последовательностей, внутри метода f'string'
            # используется метод list.pop, чтобы убрать из последовательности конкретный элемент, индекс которого
            # узнаётся методом str.index()
            i += 1
        print(jokes_list)



get_jokes(5, "repeat_disable")
