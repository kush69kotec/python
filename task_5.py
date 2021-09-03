table = ''
row = ''
for char in range(32, 128):
    row += f'{char}:{chr(char)}\t'
    if (char - 31) % 10 == 0:
        table += f'{row}\n'
        row = ''
print(table)
