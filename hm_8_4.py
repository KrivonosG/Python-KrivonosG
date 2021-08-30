def val_checker(filter):
    def val_check_decorator(func):
        def wrapper(*args):
            for a in args:
                if filter(a) != True:
                    raise ValueError
            return func(*args)
        return wrapper
    return val_check_decorator

@val_checker(lambda x: x > 0)
def  my_sqr(x):
    return x ** 0.5
print(my_sqr(4))
print(my_sqr(6))