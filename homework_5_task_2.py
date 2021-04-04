def odd_nums(n):
    nums_gen = (num for num in range(1, n + 1, 2))
    return nums_gen


odd_to_15 = odd_nums(15)