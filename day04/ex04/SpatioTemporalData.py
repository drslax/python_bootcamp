import pandas as pd
from FileLoader import FileLoader


class SpatioTemporalData:

    def __init__(self, data):
        self.data = data

    def when(self, location):
        df = self.data.drop_duplicates('Year')
        return list(df[df['City'] == location]['Year'])

    def where(self, date):
        df = self.data.drop_duplicates('City')
        return list(df[df['Year'] == date]['City'])


data = FileLoader.loader('../resources/athlete_events.csv')
print(SpatioTemporalData(data).where(2004))
print(SpatioTemporalData(data).when('Athina'))
