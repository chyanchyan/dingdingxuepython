import time

B = 100


class Dingding:
    def __init__(self):
        pass


def main():
    x = 2
    l1 = [
        1,
        2,
        3,
        4,
        5
    ]
    y = 'love u'


def loging(db_name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('start function: %s' % func.__name__)
            print(f'do sth with db named: {db_name}')
            func(*args, **kwargs)
            print('end running')
            return func
        return wrapper
    return decorator


def decorator(func):
    def wrapper(*args, **kwargs):
        print('start function: %s' % func.__name__)
        func(*args, **kwargs)
        print('end running')
        return func
    return wrapper


def decorator2(func, *args, **kwargs):
    print('start function: %s' % func.__name__)
    func(*args, **kwargs)
    print('end running')
    return func


@decorator
def foo(a, b, c, d, e, f, g):
    z = a + b * c - d / (f ** g) - e
    print(z)
    return z


foo(1, 2, 3, 4, 5, 6, 7)
