import re
from colorama import Fore, Style, init

class InputParser:
    def __init__(self):
        self.patterns = {
            "date": re.compile(r'\d{4}-\d{2}-\d{2}'),
            "phone": re.compile(r'\+?\d{1,3}[-.\s]?\d{1,3}[-.\s]?\d{4,10}'),
            "email": re.compile(r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$'),
            "id": re.compile(r'^\d+$'),
            "name": re.compile(r'^[A-Za-zА-Яа-я]+$'),
        }

    def parse_input(self, user_input):
        detected_type = None

        # Перевірка введених даних
        for key, pattern in self.patterns.items():
            if pattern.match(user_input):
                detected_type = key
                break

        if detected_type:
            print(f"{detected_type.capitalize()} detected in input.")
        else:
            print(Fore.RED + "No specific pattern detected or invalid input.")