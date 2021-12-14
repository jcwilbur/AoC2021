import fileHelper

def PlotPoints(inputCoordinates):
    maxX = 0
    maxY = 0
    outputPlane = [False] * maxX #need to make sure I make 2d list correctly and not fall into same trap i did with bingo puzzle
    return outputPlane
    

def foldPaper(inputPlane, foldDetails):
    outputPlane = inputPlane
    foldDir = foldDetails[0]
    foldLocation = int(foldDetails[1])

    match foldDir:
        case "x":
            #loop through all rows on & below the fold
            for rowNum in range(foldLocation, len(inputPlane)):
                #loop through each column
                for colNum in inputPlane[rowNum]:
                    #if the value below the fold has a dot (is true)
                    if inputPlane[rowNum][colNum]:
                        #make sure there are no dots on the fold line
                        if rowNum == foldLocation: raise Exception("Found a dot on the fold line")
                        else:
                            #set the value of the corresponding cell above the fold to True
                            outputPlane[foldLocation-(rowNum-foldLocation)][colNum] = True
                
            #trim everything below the fold
            outputPlane = outputPlane[0:foldLocation]

        case "y":
            #loop through all rows 
            for rowNum in range(len(inputPlane)):
                #loop through each column at and the fold
                for colNum in range(foldLocation, len(inputPlane[rowNum])):
                    #if the value below the fold has a dot (is true)
                    if inputPlane[rowNum][colNum]:
                        #make sure there are no dots on the fold line
                        if colNum == foldLocation: raise Exception("Found a dot on the fold line")
                        else:
                            #set the value of the corresponding cell above the fold to True
                            outputPlane[rowNum][foldLocation(colNum-foldLocation)] = True
                
            #trim everything below the fold
            for rowNum in range(len(inputPlane)):
                outputPlane[rowNum] = outputPlane[rowNum]

    return outputPlane


inputList = fileHelper.readInputFileAsStringList("Puzzle13/input13.txt")

coordinates =  [x.split(",") for x in inputList if not x[0] == "f" and not x[0] == "\n"]
foldInstructions = [(x[11],x[13:]) for x in inputList if x[0] == "f"]

plane = PlotPoints(coordinates)

plane = foldPaper(plane,foldInstructions[0])