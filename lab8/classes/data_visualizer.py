from lab8.classes.data_handler import DataHandler
from lab8.classes.visualization import Visualization
from lab8.classes.exporter import PlotExporter

class DataVisualizer:
    def __init__(self, data_handler: DataHandler, strategy: Visualization):
        self.data_handler = data_handler
        self.strategy = strategy
        self.exporter = PlotExporter()

    def set_strategy(self, strategy: Visualization):
        self.strategy = strategy

    def visualize(self):
        self.strategy.visualize(self.data_handler.get_data())
        self._ask_to_save()

    def _ask_to_save(self):
        response = input("Would you like to save the chart? (yes/no): ").strip().lower()
        if response == "yes":
            filename = input("Enter filename (without extension): ").strip()
            self.exporter.export_plot(filename, file_format = 'png')
        else:
            print("Chart was not saved.")
