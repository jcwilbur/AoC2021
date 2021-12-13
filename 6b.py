import fileHelper

cycleLength = 7
newFishCycle = 9
daysToSimulate = 256

def calculateSpawn(fish, numDays):
    OGFishCycles = int(numDays/cycleLength)

    return OGFishCycles * len(fishes)

def calculateFives(numDays):
    cycles = (numDays // cycleLength) + 1
    calc
    return cycles

def calculateSixes(numDays):
    cycles = (numDays // cycleLength) + 1
    if numDays % cycleLength ==0: cycles -=1
    return cycles


    

inputLines = fileHelper.readInputFileAsStringList("input6.txt")


fishes = inputLines[0].split(',')

for i in range(len(fishes)):
    fishes[i] = int(fishes[i])


anticipatedFish = calculateFish(fishes, daysToSimulate)


print(anticipatedFish)