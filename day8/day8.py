
from classes import signals
from classes import segments

def getSolutionOne():
    return 0

def getSolutionTwo():
    return 0

def main():
    signalObj = signals.Signals("puzzle-example.txt")
    sum = 0
    for i in range(0, len(signalObj.inputs)):
        segmentsObj = segments.Segments(signalObj.inputs[i], signalObj.outputs[i])
        sum += segmentsObj.getSumOfOutputs(signalObj.outputs[i])
    print("Part One Solution: " + str(signalObj.getUniqueOutputCount()))
    print("Part Two Solution: " + str(sum))

main()
    


    #print("Part One Solution: ", getSolutionOne())
    #print("Part Two Solution: ", getSolutionTwo())