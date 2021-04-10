from sys import argv
from sys import exit
position = int(argv[1])
new_sale = (argv[2] + '\n').encode()
with open('bakery.csv', 'r+b') as f:
    binary_text = bytearray()
    for i in range(position - 1):
        line = f.readline()
        binary_text.extend(line)
    if f.readline() == b'':
        exit("Неверный параметр")
    else:
        binary_text.extend(new_sale)
        while True:
            chunk = f.read(256)
            if not chunk:
                break
            binary_text.extend(chunk)
    with open('bakery.csv', 'w') as f:
        f.write(binary_text.decode(encoding='utf-8'))
