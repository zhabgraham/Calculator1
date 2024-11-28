import os
import sys

# Додайте корінь проекту до шляху
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


import unittest
from lab6.tests.test_operations import TestMathOperations

def run():
    unittest.main()

if __name__ == '__main__':
    run()
