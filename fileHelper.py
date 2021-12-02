from os import read
#declare a list to hold raw input

def readInputFile(filename):
    inputStrings = []
    with open(filename,'r') as inputFile:
    #one line to automatically separate each line into its own entry in the list
        inputStrings = inputFile.readlines()
    return inputStrings