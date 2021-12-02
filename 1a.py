from os import read
#declare a list to hold raw input
inputStrings = []
with open('input.txt','r') as inputFile:
   #one line to automatically separate each line into its own entry in the list
    inputStrings = inputFile.readlines()
      
#declare a list to hold the values converted to ints
#TODO: Can I swap the values in-place without copying to a new list?
inputInts = []
for stringValue in inputStrings:
    inputInts.append(int(stringValue))

increases = 0
lastValue = 0
for currentValue in inputInts: 
    if(currentValue > lastValue):
        increases = increases +1
    lastValue = currentValue

#decrement one to account for the first entry falsely reporting as an increase
increases = increases -1

print(increases)
