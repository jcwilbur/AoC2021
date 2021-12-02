from os import read

inputStrings = []
groupSize = 3
with open('input.txt','r') as inputFile:
   # while(inputFile.)
    #inputList.append(inputFile.readline())
    inputStrings = inputFile.readlines()

#print(inputList[100])
inputInts = []
for stringValue in inputStrings:
    inputInts.append(int(stringValue))

inputGroups = []

inputLength = len(inputInts)

for i in range(inputLength):
    inputGroups.append(0)
    for j in range(groupSize):
        readingNum = i+j
        if(readingNum <inputLength):
            inputGroups[i] += inputInts[readingNum]



increases = 0
lastValue = 0
for currentValue in inputGroups:
   
    if(currentValue > lastValue):
        increases = increases +1
    lastValue = currentValue

#decrement one to account for the first entry falsely reporting as an increase
increases = increases -1

print(increases)