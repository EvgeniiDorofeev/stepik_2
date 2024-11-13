from functools import wraps
def limit_query(func):
    k=0
    @wraps(func) # использование wraps
    def inner(*args, **kwargs):
        """
        Внутренняя функция декоратора
        """
        for i in range(1):
            nonlocal k
            k+=1
            if k>3:
                print('Лимит вызовов закончен, все 3 попытки израсходованы')
                return
        return func(*args, **kwargs)
    return inner




@limit_query
def add(a: int, b: int):
    return a + b

print(add(4, 5))
print(add(5, 8))
print(add(9, 43))
print(add(10, 33))
print(add.__name__)