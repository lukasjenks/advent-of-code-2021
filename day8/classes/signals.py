class Signals:

    def __init__(self, filePath):
        self.inputs = []
        self.outputs = []
        filePath = "/home/lukas/Documents/Projects/advent-of-code-2021/day8/" + filePath
        #Load contents of file into a string
        f = open(filePath, "r")
        for line in f:
            input, output = line.strip().split(" | ")
            self.inputs.append(input.split(" "))
            self.outputs.append(output.split(" "))
        f.close()

    def getUniqueOutputCount(self):
        count = 0
        for outputs in self.outputs:
            for output in outputs:
                if (len(output) in [2,4,3,7]):
                    count = count + 1
        return count

    def printClassData(self):
        print(self.inputs)
        print(self.outputs)