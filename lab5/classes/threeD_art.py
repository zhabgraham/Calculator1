import os
from lab5.classes.cube import Cube
from termcolor import colored

class ThreeDArtGenerator:
    def __init__(self):
        self.art = None  
        self.color = 'green' 
        self.direction = True  

    def choose_shape(self):
        while True:
            try:
                shape = input("Choose a shape (1 - Cube): ")
                if shape == '1':
                    size = int(input("Enter size (minimum 3): "))
                    if size < 3:
                        print("Size must be at least 3.")
                    else:
                        self.art = Cube(size)
                        break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Invalid input, please enter a number for the size and shifts.")

    def change_size(self):
        while True:
            try:
                size = int(input("Enter a new size (minimum 3): "))
                if size < 3:
                    print("Size must be at least 3.")
                elif self.art:
                    self.art.size = size  
                    break
                else:
                    print("Please select a shape first.")
            except ValueError:
                print("Invalid input, please enter a number for the size.")

    def get_available_colors(self):
        return ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def choose_color(self):
        while True:
            print("Available colors:")
            for i, color in enumerate(self.get_available_colors()):
                print(f"{i + 1}. {color}")
            try:
                color_choice = int(input("Choose a color by number: "))
                if 1 <= color_choice <= len(self.get_available_colors()):
                    self.color = self.get_available_colors()[color_choice - 1]
                    break
                else:
                    print("Invalid choice, please select again.")
            except ValueError:
                print("Invalid input, please enter a number.")

    def change_direction(self):
        self.direction = not self.direction
        print("Direction successfully changed.")
    
    def convert_to_2d(self):
        if self.art:
            return self.art.get_two_d_art()  
        else:
            print("Please select a shape first.")
            return ""

    def display_ascii_art(self):
        if self.art:
            projection = self.convert_to_2d()
            if projection:
                print("2D representation of the shape:")
                for line in projection.splitlines():
                    print(colored(line, self.color))

    def get_art(self) -> str:

        if not self.art:
            return ""
        art_lines = self.art.get_three_d_art().splitlines()
        return "\n".join([colored(line, self.color) for line in art_lines])

    def print_art(self):

        if self.art:
            print(self.get_art())
        else:
            print("Please select a shape first.")
    def save_to_file(self, filename="ascii_art"):
        if self.art:
            filename += '.txt'
            while os.path.exists(filename):
                choice = input(f"The file '{filename}' already exists. Overwrite it? (Enter 'yes' to overwrite, any other character to cancel): ").strip().lower()
                if choice == 'yes':
                    break
                else:
                    filename = input("Enter a new filename: ").strip() + '.txt'

            with open(filename, 'w') as file:
                file.write(self.get_art())
            print(f"ASCII art saved to {filename}")
        else:
            print("No art to save. Please select a shape first.")

    def run(self):
        while True:
            print("\nMain Menu")
            print("1. Generate 3D Art")
            print("2. Exit")
            choice = input("Enter your choice (1-2): ").strip()

            if choice == '1':
                self.choose_shape()
                self.choose_color()
                self.print_art()

                converted_to_2d = False
                while not converted_to_2d:
                    convert_choice = input("Do you want to convert this 3D art to 2D? (Enter 'yes' or any other character for no): ").strip().lower()
                    if convert_choice == 'yes':
                        self.display_ascii_art()
                        converted_to_2d = True
                    else:
                        print("Skipping 2D conversion.")
                        break

                saved_to_file = False
                while not saved_to_file:
                    save_choice = input("Do you want to save the ASCII art to a file? (Enter 'yes' or any other character for no): ").strip().lower()
                    if save_choice == 'yes':
                        filename = input("Enter filename: ")
                        self.save_to_file(filename)
                        saved_to_file = True
                    else:
                        print("Skipping save.")
                        break

            elif choice == '2':
                break
            else:
                print("Invalid choice, please select a number between 1 and 2.")