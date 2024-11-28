import os
import sys

# Додайте корінь проекту до шляху
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


from lab4.classes.ascii_art import ASCIIArtGenerator

if __name__ == "__main__":
    ascii_art_generator = ASCIIArtGenerator()
    ascii_art_generator.run()
