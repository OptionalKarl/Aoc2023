import unittest
import sys
import os
from common import import_csv

# Get the parent directory
parent_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
sys.path.append(parent_dir)

# Import the module from the parent directory
from day1_1 import Loopandsum
from common import import_csv



class Test_FirstAndLast(unittest.TestCase):
    def Onerowscoring4(self):
        Testdata = ["1onetwo3"]
        output = Loopandsum(Testdata)
        self.assertEqual(output, 4)

    def tworowscoringten(self):
        Testdata = ["1onetwo4","3threefive3eight"]
        output = Loopandsum(Testdata)
        self.assertEqual(output, 10)

if __name__ == '__main__':
    unittest.main()