import fileHelper
daysToSimulate = 256
fishCycleLength = 7
newFishCycle = 9

def GroupFish(fishes):
    fishesOut = [0] * newFishCycle
    for fish in fishes:
        fishesOut[fish] +=1
    return fishesOut

def SumFish(fishes):
    total = 0
    for fish in fishes:
        total += fish
    return total


if newFishCycle < fishCycleLength: raise Exception("New fish cycle can't be shorter than the fish cycle length")

inputLines = fileHelper.readInputFileAsStringList("Puzzle06/input6.txt")

fishes = inputLines[0].split(',')

for i in range(len(fishes)):
    fishes[i] = int(fishes[i])

fishGroups = GroupFish(fishes)
fishes = GroupFish(fishes)

for i in range(daysToSimulate):
    dayInCycle = i % newFishCycle
    newFishLocation = (dayInCycle + (fishCycleLength)) % newFishCycle
    fishGroups[newFishLocation] += fishGroups[dayInCycle]
    
    print("Day ", i+1, "\n",fishGroups," Sum: ",SumFish(fishGroups))