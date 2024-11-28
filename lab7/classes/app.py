from lab7.classes.user_interface import UserInterface
from lab7.classes.input_parser import InputParser
from lab7.classes.data_repository import DataRepository
from colorama import Fore

class App:
    def __init__(self):
        self.ui = UserInterface()
        self.parser = InputParser()
        self.repo = DataRepository("users")
        self.fetched_data = None 

    def run(self):
        while True:
            print("\n1. Fetch data\n2. Display data\n3. Save data\n4. Show history\n5. Parse input\n6. Exit")
            choice = input("Select an option: ").strip()

            if choice == "1":
                try:
                    self.fetched_data = self.repo.get_data()
                    self.ui.add_to_history("Fetch data", self.fetched_data)
                    print("Data fetched successfully.")
                except Exception as e:
                    print(Fore.RED + f"Error: {e}")

            elif choice == "2":
                if not self.fetched_data:
                    print(Fore.RED + "No data to display. Please fetch data first.")
                    continue
                
                while True:
                    display_type = input("Enter display type (table/list): ").strip().lower()
                    if display_type in ["table", "list"]:
                        break
                    print(Fore.RED + "Invalid input. Please enter 'table' or 'list'.")

                while True:
                    header_color = input("Enter header color (red, green, blue, yellow, white, cyan, magenta): ").strip().upper()
                    color_dict = {
                        "RED": Fore.RED,
                        "GREEN": Fore.GREEN,
                        "BLUE": Fore.BLUE,
                        "YELLOW": Fore.YELLOW,
                        "WHITE": Fore.WHITE,
                        "CYAN": Fore.CYAN,
                        "MAGENTA": Fore.MAGENTA
                    }
                    if header_color in color_dict:
                        header_color = color_dict[header_color]
                        break
                    print(Fore.RED + "Invalid input. Please enter a valid color name.")
                
                try:
                    self.ui.display_data(self.fetched_data, display_type, header_color)
                except Exception as e:
                    print(Fore.RED + f"Error: {e}")

            elif choice == "3":
                if not self.fetched_data:  
                    print(Fore.RED + "No data to save. Please fetch data first.")
                    continue

                while True:
                    format_type = input("Enter file format (json/csv/txt): ").strip().lower()
                    if format_type in ["json", "csv", "txt"]:
                        break
                    print(Fore.RED + "Invalid input. Please enter 'json', 'csv', or 'txt'.")

                try:
                    self.ui.save_data(self.fetched_data, format_type)
                except Exception as e:
                    print(Fore.RED + f"Error: {e}")

            elif choice == "4":
                self.ui.show_history()

            elif choice == "5":
                while True:
                    user_input = input("Enter text to parse: ").strip()
                    if user_input:
                        break
                    print(Fore.RED + "Input cannot be empty. Please enter some text.")
                
                self.parser.parse_input(user_input)

            elif choice == "6":
                print("Exiting the application.")
                break

            else:
                print(Fore.RED + "Invalid choice. Try again.")
