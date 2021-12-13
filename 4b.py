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

def checkForBingos(bingoCards, winners, lastCalledNum):
    #for each card
    for cardIndex in range(len(bingoCards)):
        #make sure you don't overrun index since this loop can remove cards 
        if cardIndex < len(bingoCards):
            numsCalledInRow = [0] * 5
            numsCalledInCol = [0] * 5

            #count/locate the called numbers
            for row in range(len(bingoCards[cardIndex])):
                for col in range(len(bingoCards[cardIndex][row])):
                    numsCalledInRow[row] += bingoCards[cardIndex][row][col]["drawn"]
                    numsCalledInCol[col] += bingoCards[cardIndex][row][col]["drawn"]
            skip = False
            #see if there's a vertical bingo
            for total in numsCalledInCol:
                if total == bingoCardSize:
                    winners.append(calculateWinningNumber(bingoCards[cardIndex],lastCalledNum))
                    bingoCards.pop(cardIndex)
                    skip = True
                    break
            #in the event of a number getting horitzontal & vertical bingo at the same time, don't add multiple entries to winners
            if not skip:
                for total in numsCalledInRow:
                    if total == bingoCardSize:
                        winners.append(calculateWinningNumber(bingoCards[cardIndex],lastCalledNum))
                        bingoCards.pop(cardIndex)
                        break
    return winners
    

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
winners = []
for calledNum in instructions:
    callNumber(bingoCards,calledNum)
    winners = checkForBingos(bingoCards, winners,calledNum)
    
print(winners[-1])