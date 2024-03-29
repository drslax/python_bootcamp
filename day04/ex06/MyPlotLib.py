from FileLoader import FileLoader
import seaborn
import matplotlib


class MyPlotLib:
    def __init__(self):
        pass

    @classmethod
    def histogram(self, data, features):
        data[features].hist()
        matplotlib.pyplot.show()

    @classmethod
    def density(self, data, features):
        data[features].plot.kde()
        matplotlib.pyplot.show()

    @classmethod
    def pair_plot(self, data, features):
        seaborn.pairplot(data[features])
        matplotlib.pyplot.show()

    @classmethod
    def box_plot(self, data, features):
        seaborn.boxplot(data=data[features])
        matplotlib.pyplot.show()


data = FileLoader.loader('../resources/athlete_events.csv')
ftr = ["Weight", "Height"]
MyPlotLib.histogram(data, ftr)
#MyPlotLib.density(data, ftr)
#MyPlotLib.pair_plot(data, ftr)
#MyPlotLib.box_plot(data, ftr)
