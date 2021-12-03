import fileHelper

inputLines = fileHelper.readInputFileAsStringList("Puzzle3/input.txt")

numBits = len(inputLines[0].strip())
zeroes = [0] * numBits
ones = [0] * numBits

for line in inputLines:
    line = line.strip()
    if(len(line) != numBits):
        raise Exception("jagged input")
    for i in range(len(line)):
         match line[i]:
             case '0':
                 zeroes[i] +=1
             case '1':
                 ones[i] += 1

gammaBool = [0] * numBits
gammaStr = ""
epsilonBool = [0] * numBits
epsilonStr = ""

for i in range(numBits):
    gammaBool[i] = (int(ones[i]) > int(zeroes[i]))
    epsilonBool[i] = not gammaBool[i]

    gammaStr += str(gammaBool[i] * 1)
    epsilonStr += str(epsilonBool[i] *1)


gammaDecimal = int(gammaStr,2)
epsilonDecimal = int(epsilonStr,2)

powerConsumption = gammaDecimal * epsilonDecimal
print(powerConsumption)