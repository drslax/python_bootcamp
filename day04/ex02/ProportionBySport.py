import pandas as pd
from FileLoader import FileLoader


def proportionBySport(df, year, sport, gender):
    res = df[(data['Year'] == year) & (data['Sport']
                                       == sport) & (data['Sex'] == gender)]
    res_cln = res.drop_duplicates('Name')
    all_pr = df[(data['Year'] == year) & (
        data['Sex'] == gender)].drop_duplicates('Name')
    return (len(res_cln) / len(all_pr))


data = FileLoader.loader('../resources/athlete_events.csv')
print(proportionBySport(data, 2004, 'Tennis', 'F'))
