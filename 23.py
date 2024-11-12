def filter_even(func):
    def wrapper(*args, **kwargs):
        filtered_args = [
            arg for arg in args
            if (isinstance(arg, (int, bool)) and arg % 2 == 0) or
               (isinstance(arg, (list, tuple, dict, str)) and len(arg) % 2 == 0)]
        return func(*filtered_args, **kwargs)
    return wrapper

def delete_short(func):
    a = {}
    def wrapper(*args, **kwargs):
        nonlocal a
        for i in kwargs:
            if len(i) > 4:
                a[i]=kwargs[i]
            else:
                continue
        return func(*args, **a)
    return wrapper

@filter_even
@delete_short
def concatenate(*args, **kwargs):
    result = ""
    for arg in args + tuple(kwargs.values()):
        result += str(arg)
    return result


print(concatenate("Я", "хочу", "Выучить", "Питон", a="За", qwerty=10, c="Месяцев"))