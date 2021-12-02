import fileHelper

#inputList = fileHelper.readInputFileAsStringList("input2.txt")
inputStrings = []
with open("input2.txt",'r') as inputFile:
    #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()

depth = 0
horizontal = 0

for step in inputList:
    stepList = step.split(" ")
    stepList[1] = int(stepList[1])
    match stepList[0]:
        case "down":
            depth += stepList[1]
        case "up":
            depth -= stepList[1]
        case "forward":
            horizontal += stepList[1]

print('Depth: {}, Distance {}, Product: {}'.format(depth, horizontal, depth * horizontal))