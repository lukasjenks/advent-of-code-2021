class Segments:

    def __init__(self, inputs, outputs):
        self.numberToLettersMap = {} # what is needed for the solution
        self.lettersToNumbersMap = {} # what is needed for the solution
        self.letterToLetterMap = {}
        inputsAndOutputs = inputs + outputs
        foundItems = 0
        for signals in inputsAndOutputs:
            if (len(signals) == 2):
                if (not self.numberToLettersMap.get(1)):
                    foundItems += 1
                    self.numberToLettersMap[1] = signals
                    
            elif (len(signals) == 4):
                if (not self.numberToLettersMap.get(4)):
                    foundItems += 1
                    self.numberToLettersMap[4] = signals
                    
            elif (len(signals) == 3):
                if (not self.numberToLettersMap.get(3)):
                    foundItems += 1
                    self.numberToLettersMap[7] = signals
                    
            elif (len(signals) == 7):
                if (not self.numberToLettersMap.get(7)):
                    foundItems += 1
                    self.numberToLettersMap[8] = signals
                    
            elif (foundItems == 4):
                break;

        # Can now decode a segment
        for letter in self.numberToLettersMap[7]:
            if letter not in self.numberToLettersMap[1]:
                self.letterToLetterMap["a"] = letter
                break

        if (self.numberToLettersMap.get(8) == None):
            self.numberToLettersMap[8] = 'abcdefg'

        # Can now decode bd pair
        bdSegment = []
        # Segments present in 4 and 8 but not 7 = bd
        for letter in self.numberToLettersMap[4]:
            if letter in self.numberToLettersMap.get(8) and letter not in self.numberToLettersMap.get(7):
                # b segment not in 2 but d segment is
                bdSegment.append(letter)

        # Can now decode eg pair
        egSegment = []
        for letter in self.numberToLettersMap[8]:
            if (letter not in (self.numberToLettersMap[1] + self.numberToLettersMap[7] + self.numberToLettersMap[4])):
                egSegment.append(letter)

        foundItems = 0
        for signals in inputsAndOutputs:
            if (len(signals) == 5):
                if (egSegment[0] in signals and egSegment[1] in signals):
                    if (not self.numberToLettersMap.get(2)):
                        self.numberToLettersMap[2] = signals
                        foundItems += 1
                elif (bdSegment[0] in signals and bdSegment[1] in signals):
                    if (not self.numberToLettersMap.get(5)):
                        self.numberToLettersMap[5] = signals
                        foundItems += 1
                else:
                    if (not self.numberToLettersMap.get(3)):
                        self.numberToLettersMap[3] = signals
                        foundItems += 1
                if (foundItems == 3):
                    break
        
        for letter in egSegment:
            if letter in self.numberToLettersMap[5]:
                self.letterToLetterMap["g"] = letter
            else:
                self.letterToLetterMap["e"] = letter

        self.numberToLettersMap[9] = bdSegment[0] + bdSegment[1] + self.numberToLettersMap[7] + self.letterToLetterMap["g"]
        self.numberToLettersMap[6] = self.numberToLettersMap[5] + self.letterToLetterMap["e"]

        # isolate 0 - 6 segment signal that is not self.numberToLettersMAp[9] pr self.numberToLettersMap[6]

        # or could isolate b and d by taking bdsegment and isolating based on letters for 3
        for letter in bdSegment:
            if letter in self.numberToLettersMap[3]:
                self.letterToLetterMap["d"] = letter
            else:
                self.letterToLetterMap["b"] = letter
        
        zero = self.numberToLettersMap[8]
        for letter in zero:
            if (letter == self.letterToLetterMap["d"]):
                #remove letter from zero
                zero = zero.replace(letter, '')
                self.numberToLettersMap[0] = zero
                break

    def getSumOfOutputs(self, outputs):
        outputValue = ""
        for output in outputs:
            match(len(output)):
                case 2:
                    outputValue += '1'
                case 3:
                    outputValue += '7'
                case 4:
                    outputValue += '4'
                case 5:
                    # 2, 3, 5
                    if self.strContentEq(self.numberToLettersMap[2], output):
                        outputValue += '2'
                    elif self.strContentEq(self.numberToLettersMap[3], output):
                        outputValue += '3'
                    elif self.strContentEq(self.numberToLettersMap[5], output):
                        outputValue += '5'
                case 6:
                    # 0, 6, 9
                    if self.strContentEq(self.numberToLettersMap[0], output):
                        outputValue += '0'
                    elif self.strContentEq(self.numberToLettersMap[6], output):
                        outputValue += '6'
                    elif self.strContentEq(self.numberToLettersMap[9], output):
                        outputValue += '9'
                case 7:
                    outputValue += '8'
        return int(outputValue)

    def strContentEq(self, str1, str2):
        if len(str1) != len(str2):
            return False
        else:
            for letter in str1:
                if letter not in str2:
                    return False
        return True

        
# aaaa
#b    c
#b    c
# ddd
#e    f
#e    f
# gggg

# 1 - 2 segments (letters)
# 4 - 4 segments (letters)
# 7 - 3 segments (letters)
# 8 - 7 segments (letters)

# 0 - 6 segments (letters) 
# 6 - 6 segments (letters)
# 9 - 6 segments (letters)

# 2 - 5 segments (letters)
# 3 - 5 segments (letters)
# 5 - 5 segments (letters)