def func(a, b, c):
    return a + b + c


def ft_map(func, *args, **kwargs):
    if func == None or len(args) == 0:
        raise TypeError('ft_map() must have at least two arguments.')
    return [func(*a) for a in list(zip(*args))]


# test
print(list(map(func, ('1', '2', '3'), ('1', '2', '3'), ('1', '2', '3'))))
print(list(ft_map(func, ('1', '2', '3'), ('1', '2', '3'), ('1', '2', '3'))))
