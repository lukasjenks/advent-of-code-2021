class Input

    # array of numbers
    private inputsAndOutputs = Array.new
    private outputs = Array.new
    private inputs = Array.new

    def initialize(linesOfFile)
        inputsAndOutputs = linesOfFile.map { |line| line.split(" | ") }
        @inputsAndOutputs = inputsAndOutputs
        @inputs = []
        @outputs = []
        for i in 0..@inputsAndOutputs.length-1
            @inputs.append([@inputsAndOutputs[i][0].split(" ")])
            @outputs.append([@inputsAndOutputs[i][1].split(" ")])
        end
        puts("Inputs:", @inputs[0])
        puts("Outputs:", @outputs[0])
    end

    def getNumUniqueOutputs()
        count = 0
        for i in 0..@outputs.length-1
            puts("--")
            puts(@outputs[i])
            puts("--")
            for j in 0..@outputs[i].length-1
                if [2,4,3,7].include?@outputs[i][j].length
                    count += 1
                end
            end
        end
        return count
    end

    def getSumOfOutputs()
        sum = 0
        for i in 0..@outputs.length - 1
            for j in 0..@outputs[i]
                sum += 1
            end
        end
        return sum
    end
end

# 1 - 2 segments (letters)
# 4 - 4 segments (letters)
# 7 - 3 segments (letters)
# 8 - 7 segments (letters)

# 0 - 6 segments (letters)
# 2 - 5 segments (letters)
# 3 - 5 segments (letters)
# 5 - 5 segments (letters)
# 6 - 6 segments (letters)
# 9 - 6 segments (letters)