#!/usr/bin/env ruby

require "./Input.rb"

def getPuzzleInput(fileName)
    lines = File.readlines(fileName)
end

def main
    input = getPuzzleInput("puzzle-example.txt")
    inputParsed = Input.new(input)
    solutionOne = inputParsed.getNumUniqueOutputs()
    solutionTwo = inputParsed.getSumOfOutputs()
    puts "Solution One: #{solutionOne}"
    puts "Solution Two: #{solutionTwo}"
end

main()