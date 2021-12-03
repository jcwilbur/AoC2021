import fileHelper

def o2rating(arr):
    if(len(arr) > 1):
        mostPopularValue = findMostPopularValue(arr, 0, 1)
        newList =[{"stringVal": x["stringVal"][1:],"originalIndex": x["originalIndex"],"decimalVal":x["decimalVal"]} for x in arr if int(x["stringVal"][:1]) == mostPopularValue] 
        return o2rating(newList)
    return arr
     
def co2rating(arr):
    if(len(arr) > 1):
        mostPopularValue = findLeastPopularValue(arr, 0, 0)
        newList =[{"stringVal": x["stringVal"][1:],"originalIndex": x["originalIndex"],"decimalVal":x["decimalVal"]} for x in arr if int(x["stringVal"][:1]) == mostPopularValue] 
        return co2rating(newList)
    return arr

def findMostPopularValue(inDictionary, inPosition, tiebreaker):
    zeroes = 0
    ones = 0

    for line in inDictionary:
        valueToMatch = line["stringVal"][inPosition:inPosition+1]
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
        valueToMatch = line["stringVal"][inPosition:inPosition+1]
        match valueToMatch:
            case '0':
                zeroes +=1
            case '1':
                ones += 1 
    if zeroes < ones: return 0
    if ones < zeroes : return 1  
    if ones == zeroes : return tiebreaker 

inputLines = fileHelper.readInputFileAsStringList("Puzzle3/input.txt")

inputDictionary = []
for i in range(len(inputLines)):
    inputLines[i] = inputLines[i].strip()
    inputDictionary.append({"stringVal":inputLines[i],
                            "originalIndex":i,
                            "decimalVal": int(inputLines[i],2)})
   
oxygen = o2rating(inputDictionary)[0]["decimalVal"]
co2 = co2rating(inputDictionary)[0]["decimalVal"]

print('Oxygen: {}, CO2 {}, Product: {}'.format(oxygen, co2, oxygen * co2))