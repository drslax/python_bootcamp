from functools import reduce


def do_sum(x1, x2):
    return x1 + x2


def ft_reduce(func, lst):
    res = lst[0]
    for i in lst[1:]:
        res = func(res, i)
    return res


# Test
print(reduce(do_sum, [1, 2, 3, 4]))
print('------')
print(ft_reduce(do_sum, [1, 2, 3, 4]))
