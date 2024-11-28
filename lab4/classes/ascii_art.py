import os

from shared.base_ascii_art import BaseAsciiArt
from lab4.sources.ascii_templates import ascii_templates

class ASCIIArtGenerator(BaseAsciiArt):

    def get_console_width(self):
        try:
            return os.get_terminal_size().columns
        except OSError:
            return 80

    def generate_ascii_art(self):
        art_lines = [""] * 5
        for char in self.text.upper():
            if char in ascii_templates:
                for i in range(5):
                    art_lines[i] += ascii_templates[char][i].replace('*', self.symbol) + "  "

        console_width = self.get_console_width()
        if self.alignment == "center":
            aligned_art = [line.center(console_width) for line in art_lines]
        elif self.alignment == "right":
            aligned_art = [line.rjust(console_width) for line in art_lines]
        else:
            aligned_art = art_lines

        self.generated_art = "\n".join(aligned_art)
        self.generated_art = self.resize_ascii_art(self.generated_art)
        self.preview_art()

    def run(self):
        while True:
            print("\nMain Menu")
            print("1. Generate ASCII Art")
            print("2. Exit")
            choice = input("Enter your choice (1-2): ").strip()

            if choice == '1':
                self.user_input()
                self.choose_symbol()
                self.choose_alignment()
                self.generate_ascii_art()
            elif choice == '2':
                break
            else:
                print("Invalid choice, please select a number between 1 and 2.")