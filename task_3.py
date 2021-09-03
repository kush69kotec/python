while True:
    user_num = input('Enter your number(enter zero to stop): ')
    if user_num == '0':
        break
    else:
        print(f'Your reversed number is {user_num[::-1]}')
