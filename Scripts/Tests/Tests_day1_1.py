import unittest
import sys
import os
import sys


sys.path.append('/..')
sys.path.append('D:/Storage/1 - Home Files/Solutions/Aoc2023/Scripts')
from day1_1 import Loopandsum



class Test_FirstAndLast(unittest.TestCase):
    def test_Onerowscoring4(self):
        Testdata = ["1onetwo3"]
        output = Loopandsum(Testdata)
        self.assertEqual(output, 13)

    def test_tworowscoringten(self):
        Testdata = ["1onetwo4","3threefive3eight"]
        output = Loopandsum(Testdata)
        self.assertEqual(output, 47)

if __name__ == '__main__':
    unittest.main()