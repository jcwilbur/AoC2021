import fileHelper

inputLines = fileHelper.readInputFileAsStringList("input5.txt")
vectors = []
horizontalVectors = []
verticalVectors = []
diagonalVectors = []

def processData(input, vectorList):
    for line in inputLines:
        myVector = ((),())
        splitLine = line.split()
        startCoord = splitLine[0].split(',')
        endCoord = splitLine[2].split(',') 

        myVector = (int((startCoord[0])),int(startCoord[1])),(int(endCoord[0]),int(endCoord[1]))
        
        vectors.append(myVector)
    return vectors

def sortVectors(inputVectors):
    outputVectors = []
    for vector in inputVectors:
        #check for horizontal
        if vector[0][0] == vector[1][0]:
            outputVectors.append(vector)
            horizontalVectors.append(vector)
        #check for vertical
        elif vector[0][1] == vector[1][1]:
            outputVectors.append(vector)
            verticalVectors.append(vector)
        else:
            diagonalVectors.append(vector)

    return outputVectors

def setPlaneSize(inputVectors):
    maxX =0
    maxY =0
    for vector in inputVectors:
        for coordinate in vector:
            if coordinate[0] > maxX: maxX = coordinate[0]
            if coordinate[1] > maxY: maxY = coordinate[1]
    return (maxX+1,maxY+1)

def createPlane(inputVectors):
    planeSize = setPlaneSize(inputVectors)
    #outputPlane = [[0]*planeSize[1]] *planeSize[0]
    outputPlane=[[0 for row in range(0,planeSize[0])] for col in range(0,planeSize[1])]
    for vector in inputVectors:
        #check for horizontal
        if vector[0][0] == vector[1][0]:
            minY=0
            maxY=0
            if vector[0][1] < vector[1][1]:
                minY = vector[0][1]
                maxY = vector[1][1]
            elif vector[1][1] < vector[0][1]:
                minY = vector[1][1]
                maxY = vector[0][1]
            else: raise Exception("uh oh")

            for i in range(minY,maxY+1):
                outputPlane[vector[0][0]][i] += 1

        #check for vertical
        elif vector[0][1] == vector[1][1]:
            minX=0
            maxX=0
            yAxis = vector[0][1]
            if vector[0][0] < vector[1][0]:
                minX = vector[0][0]
                maxX = vector[1][0]
            elif vector[1][0] < vector[0][0]:
                minX = vector[1][0]
                maxX = vector[0][0]
            else: raise Exception("uh oh")

            for i in range(minX,maxX+1):
                outputPlane[i][yAxis] = outputPlane[i][yAxis] + 1
        else:
            raise Exception("shoudn't happen")
    return outputPlane

def countDangerZones(inputPlane):
    dangerZones = 0
    for row in inputPlane:
        for col in row:
            if col > 1:
                dangerZones +=1
    
    return dangerZones


vectors = processData(inputLines, vectors)

vectors = sortVectors(vectors)

plane = createPlane(vectors)

answer = countDangerZones(plane)
print(answer)