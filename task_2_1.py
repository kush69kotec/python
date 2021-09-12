import cProfile
n = int(input('Enter your num: '))


def main():
    result_list = []
    counter = 0
    for i in range(2, n + 1):
        for j in result_list:
            if i % j == 0:
                break
        else:
            result_list.append(i)
    print(result_list)


cProfile.run('main()')

