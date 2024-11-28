import os
import sys

# Додайте корінь проекту до шляху
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


from lab5.classes.threeD_art import ThreeDArtGenerator

if __name__ == '__main__':
    threeD_art = ThreeDArtGenerator()
    threeD_art.run()