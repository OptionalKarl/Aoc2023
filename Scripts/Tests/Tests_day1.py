import unittest
import sys
import os
import sys
sys.path.insert(0, "..\Scripts")

from day1_1 import Loopandsum



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