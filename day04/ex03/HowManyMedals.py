import pandas as pd
from FileLoader import FileLoader


def howManyMedals(df, name):
    fil_data = df[df['Name'] == name][['Year', 'Medal']]
    dic = {}
    for year in fil_data['Year'].drop_duplicates():
        g = fil_data['Medal'][(fil_data['Medal'] ==
                               'Gold') & (fil_data['Year'] == year)].count()
        s = fil_data['Medal'][(fil_data['Medal'] ==
                               'Silver') & (fil_data['Year'] == year)].count()
        b = fil_data['Medal'][(fil_data['Medal'] ==
                               'Bronze') & (fil_data['Year'] == year)].count()
        dic[year] = ({'G': g, 'S': s, 'B': b})
    return dic


data = FileLoader.loader('../resources/athlete_events.csv')
print(howManyMedals(data, 'Kjetil Andr Aamodt'))
