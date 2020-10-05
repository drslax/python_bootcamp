import pandas as pd
from FileLoader import FileLoader


def youngestFellah(df, year):
    m = df['Age'][(df['Sex'] == 'M') & (df['Year'] == year)].min()
    f = df['Age'][(df['Sex'] == 'F') & (df['Year'] == year)].min()
    dic = {'f': f, 'm': m}
    return dic


data = FileLoader.loader('../resources/athlete_events.csv')
#FileLoader.display(data, -6)
print(youngestFellah(data, 2004))
