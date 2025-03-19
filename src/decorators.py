

def log(filename=None):
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
                if filename:
                    with open(filename, "a", encoding='utf-8') as file:
                        file.write(message)
                else:
                    print(message)

            return result
        return inner
    return my_decorator


@log("log.txt")
def sum_(a, b):
    print(a + b)

sum_(3, 4)