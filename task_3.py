def type_logger(func):
    def arg_type(*args):
        type_dict = []
        for arg in args:
            type_dict.append(f'{arg}: {str(type(arg))}')
        result = func(*args)
        result_string = (','.join(type_dict))
        print(f'{func.__name__}({result_string})')
        return result
    return arg_type


@type_logger
def calc_cube(*args):
    result = []
    for arg in args:
        result.append(arg ** 3)
    return result


a = calc_cube(3, 4, 3)
print(a)
