import pyfiglet
from termcolor import colored
from shared.base_ascii_art import BaseAsciiArt

class AsciiArtPyfiglet(BaseAsciiArt):
    def __init__(self):
        super().__init__()
        self.fonts = ['slant', '3-d', '5lineoblique', 'standard', 'big', 'block', 'bubble', 'digital', 'isometric1', 'banner']
        self.colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def choose_font(self):
        print("Available fonts:")
        for i, font in enumerate(self.fonts):
            print(f"{i + 1}. {font}")
        try:
            font_choice = int(input("Choose a font by number: "))
            return self.fonts[font_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Defaulting to 'slant'.")
            return 'slant'

    def choose_color(self):
        print("Available colors:")
        for i, color in enumerate(self.colors):
            print(f"{i + 1}. {color}")
        try:
            color_choice = int(input("Choose a color by number: "))
            return self.colors[color_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Defaulting to 'white'.")
            return 'white'

    def generate_ascii_art(self):
        font = self.choose_font()
        color = self.choose_color()
        custom_char = input("Enter a custom character for the ASCII art (optional): ") or None

        ascii_art = pyfiglet.Figlet(font=font).renderText(self.text)
        if custom_char:
            for old_char in set(ascii_art):
                if old_char not in ['\n', ' ']:
                    ascii_art = ascii_art.replace(old_char, custom_char)

        self.generated_art = self.resize_ascii_art(ascii_art)
        print(colored(self.generated_art, color))



    def run(self):
        while True:
            print("\nMain Menu")
            print("1. Generate ASCII Art")
            print("2. Exit")
            choice = input("Enter your choice (1-2): ").strip()

            if choice == '1':
                self.user_input()
                self.generate_ascii_art()
            elif choice == '2':
                break
            else:
                print("Invalid choice, please select a number between 1 and 2.")