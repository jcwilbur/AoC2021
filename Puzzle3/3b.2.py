import fileHelper

def o2rating(arr, recursionCounter):
    if(len(arr) > 1):
        mostPopularValue = findMostPopularValue(arr, recursionCounter, 1)
        newList =[x for x in arr if int(x[recursionCounter:recursionCounter+1]) == mostPopularValue] 
        recursionCounter +=1
        return o2rating(newList, recursionCounter)
    return arr
     
def co2rating(arr, recursionCounter):
    if(len(arr) > 1):
        LeastPopularValue = findLeastPopularValue(arr, recursionCounter, 0)
        newList =[x for x in arr if int(x[recursionCounter:recursionCounter+1]) == LeastPopularValue]
        recursionCounter += 1
        return co2rating(newList, recursionCounter)
    return arr

def findMostPopularValue(inList, inPosition, tiebreaker):
    zeroes = 0
    ones = 0

    for line in inList:
        valueToMatch = line[inPosition:inPosition+1]
        match valueToMatch:
            case '0':
                zeroes +=1
            case '1':
                ones += 1 
    if zeroes > ones: return 0
    if ones > zeroes : return 1  
    if ones == zeroes : return tiebreaker 

def findLeastPopularValue(inDictionary, inPosition, tiebreaker):
    zeroes = 0
    ones = 0

    for line in inDictionary:
        valueToMatch = line[inPosition:inPosition+1]
        match valueToMatch:
            case '0':
                zeroes +=1
            case '1':
                ones += 1 
    if zeroes < ones: return 0
    if ones < zeroes : return 1  
    if ones == zeroes : return tiebreaker 

inputLines = fileHelper.readInputFileAsStringList("Puzzle3/input.txt")

recursionCounter=0
oxygen = int(o2rating(inputLines,recursionCounter)[0],2)

recursionCounter=0
co2 = int(co2rating(inputLines, recursionCounter)[0],2)

print('Oxygen: {}, CO2 {}, Product: {}'.format(oxygen, co2, oxygen * co2))