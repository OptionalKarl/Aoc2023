from common import import_csv 
import unittest

class FirstAndLast:
    def Loopandsum(Data):
        for item in Data:
                firstint = 0
                secondint = 0
                for char in item:
                    if char.isnumeric():
                        if firstint == 0:
                            firstint = char
                        else:
                            secondint = char
                if secondint == 0:
                    secondint = firstint
                calibrationscore = int(str(firstint) + str(secondint))
                total += calibrationscore
        return total         


class Test_FirstAndLast(unittest.TestCase):
    def Onerowscoring4(self):
        Testdata = ["1onetwo3"]
        output = FirstAndLast.Loopandsum(Testdata)
        self.assertEqual(output, 4)

    def tworowscoringten(self):
        Testdata = ["1onetwo3","3threefive3eight"]
        output = FirstAndLast.Loopandsum(Testdata)
        self.assertEqual(output, 10)



file_path = 'VScode/AocSourceData/AoC2023Day1.txt'
Data = import_csv(file_path)
print (FirstAndLast.Loopandsum(Data))
