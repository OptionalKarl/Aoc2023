import sys
from common import import_csv

class Instruction:
    def __init__(self, input1, output, change='direct', input2=None, done=False):
        self.input1 = input1
        self.input2 = input2
        self.change = change
        self.output = output
        self.done = False

    def __str__(self):
        if self.input2 is None:
            return f"Instruction(input1={self.input1}, change={self.change}, output={self.output},)"
        else:
            return f"Instruction(input1={self.input1}, change={self.change}, input2={self.input2}, output={self.output})"
        
def compute (instruction):
    input1 = int(instruction.input1) if instruction.input1.isnumeric() else int(initial_dict.get(instruction.input1, 0))
    input2 = int(instruction.input2) if instruction.input2.isnumeric() else int(initial_dict.get(instruction.input2, 0))

    result = 0
    if instruction.change == 'AND': result = input1 & input2
    if instruction.change == 'OR': result = input1 | input2
    if instruction.change == 'LSHIFT': result = input1 << input2
    if instruction.change == 'RSHIFT': result = input1 >> input2
    return result 


def recurse(instructions, initial_dict, trace = ''):
    while initial_dict["a"] == None:
        for instruction in instructions:
            if initial_dict[instruction.output] == None :        
                # Direct
                if instruction.input1 == trace:
                    print(instruction)
                if instruction.change == 'direct':
                    if instruction.input1.isnumeric():
                        initial_dict[instruction.output] = instruction.input1
                        instruction.done = True  
                    elif initial_dict[instruction.input1] != None:
                        initial_dict[instruction.input1] = instruction.input1
                        instruction.done = True  
                # Not       
                elif instruction.change == 'Not':
                    if initial_dict[instruction.input1] != None:
                        initial_dict[instruction.output] = (1 << 16) - int(initial_dict[instruction.input1]) - 1
                        instruction.done = True
                else:
                    input1 = -1
                    input2 = -1
                    if (instruction.input1 in initial_dict and initial_dict[instruction.input1] != None) : input1 = initial_dict[instruction.input1]
                    elif instruction.input1.isnumeric(): input1 = instruction.input1
                    if input1 != -1:
                        if (instruction.input2 in initial_dict and initial_dict[instruction.input2] != None) : input2 = initial_dict[instruction.input2]
                        elif instruction.input2.isnumeric(): input2 = instruction.input2
                    if input1 != -1 and input2 != -1:
                        initial_dict[instruction.output] = compute(instruction)
                        instruction.done = True
                if instruction.done == True :
                    print(instruction)
                    trace = instruction.output

    result = initial_dict["a"]

    return result

    
filepath = 'D:/Storage/1 - Home Files/Solutions/Aoc2023/AOC2015/data/day7.txt'
data = import_csv(filepath)

padded = []
for row in data:
    newrow = row.split(' ')
    if len(newrow[0]) == 1: newrow[0] = newrow[0] + " "
    padded.append(newrow)
# data  = sorted(padded, key=lambda x: (x[-1][0], x[-1][1]))
data  = sorted(padded, key=lambda x: (x[0][0], x[0][1]))
instructions = []
for row in data:
    inst = row
    inst[0] = inst[0].replace(" ","")
    if len(inst) == 3:
        myobj = Instruction(input1=inst[0], change='direct', output=inst[2])
        instructions.append(myobj)
    elif len(inst) == 4:
        myobj = Instruction(input1=inst[1], change='Not', output=inst[3])
        instructions.append(myobj)
    else:
        myobj = Instruction(input1=inst[0], change=inst[1], output=inst[-1], input2=inst[2])
        instructions.append(myobj)
        

initial_dict = {}

for instruction in instructions:
    initial_dict[instruction.output] = None
result = recurse(instructions,initial_dict)

print(result)
