from random import random
guessed_num = int(random() * 100)
i = 0
while True:
    user_num = int(input("What's the guessed number?"))
    i += 1
    if i >= 10:
        print('You have no tries left')
        break
    if user_num < guessed_num:
        print('Your number is too small')
    elif user_num > guessed_num:
        print('Your number is too big')
    elif user_num == guessed_num:
        print("That's it! You won!")
