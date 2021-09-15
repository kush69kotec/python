import collections
avrg_income = 0
companies = {}
higher_avrg = []
lower_avrg = []
n = int(input('Enter num of companies: '))

for i in range(n):
    name = input('company name: ')
    companies[name] = collections.defaultdict(int)
    year_income = 0
    for j in range(4):
        companies[name][j + 1] = (int(input(f'enter {j + 1} quarter income')))
        year_income += companies[name][j + 1]
    companies[name]['year_income'] = year_income
    avrg_income += year_income

avrg_income //= n

for elem in companies:
    if companies[elem]['year_income'] > avrg_income:
        higher_avrg.append(elem)
    elif companies[elem]['year_income'] < avrg_income:
        lower_avrg.append(elem)

print('Companies with lower than average income are: ')
for i in lower_avrg:
    print(i)

print('Companies with higher than average income are: ')
for i in higher_avrg:
    print(i)



