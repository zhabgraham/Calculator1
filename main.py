import os
import subprocess
import sys

project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.append(project_root)

class LabFacade:
    def __init__(self):
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
        self.lab_map = {
            '1': os.path.join(base_path, 'piton3/lab1', 'runner.py'),
            '2': os.path.join(base_path, 'piton3/lab2', 'runner.py'),
            '3': os.path.join(base_path, 'piton3/lab3', 'runner.py'),
            '4': os.path.join(base_path, 'piton3/lab4', 'runner.py'),
            '5': os.path.join(base_path, 'piton3/lab5', 'runner.py'),
            '6': os.path.join(base_path, 'piton3/lab6', 'runner.py'),
            '7': os.path.join(base_path, 'piton3/lab7', 'runner.py'),
            '8': os.path.join(base_path, 'piton3/lab8', 'runner.py'),
        }

    def run_lab(self, lab_number):
        """
        Запускає лабораторну роботу за її номером.

        :param lab_number: Номер лабораторної роботи.
        """
        lab_path = self.lab_map.get(lab_number)
        if lab_path:
            subprocess.run(['python3', lab_path])
        else:
            print("Невірний номер лабораторної роботи.")

def main():
    """
    Головна функція програми для вибору лабораторної роботи та її запуску.
    """
    facade = LabFacade()
    while True:
        print("\nВиберіть лабораторну роботу для запуску:")
        print("1. Лабораторна робота 1")
        print("2. Лабораторна робота 2")
        print("3. Лабораторна робота 3")
        print("4. Лабораторна робота 4")
        print("5. Лабораторна робота 5")
        print("6. Лабораторна робота 6")
        print("7. Лабораторна робота 7")
        print("8. Лабораторна робота 8")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '0':
            print("Вихід з програми.")
            break
        facade.run_lab(choice)

if __name__ == "__main__":
    main()


