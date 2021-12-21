class Segments:

    def __init__(self, inputs, outputs):
        self.numberToLettersMap = {} # what is needed for the solution
        self.lettersToNumbersMap = {} # what is needed for the solution
        # self.letterToLetterMap = {}
        inputsAndOutputs = inputs + outputs
        for signals in inputsAndOutputs:
            match(len(signals)):
                case 2:
                    self.numberToLettersMap[1] = signals
                case 4:
                    self.numberToLettersMap[4] = signals
                case 7:
                    self.numberToLettersMap[3] = signals
                case 8:
                    self.numberToLettersMap[7] = signals
        # Algorithm for finding letter that maps to a
        #for letter in self.numberToLettersMap[7]:
            #if letter not in self.numberToLettersMap[1]:
                #self.letterToLetterMap["a"] = letter
        # 3 is the one with 5 segments and contains all letters in 1
        for signal in inputsAndOutputs:
            if len(signal) == 5:
                numInCommonWith1 = 0
                for letter in signal:
                    if self.numberToLettersMap.get(1) and letter in self.numberToLettersMap.get(1):
                        numInCommonWith1 += 1
                if (numInCommonWith1 == 2):
                    self.numberToLettersMap[3] = signal
        # 9 is now the one with all letters in 3 + 1 more
        for signal in inputsAndOutputs:
            if len(signal) == 6: # only 9 or 6
                numInCommonWith3 = 0
                numInCommonWith1 = 0
                for letter in signal:
                    if self.numberToLettersMap.get(3) and letter in self.numberToLettersMap.get(3):
                        numInCommonWith3 += 1
                    if self.numberToLettersMap.get(1) and letter in self.numberToLettersMap.get(1):
                        numInCommonWith1 += 1
                if numInCommonWith3 == 5 and numInCommonWith1 == 2:
                    self.numberToLettersMap[9] = signal
                elif numInCommonWith3 == 5 and numInCommonWith1 == 1:
                    self.numberToLettersMap[6] = signal
                else:
                    self.numberToLettersMap[0] = signal
        # 5 has 3 in common with 4, 2 has 2 in common with 4
        for signal in inputsAndOutputs:
            if len(signal) == 5:
                numInCommonWith4 = 0
                numInCommonWith2 = 0
                for letter in signal:
                    if self.numberToLettersMap.get(4) and letter in self.numberToLettersMap.get(4):
                        numInCommonWith4 += 1
                    if self.numberToLettersMap.get(2) and letter in self.numberToLettersMap.get(2):
                        numInCommonWith2 += 1
                if numInCommonWith4 == 3:
                    self.numberToLettersMap[5] = signal
                elif numInCommonWith2 == 2:
                    self.numberToLettersMap[2] = signal
        for key, value in self.numberToLettersMap.items():
            self.lettersToNumbersMap[value] = key

    def getSumOfOutputs(self, outputs):
        sum = 0
        for output in outputs:
            if (self.lettersToNumbersMap.get(output)):
                sum += self.lettersToNumbersMap.get(output)
            else:
                print("Error: missing key: " + output)
                print(self.lettersToNumbersMap.get(output))
        return sum
        
# aaaa
#b    c
#b    c
# ddd
#e    f
#e    f
# gggg

# 1 - 2 segments (letters) #done
# 4 - 4 segments (letters) #done
# 7 - 3 segments (letters) #done
# 8 - 7 segments (letters) #done

# 0 - 6 segments (letters) #done
# 2 - 5 segments (letters)
# 3 - 5 segments (letters) #done
# 5 - 5 segments (letters)
# 6 - 6 segments (letters) #done
# 9 - 6 segments (letters) #done