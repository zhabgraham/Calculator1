import json
import csv
from colorama import Fore, Style, init
from prettytable import PrettyTable
import textwrap

init(autoreset=True)

class UserInterface:
    def __init__(self):
        self.history = []

    def flatten_data(self, data):
        flattened_data = []
        for item in data:
            flat_item = {}
            for key, value in item.items():
                if isinstance(value, dict):
                    flat_item[key] = ", ".join(f"{sub_key}: {sub_value}" for sub_key, sub_value in value.items())
                elif isinstance(value, list):
                    flat_item[key] = ", ".join(map(str, value))
                else:
                    flat_item[key] = value
            flattened_data.append(flat_item)
        return flattened_data

    def display_data(self, data, display_type="table", header_color=Fore.WHITE):
        if not data:
            print(Fore.RED + "No data to display.")
            return

        headers = list(data[0].keys())
        data = self.flatten_data(data)

        if display_type == "table":
            table = PrettyTable()
            table.field_names = [header_color + header + Style.RESET_ALL for header in headers]

            max_width = 30

            for entry in data:
                row = [textwrap.fill(str(entry.get(header, "")), max_width) for header in headers]
                table.add_row(row)

            for header in headers:
                table.align[header] = "l"
            print(table)

        elif display_type == "list":
            for i, entry in enumerate(data, 1):
                print(header_color + f"---{i} ---" + Style.RESET_ALL)
                for header, value in entry.items():
                    print(header_color + f"{header}:" + Style.RESET_ALL, value)
                print("-" * 40)

    def save_data(self, data, format_type="json"):
        filename = f"users_data.{format_type}"
        try:
            if format_type == "json":
                with open(filename, "w") as f:
                    json.dump(data, f, indent=4)
            elif format_type == "csv":
                keys = data[0].keys()
                with open(filename, "w", newline='') as f:
                    dict_writer = csv.DictWriter(f, fieldnames=keys)
                    dict_writer.writeheader()
                    dict_writer.writerows(data)
            elif format_type == "txt":
                with open(filename, "w") as f:
                    for entry in data:
                        f.write(str(entry) + "\n")
            print(f"Data saved as {filename}")
        except Exception as e:
            print(Fore.RED + f"Error saving data: {e}")

    def add_to_history(self, query, result):
        self.history.append({"query": query, "result": result})

    def show_history(self):
        if not self.history:
            print( "No history available.")
            return
        
        print( "User Query History:")
        for i, entry in enumerate(self.history, 1):
            print( f"\n{i}. User Input:" + Fore.WHITE, entry.get("query", "Unknown"))

            result = entry.get("result")
            print( "   Result:")
            if isinstance(result, list):
                for idx, item in enumerate(result, 1):
                    if isinstance(item, dict):
                        print(f"      {idx}.")
                        for key, value in item.items():
                            print( f"         {key}:" + Fore.WHITE, value)
                    else:
                        print( f"      {idx}. {item}")
            elif isinstance(result, dict):
                for key, value in result.items():
                    print( f"      {key}:" + Fore.WHITE, value)
            else:
                print( f"      {result}")
        print( "-" * 40)