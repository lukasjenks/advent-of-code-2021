class Input

    # array of numbers
    private inputsAndOutputs = Array.new
    private outputs = Array.new

    def initialize(linesOfFile)
        inputsAndOutputs = linesOfFile.map { |line| line.split(" | ") }
        @inputsAndOutputs = inputsAndOutputs
    end

    def getNumUniqueOutputs()
        count = 0
        for i in 0..@inputsAndOutputs.length - 1
            input = @inputsAndOutputs[i][0].split(" ")
            outputs = @inputsAndOutputs[i][1].split(" ")
            for j in 0..outputs.length - 1
                if ([2,4,3,7].include?outputs[j].length)
                    puts outputs[j]
                    count += 1
                end
            end
        end
        return count
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