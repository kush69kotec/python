
numerals_translate = {
    'zero' : 'ноль',
    'one':'один',
    'two' : 'два',
    'three' : 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять'
}
def num_translate_adv(eng_numeral):
    if eng_numeral in numerals_translate:
        print(numerals_translate[eng_numeral])
    elif eng_numeral.istitle() == True:
        print(numerals_translate[eng_numeral.lower()].title())
    else:
        print('Ошибка, перевод выполнить невозможно', None)

num_translate_adv("Six")