import os
import sys

# Додайте корінь проекту до шляху
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


from lab3.classes.ascii_art_pyfiglet import AsciiArtPyfiglet

if __name__ == "__main__":
    ascii_art_generator = AsciiArtPyfiglet()
    ascii_art_generator.run()
