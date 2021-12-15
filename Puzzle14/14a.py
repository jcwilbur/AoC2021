import fileHelper
inputList = fileHelper.readInputFileAsStringList("Puzzle14/input14.txt")
startingPolymer = inputList.pop(0).strip()
pairInsertionRules = inputList[1:]
lastLetter = startingPolymer[-1]
numRuns = 40

#manually verified to work with input given
def createPairList(polymerIn):
    pairListOut = {}
    for letterIndex in range(len(polymerIn)-1):
        pair = polymerIn[letterIndex:letterIndex+2]
        if not pair in pairListOut:
            pairListOut[pair] = 1
        else:
            pairListOut[pair] += 1
    return pairListOut
        
def createRuleDictionary(rulesLinesIn):
    ruleDictOut = {}
    for ruleLine in rulesLinesIn:
        list = ruleLine.split("->")
        ruleDictOut[list[0].strip()] = list[1].strip()
    
    return ruleDictOut

def doWork(polymerIn,rulesIn):
    pairsToAdd = {}
    for key in rulesIn:
        #get the count of occurences of this key in the polymer
        if key in polymerIn:
            count = polymerIn[key]
            #you have to add that number to both combos created by this insertion
            key1 = key[0] + rulesIn[key]
            key2 = rulesIn[key] + key[1]
            if not key1 in pairsToAdd: pairsToAdd[key1] = 0
            if not key2 in pairsToAdd: pairsToAdd[key2] = 0
            if not key in pairsToAdd: pairsToAdd[key] = 0
            pairsToAdd[key1] += count
            #don't double add on keys like "KK"
            if not key1 == key2:
                pairsToAdd[key2] += count
            #decrement the prior pair
            pairsToAdd[key] -=count
    mergedDictionary = MergeDictionaries(polymerIn,pairsToAdd)
    return mergedDictionary

def doWork2(polymerIn,rulesIn):
    pairsToAdd = {}

    for pair in polymerIn:
        if pair in rulesIn:
            count = polymerIn[pair]
            polymerIn[pair] = 0
            newKey1 = pair[0] + rulesIn[pair]
            newKey2 = rulesIn[pair] + pair[1]
            if not newKey1 in pairsToAdd: pairsToAdd[newKey1] = 0
            if not newKey2 in pairsToAdd: pairsToAdd[newKey2] = 0
            pairsToAdd[newKey1] += count
            pairsToAdd[newKey2] += count
    output = MergeDictionaries(polymerIn,pairsToAdd)

    return output

def MergeDictionaries(target,valuesToMerge):
    output = target
    for key in valuesToMerge:
        if not key in output: output[key] = valuesToMerge[key]
        else: output[key] += valuesToMerge[key]
    return output

def CountLetters(pairListIn,lastLetterIn):
    letterCounts = {}
    for key in pairListIn:
        if not key[0] in letterCounts: letterCounts[key[0]] = pairListIn[key]
        else: letterCounts[key[0]] += pairListIn[key]
    
    #b/c i'm only counting first letters of pairs, have to manually add the last
    if not lastLetterIn in letterCounts: letterCounts[lastLetterIn] = 1
    else: letterCounts[lastLetterIn] += 1

    minKey = min(letterCounts,key=letterCounts.get)
    maxKey = max(letterCounts,key=letterCounts.get)
    minVal = letterCounts[minKey]
    maxVal = letterCounts[maxKey]
    print("Min: ", minKey, " Value: ",minVal)
    print("Max: ", maxKey, " Value: ", maxVal)
    print("Difference of: ", maxVal-minVal)

pairList = createPairList(startingPolymer)

pairInsertionRules = createRuleDictionary(pairInsertionRules)

for i in range(numRuns):
    pairList = doWork(pairList, pairInsertionRules)
    print("run: ",i, "\n",CountLetters(pairList,lastLetter))


