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
    output = merge(polymerIn,pairsToAdd)

    return output
