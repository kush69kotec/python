from sys import argv
max_sale_length = 8
with open('bakery.csv', 'a', encoding='utf-8') as f:
    num_of_spaces = max_sale_length - len(argv[1])
    f.write(argv[1] + num_of_spaces * ' ')
    f.write('\n')
