companies = {}
n = int(input('Enter num of companies: '))
total_income = 0
for i in range(n):
    cname = input('Enter company name:')
    year_income = 0
    for j in range(4):
        quart_income = int(input(f'enter income in {j + 1} quarter: '))
        year_income += quart_income
    average_income = year_income // 4
    companies[cname] = average_income
    total_income += average_income

total_avrg = total_income // n
lower_avrg = {}
higher_avrg = {}
for i in companies:
    if companies[i] > total_avrg:
        higher_avrg[i] = companies[i]
    elif companies[i] < total_avrg:
        lower_avrg[i] = companies[i]

print('Companies with lower than average income are: ')
for i in lower_avrg:
    print(i)

print('Companies with higher than average income are: ')
for i in higher_avrg:
    print(i)