
from classes import signals
from classes import segments

def main():
    signalObj = signals.Signals("puzzle-input.txt")
    sum = 0
    for i in range(0, len(signalObj.inputs)):
        segmentsObj = segments.Segments(signalObj.inputs[i], signalObj.outputs[i])
        sum += segmentsObj.getSumOfOutputs(signalObj.outputs[i])
    print("Part One Solution: " + str(signalObj.getUniqueOutputCount()))
    print("Part Two Solution: " + str(sum))

main()

# 3570 answer is too low