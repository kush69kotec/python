from random import randint
tables_num = 6
rows_num = 8
matrix = []
for i in range(rows_num):
    row = []
    for j in range(tables_num):
        row.append(randint(0, 20))
    matrix.append(row)
print(matrix)
for row in matrix:
    for elem in row:
        print(elem, end='\t')
    print('\n')

min_elem_in_table_list = []
for i in range(tables_num):
    min_elem = matrix[0][i]
    for j in range(rows_num):
        if matrix[j][i] < min_elem:
            min_elem = matrix[j][i]
    min_elem_in_table_list.append(min_elem)

print(min_elem_in_table_list)


