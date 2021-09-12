import cProfile

n = int(input('enter your num'))


def main():
    result_list = [0] * n
    for i in range(n):
        result_list[i] = i

    result_list[1] = 0

    m = 2
    while m < n:
        if result_list[m] != 0:
            j = m * 2
            while j < n:
                result_list[j] = 0
                j = j + m
        m += 1

    final_list = []
    for i in result_list:
        if result_list[i] != 0:
            final_list.append(result_list[i])

    del result_list


cProfile.run('main()')

# Мы видим что этот алгоритм значительно проще и быстрее выполняется, чем без использования "решета Эратосфена".
# Он имеет линейную сложность.
