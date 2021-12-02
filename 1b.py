from os import read
#constants
groupSize = 3

inputStrings = []
with open('input.txt','r') as inputFile:
    inputStrings = inputFile.readlines()

inputInts = []
for stringValue in inputStrings:
    inputInts.append(int(stringValue))

inputGroups = []
inputLength = len(inputInts)

#loop through entire input file
for i in range(inputLength):
   #append an zero value item to the list to add to later
    inputGroups.append(0)
    #loop through enough entries in the input file to create a full group
    for j in range(groupSize):
         #set the index I need to the base of the loop (i) plus the location within the group (j)
        readingNum = i+j
        #prevent from reading past the end of the file
        if(readingNum <inputLength):
            #add the individual reading to the group it's in
            inputGroups[i] += inputInts[readingNum]

#find how many increases there are - same code as in 1a            
increases = 0
lastValue = 0
for currentValue in inputGroups:   
    if(currentValue > lastValue):
        increases = increases +1
    lastValue = currentValue

#decrement one to account for the first entry falsely reporting as an increase
increases = increases -1

print(increases)
