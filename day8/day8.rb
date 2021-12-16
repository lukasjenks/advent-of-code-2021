#!/usr/bin/env ruby

require "./Input.rb"

def getPuzzleInput(fileName)
    lines = File.readlines(fileName)
end

def main
    input = getPuzzleInput("puzzle-input.txt")
    inputParsed = Input.new(input)
    solutionOne = inputParsed.getNumUniqueOutputs()
    puts "Solution One: #{solutionOne}"
end

main()