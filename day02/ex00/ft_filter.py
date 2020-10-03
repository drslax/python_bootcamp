def func(x):
    return x >= 18


def ft_filter(func, lst):
    res = [i for i in lst if func(i)]
    return res


# Test
ages = [5, 12, 17, 18, 24, 32]
adults = filter(func, ages)
ft_adults = ft_filter(func, ages)
for x, y in zip(adults, ft_adults):
    print(x, '----', y)
