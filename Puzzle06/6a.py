import fileHelper
daysToSimulate = 80
def SimulateDay(fishes):
    for i in range(len(fishes)):
        match fishes[i]:
            case 0:
                #create new fish
                fishes.append(8)
                fishes[i] = 6
            case _:
                fishes[i] -= 1
    return fishes

inputLines = fileHelper.readInputFileAsStringList("input6.txt")

fishes = inputLines[0].split(',')

for i in range(len(fishes)):
    fishes[i] = int(fishes[i])


for i in range(daysToSimulate):
    fishes = SimulateDay(fishes)
    print("Day Complete: ", i)

print(len(fishes))