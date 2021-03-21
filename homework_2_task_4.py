employ_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range(len(employ_list)):
    employ = employ_list[i][::-1]
    a = employ.index(' ')
    employ_list[i] = employ[:a:][::-1].lower().capitalize()
    print(f'Привет, {employ_list[i]} !')
