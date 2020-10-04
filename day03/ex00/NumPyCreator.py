import numpy


class NumPyCreator:

    @staticmethod
    def from_list(lst):
        return numpy.array(lst) if isinstance(lst, list) else None

    @staticmethod
    def from_tuple(tpl):
        return numpy.array(tpl) if isinstance(tpl, tuple) else None

    @ staticmethod
    def from_iterable(itr):
        return numpy.array(itr)

    @ staticmethod
    def from_shape(shape, value=0):
        return numpy.full(shape, value)

    @ staticmethod
    def random(shape):
        return numpy.random.rand(*shape)

    @ staticmethod
    def identify(n):
        return numpy.identity(n)


print(NumPyCreator.identify(4))
