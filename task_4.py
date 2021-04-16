def val_checker(val_exp):
    def wrapper(func):
        def check(arg):
            if not val_exp(arg):
                raise ValueError(f'wrong parameter')
            else:
                result = func(arg)
                return result
        return check
    return wrapper


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-3)
print(a)