import fileHelper

inputLines = fileHelper.readInputFileAsStringList("input4.txt")

#assuming all the instructions are on the first line
instructions = inputLines.pop(0)
#assuming all bingo cards are 5x5
bingoCardSize = 5

bingoCards = []
#my code at the time of writing will increment first, and I want to keep zero index
bingoCardIndex = -1

def calculateWinningNumber(card,winningNum):
    sum =0
    for row in range(len(card)):
            for col in range(len(card[row])):
                if not card[row][col]["drawn"]:
                    sum += int(card[row][col]["value"])
    return sum * int(winningNum)

def checkForBingos(bingoCards):
    for card in range(len(bingoCards)):
        numsCalledInRow = [0] *bingoCardSize
        numsCalledInCol = [0] * bingoCardSize

        for row in range(len(bingoCards[card])):
            for col in range(len(bingoCards[card][row])):
                numsCalledInRow[row] += bingoCards[card][row][col]["drawn"]
                numsCalledInCol[col] += bingoCards[card][row][col]["drawn"]

        for total in numsCalledInCol:
            if total == bingoCardSize:
                return card

        for total in numsCalledInRow:
            if total == bingoCardSize:
                return card
    return False
    

def callNumber(bingoCards, number):

    for card in range(len(bingoCards)):
        for row in range(len(bingoCards[card])):
            for col in range(len(bingoCards[card][row])):
                if bingoCards[card][row][col]["value"] == number:
                    bingoCards[card][row][col]["drawn"] = 1

    return bingoCards

def addLineToBingoCard(inputLine,cardList,cardIndex):
    
    lineValues = inputLine.split()
    typedLine = []
    for value in lineValues:
        typedLine.append({"value":value, "drawn":0})
    

    cardList[cardIndex].append(typedLine)
    return cardList

#create bingo cards
for i in range(len(inputLines)):
    if inputLines[i] == "\n":
        bingoCardIndex +=1
        bingoCards.append([])
    else:
        bingoCards = addLineToBingoCard(inputLines[i],bingoCards, bingoCardIndex)
        
#draw numbers

instructions = instructions.split(",")

for calledNum in instructions:
    callNumber(bingoCards,calledNum)
    bingo = checkForBingos(bingoCards)
    if bingo:
        print(calculateWinningNumber(bingoCards[bingo],calledNum))
        break 
