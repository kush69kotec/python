tables_num = 5
rows_num = 4
matrix = []
for i in range(rows_num):
    row = []
    for j in range(tables_num - 1):
        while True:
            try:
                num = int(input('enter your num: '))
                break
            except Exception:
                print('reenter your num!')
        row.append(num)
    row.append(sum(row))
    matrix.append(row)

for row in matrix:
    for elem in row:
        print(elem, end='\t')
    print('\n')
