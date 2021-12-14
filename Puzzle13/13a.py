import fileHelper

def PlotPoints(inputCoordinates):
    maxX = 0
    maxY = 0

    for coord in inputCoordinates:
        if coord[0] > maxX: maxX = coord[0]
        if coord[1] > maxY: maxY = coord[1]

    outputPlane = []# [False] * maxX #need to make sure I make 2d list correctly and not fall into same trap i did with bingo puzzle
    for row in range(maxY+1):
        outputPlane.append([False] * (maxX+1))
    dotCounter = 0
    for coord in inputCoordinates:
        outputPlane[coord[1]][coord[0]] = True
        dotCounter +=1

    return outputPlane
    
def foldPaper(inputPlane, foldDetails):
    outputPlane = inputPlane
    foldDir = foldDetails[0]
    foldLocation = int(foldDetails[1])

    match foldDir:
        case "y":
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

        case "x":
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
                            outputPlane[rowNum][foldLocation-(colNum-foldLocation)] = True
            #trim everything below the fold
            for rowNum in range(len(inputPlane)):
                outputPlane[rowNum] = outputPlane[rowNum][0:foldLocation]

    return outputPlane

def countDots(inputPlane):
    totalDots = 0
    for row in inputPlane:
        for col in row:
            if col: totalDots +=1
    
    return totalDots

inputList = fileHelper.readInputFileAsStringList("Puzzle13/input13.txt")

coordinates =  [x.split(",") for x in inputList if not x[0] == "f" and not x[0] == "\n"]
for coord in coordinates:
    coord[0] = int(coord[0])
    coord[1] = int(coord[1])

foldInstructions = [(x[11],x[13:]) for x in inputList if x[0] == "f"]

plane = PlotPoints(coordinates)

print("count of dots before fold: ", countDots(plane))

plane = foldPaper(plane,foldInstructions[0])

print("count of dots after fold:  ", countDots(plane))
