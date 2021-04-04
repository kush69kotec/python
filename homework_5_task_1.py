def odd_nums(n):
    for i in range(n + 1):
        if i % 2 != 0:
            yield i


odd_to_15 = odd_nums(15)
