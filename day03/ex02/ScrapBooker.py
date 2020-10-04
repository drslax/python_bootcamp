import numpy as np


class ScrapBooker:
    @staticmethod
    def crop(array, dimension, position):
        return a2[position:(dimension[0] + position), position:(dimension[1] + position)]

    @staticmethod
    def thin(array, n, axis):
        return np.delete(array, n, axis)

    @staticmethod
    def juxtapose(array, n, axis):
        pass

    @staticmethod
    def mosaic(array, dimension):
        pass


a2 = np.array([[10, 11, 12, 13, 14],
               [15, 16, 17, 18, 19],
               [20, 21, 22, 23, 24],
               [25, 26, 27, 28, 29]])

print(ScrapBooker.thin(a2, 2, 0))
#print(ScrapBooker.crop(a2, [2, 2], 1))
