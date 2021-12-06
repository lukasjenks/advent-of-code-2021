package com.company;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Objects;

public class Day3 {

    public static void main(String[] args) {
        ArrayList<String> binaryNums = getPuzzleInput("day3PuzzleInput.txt");
        assert binaryNums != null;
        getSolutionOne(binaryNums);
        getSolutionTwo(binaryNums);
    }

    private static ArrayList<String> getPuzzleInput(String fileName) {
        try {
            return new ArrayList<>(Files.readAllLines(Paths.get(fileName)));
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
        return null;
    }

    private static void getSolutionOne(ArrayList<String> binaryNums) {
        String gammaRate = "";
        String epsilonRate = "";
        // For column in 2D array
        for (int i = 0; i < binaryNums.get(0).length(); i++) {
            int numberOfOnes = 0;
            for (String binaryNum : binaryNums) {
                if (binaryNum.charAt(i) == '1') {
                    numberOfOnes++;
                }
            }
            int numberOfZeroes = binaryNums.size() - numberOfOnes;
            if (numberOfOnes > numberOfZeroes) {
                gammaRate = gammaRate + "1";
                epsilonRate = epsilonRate + "0";
            } else {
                gammaRate = gammaRate + "0";
                epsilonRate = epsilonRate + "1";
            }
        }
        // output product of gammaRate converted to decimal and epsilonRate converted to decimal
        System.out.println("Part One Solution: " + (Integer.parseInt(gammaRate, 2) * Integer.parseInt(epsilonRate, 2)));
    }

    private static void getSolutionTwo(ArrayList<String> binaryNums) {
        String oxygenGeneratorRating = getRating(new ArrayList<>(binaryNums), "oxygen");
        String co2ScrubberRating = getRating(new ArrayList<>(binaryNums), "co2");
        assert oxygenGeneratorRating != null;
        assert co2ScrubberRating != null;
        System.out.println("Part Two Solution: " + (Integer.parseInt(oxygenGeneratorRating, 2) * Integer.parseInt(co2ScrubberRating, 2)));
    }

    private static String getRating(ArrayList<String> binaryNums, String chemical) {
        for (int bitPosition = 0; bitPosition < binaryNums.get(0).length(); bitPosition++) {
            int numOfOnes = 0;
            int binaryNumsIndex;
            for (binaryNumsIndex = 0; binaryNumsIndex < binaryNums.size(); binaryNumsIndex++) {
                if (binaryNums.get(binaryNumsIndex).charAt(bitPosition) == '1') {
                    numOfOnes += 1;
                }
            }
            int numOfZeroes = binaryNums.size() - numOfOnes;
            char filterBit;
            if (numOfOnes > numOfZeroes) {
                filterBit = (Objects.equals(chemical, "oxygen")) ? '1' : '0';
            } else if (numOfOnes < numOfZeroes) {
                filterBit = (Objects.equals(chemical, "oxygen")) ? '0' : '1';
            } else {
                filterBit = (Objects.equals(chemical, "oxygen")) ? '1' : '0';
            }

            binaryNumsIndex = 0;
            while (binaryNumsIndex < binaryNums.size()) {
                if (binaryNums.get(binaryNumsIndex).charAt(bitPosition) != filterBit) {
                    binaryNums.remove(binaryNumsIndex);
                    if (binaryNums.size() == 1) {
                        return binaryNums.get(0);
                    }
                } else {
                    binaryNumsIndex++;
                }
            }
        }
        return null;
    }
}
