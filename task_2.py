import collections

symb = '0123456789ABCDEF'
symb_dict = collections.defaultdict(int)
counter = 0
for i in symb:
    symb_dict[i] = counter
    counter += 1


def to_hex(number):
    hex_number = collections.deque()
    while number > 0:
        remainder = number % 16
        for i in symb_dict:
            if symb_dict[i] == remainder:
                hex_number.append(i)
        number //= 16
    hex_number.reverse()
    return list(hex_number)


def to_dex(string_number):
    dex = 0
    number = collections.deque(string_number)
    number.reverse()
    for i in range(len(number)):
        dex += symb_dict[number[i]] * (16 ** i)
    return dex


number_one = to_dex(input('Enter your first hex number:'))
number_two = to_dex(input('Enter your second hex number:'))

print(f'summ is {to_hex(number_one + number_two)}, product is {to_hex(number_one * number_two)}')