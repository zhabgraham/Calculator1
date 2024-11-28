import matplotlib.pyplot as plt

class PlotExporter:
    def export_plot(self, filename, file_format='png'):
        full_path = f"{filename}.{file_format}"
        plt.savefig(full_path, format=file_format)
        print(f"Chart saved as {full_path}")
