from matplotlib import pyplot as plt


class ImageProcessor:

    @staticmethod
    def load(path):
        return plt.imread(path)

    @staticmethod
    def display(array):
        return plt.imshow(array, interpolation='bilinear')


img = ImageProcessor.load("../resources/42AI.png")
print(img)
ImageProcessor.display(img)
plt.show()
