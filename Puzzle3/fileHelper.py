from os import read

def readInputFileAsStringList(filename):
    inputStrings = []
    with open(filename,'r') as inputFile:
    #one line to automatically separate each line into its own entry in the list
        inputStrings = inputFile.readlines()
    return inputStrings