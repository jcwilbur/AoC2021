import fileHelper
daysToSimulate = 256
newFishCycle = 9

def SimulateDayWithCombinedFish(fishesIn):
    zeroes = fishesIn[0]
    fishesOutput = [fishesIn[1],fishesIn[2],fishesIn[3],fishesIn[4],fishesIn[5],fishesIn[6],fishesIn[7]+zeroes,fishesIn[8],zeroes]
    return fishesOutput

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

inputLines = fileHelper.readInputFileAsStringList("input6.txt")

fishes = inputLines[0].split(',')

for i in range(len(fishes)):
    fishes[i] = int(fishes[i])

fishes = GroupFish(fishes)

for i in range(daysToSimulate):
    fishes = SimulateDayWithCombinedFish(fishes)
    print("Day Complete: ", i, " ", SumFish(fishes))
