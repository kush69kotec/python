while True:
    user_num = input('enter your number')
    try:
        int_user_num = int(user_num)
        break
    except Exception:
        print('not number entered, try again')
even_nums = 0
not_even_nums = 0
for num in user_num:
    if int(num) % 2 == 0:
        even_nums += 1
    else:
        not_even_nums += 1

print(f"there's {even_nums} even nums and {not_even_nums} not even nums in your number")
