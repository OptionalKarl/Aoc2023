import unittest
import sys
import os
import sys

sys.path.append('../Scripts')

sys.path.append('/..')
sys.path.append('D:/Storage/1 - Home Files/Solutions/Aoc2023/Scripts')

from common import import_csv

class Test_SampleData(unittest.TestCase):
    def test_Onerowscoring4(self):
        TestData = import_csv("D:/Storage/1 - Home Files/Solutions/Aoc2023\Data/TestDataDay5.txt")
        self.assertEqual(output, 13)

    