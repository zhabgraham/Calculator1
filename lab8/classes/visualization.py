from abc import ABC, abstractmethod
import matplotlib.pyplot as plt

class Visualization(ABC):
    @abstractmethod
    def visualize(self, data):
        pass

class BarChart(Visualization):
    def __init__(self, category_column, value_column):
        self.category_column = category_column
        self.value_column = value_column

    def visualize(self, data):
        data_grouped = data.groupby(self.category_column)[self.value_column].mean()
        data_grouped.plot(kind='bar', figsize=(10, 5), color='green')
        plt.xlabel(self.category_column)
        plt.ylabel(f"Average {self.value_column}")
        plt.title(f"Average {self.value_column} by {self.category_column}")
        plt.show()

class Histogram(Visualization):
    def __init__(self, column, bins=10):
        self.column = column
        self.bins = bins

    def visualize(self, data):
        plt.hist(data[self.column], bins=self.bins, color='skyblue')
        plt.title(f'Histogram of {self.column}')
        plt.xlabel(self.column)
        plt.ylabel('Frequency')
        plt.show()

class PieChart(Visualization):
    def __init__(self, column):
        self.column = column

    def visualize(self, data):
        plt.figure(figsize=(8, 8))
        data[self.column].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'orange', 'green', 'pink'])
        plt.title(f"Distribution of {self.column}")
        plt.ylabel('')
        plt.show()

class MultiPlot(Visualization):
    def visualize(self, data):
        fig, axs = plt.subplots(1, 2, figsize=(14, 7))

        # Bar chart for 'Number_of_Apps_Used'
        data['Number_of_Apps_Used'].value_counts().plot(kind='bar', ax=axs[0], color='green')
        axs[0].set_title('Distribution of Number of Apps Used')
        axs[0].set_xlabel('Number of Apps')
        axs[0].set_ylabel('Frequency')

        # Pie chart for 'Number_of_Apps_Used'
        data['Number_of_Apps_Used'].value_counts().plot(kind='pie', ax=axs[1], autopct='%1.1f%%', colors=['lightblue', 'orange', 'yellow', 'pink'])
        axs[1].set_title('Number of Apps Used Distribution')
        axs[1].set_ylabel('')

        plt.tight_layout()
        plt.show()
