import os

class BaseAsciiArt:
    def __init__(self):
        self.text = ""
        self.symbol = "*"
        self.generated_art = ""
        self.alignment = "left"

    def user_input(self):
        self.text = input("Enter text or phrase to convert to ASCII art: ")
        return self.text

    def choose_symbol(self):
        self.symbol = input("Enter a character to create ASCII art (e.g., @, #, *): ").strip() or "*"
        return self.symbol

    def choose_alignment(self):
        while True:
            alignment = input("Select the alignment (left, center, right): ").strip().lower()
            if alignment in ["left", "center", "right"]:
                self.alignment = alignment
                return self.alignment
            print("Invalid choice. Please select 'left', 'center', or 'right'.")


    def resize_ascii_art(self, art, width_scale=1, height_scale=1):
        lines = art.splitlines()
        scaled_art = []
        for line in lines:
            scaled_line = ''.join([char * width_scale for char in line])
            for _ in range(height_scale):
                scaled_art.append(scaled_line)
        return "\n".join(scaled_art)

    def generate_ascii_art(self):
        pass

    def preview_art(self):
        print("\nASCII art preview:\n")
        print(self.generated_art)

    def run(self):
        raise NotImplementedError("The 'run' method must be implemented by subclasses.")
