import os
import sys

# Додайте корінь проекту до шляху
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from lab7.classes.app import App

if __name__ == "__main__":
    app = App()
    app.run()