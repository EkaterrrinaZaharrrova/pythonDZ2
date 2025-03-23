

def log(filename=None):
    """Декоратор принимающий на вход необязательный аргумент filename"""
    def my_decorator(func):
        def inner(*args, **kwargs):
            message = ''
            try:
                result = func(*args, **kwargs)
                message = f'{func.__name__} OK\n'
            except Exception as error:
                result = None
                message = f'{func.__name__} error: {error}. Inputs: {args}, {kwargs}\n'
            finally:
                if filename is None:
                    print(message)
                else:
                    with open(filename, "a") as file:
                        file.write(message)

            return result
        return inner
    return my_decorator


@log()
def sum_(a, b):
    return a + b


print(sum_(3, 4))
