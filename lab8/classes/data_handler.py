import pandas as pd

class DataHandler:
    def __init__(self, file_path):
        self._data = pd.read_csv(file_path)

    def get_data(self):
        return self._data

    def show_summary(self):
        print(self._data.describe())

    def find_extremes(self):
        extremes = {}
        for column in self._data.select_dtypes(include='number').columns:
            extremes[column] = {
                'min': self._data[column].min(),
                'max': self._data[column].max()
            }
        for col, values in extremes.items():
            print(f"Column: {col} | Min: {values['min']} | Max: {values['max']}")
        return extremes
