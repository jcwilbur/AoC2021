import fileHelper

inputList = fileHelper.readInputFileAsStringList("Puzzle2/input2.txt")

depth = horizontal = aim = 0

for step in inputList:
    stepList = step.split(" ")
    stepList[1] = int(stepList[1])
    match stepList[0]:
        case "down":
            aim += stepList[1]
        case "up":
            aim -= stepList[1]
        case "forward":
            horizontal += stepList[1]
            depth += stepList[1] * aim

print('Depth: {}, Distance {}, Product: {}'.format(depth, horizontal, depth * horizontal))