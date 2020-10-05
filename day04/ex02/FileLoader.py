import pandas as pd


class FileLoader:
    @staticmethod
    def loader(path):
        data = pd.read_csv(path)
        shape = data.shape
        print(f'Loading dataset of dimensions {shape[0]} x {shape[1]}')
        return data

    @staticmethod
    def display(df, n):
        if (n >= 0):
            print(df.head(n))
        else:
            print(df.tail(-n))
        pass
