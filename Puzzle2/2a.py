import fileHelper

inputList = fileHelper.readInputFileAsStringList("Puzzle2/input2.txt")

depth = horizontal = 0

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