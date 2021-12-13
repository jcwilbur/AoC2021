import fileHelper
daysToSimulate = 256
totalFish=0
daysRemaining = daysToSimulate
cycleLength = 7
newFishCycle = 9
daysToSimulate = 256

def SimulateDay(fishes, daysRemaining):
    for i in range(len(fishes)):
        match fishes[i]:
            case 0:
                #create new fish
                fishes.append(8)
                fishes[i] = 6
            case _:
                fishes[i] -= 1
    daysRemaining -= 1
    return fishes

def CalcChildren(fish, daysRemaining):
    numSpawn = 0
    match fish:
        case 0:
            numSpawn = (daysRemaining // cycleLength) + 1
            if(daysRemaining % cycleLength) > 5: numSpawn += 1
        case 1:
            numSpawn = (daysRemaining // cycleLength) + 1
            if(daysRemaining % cycleLength) > 4: numSpawn += 1
        case 2:
            numSpawn = (daysRemaining // cycleLength) + 1
            if(daysRemaining % cycleLength) > 3: numSpawn += 1
        case 3:
            numSpawn = (daysRemaining // cycleLength) + 1
            if(daysRemaining % cycleLength) > 2: numSpawn += 1
        case 4:
            numSpawn = (daysRemaining // cycleLength) + 1
            if(daysRemaining % cycleLength) > 1: numSpawn += 1
        case 5: 
            numSpawn = (daysRemaining // cycleLength) + 1
            if(daysRemaining % cycleLength) > 0: numSpawn += 1
        case 6:
            numSpawn = (daysRemaining // cycleLength) + 1
        case 7:
            pass
        case 8:
            pass
    return numSpawn

#inputLines = fileHelper.readInputFileAsStringList("input6.txt")
inputLines = ["6"]

fishes = inputLines[0].split(',')

for i in range(len(fishes)):
    fishes[i] = int(fishes[i])

for i in range(20):
    print("Day: ",i,". Fish: ",CalcChildren(fishes[0],i))

