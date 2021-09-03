num_list = []
while True:
    user_num = input('Enter number(enter "stop" to stop enter:')
    if user_num == 'stop':
        break
    try:
        user_num = int(user_num)
        num_list.append(int(user_num))
    except Exception:
        print('Its not a natural number!')

if len(num_list) == 0:
    print('You did not enter any number')
else:
    max_num = str(max(num_list))
    num_sum = 0
    for num in max_num:
        num_sum += int(num)
    print(f'{max_num} is the biggest entered number and sum of its numbers is {num_sum}')

