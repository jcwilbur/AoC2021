from os import read

inputStrings = []
with open('input.txt','r') as inputFile:
   # while(inputFile.)
    #inputList.append(inputFile.readline())
    inputStrings = inputFile.readlines()

#print(inputList[100])
inputInts = []
for stringValue in inputStrings:
    inputInts.append(int(stringValue))

inputGroups = []



increases = 0
lastValue = 0
for currentValue in inputInts:
   
    if(currentValue > lastValue):
        increases = increases +1
    lastValue = currentValue

#decrement one to account for the first entry falsely reporting as an increase
increases = increases -1

print(increases)