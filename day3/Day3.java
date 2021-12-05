import java.util.*;
import java.io.*;
import java.nio.file.*;

public class Day3 {
	public static void main(String[] args) {
		ArrayList<String> binaryNums = getPuzzleInput("./day3puzzleinput.txt");
		assert binaryNums != null;
		getSolutionOne(binaryNums);
		getSolutionTwo(binaryNums);
	}

	private static ArrayList<String> getPuzzleInput(String fileName) {
		try {
			return new ArrayList<>(Files.readAllLines(Paths.get(fileName)));
		}
		catch (IOException e) {
			System.out.println(e);
		}
		return null;
	}

	private static void getSolutionOne(ArrayList<String> binaryNums) {
		String gammaRate = "";
		String epsilonRate = "";
		// For column in 2D array
		for (int i=0; i<binaryNums.get(0).length(); i++) {
			int numberOfOnes = 0;
			for (int j=0; j<binaryNums.size(); j++) {
				if (binaryNums.get(j).charAt(i) == '1') {
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
		System.out.println(Integer.parseInt(gammaRate, 2) * Integer.parseInt(epsilonRate, 2));
	}

	private static void getSolutionTwo(ArrayList<String> binaryNums) {
		ArrayList<String> oxygenGeneratorRatingValues = new ArrayList<>(binaryNums);
		ArrayList<String> co2ScrubberRatingValues = new ArrayList<>(binaryNums);
		String[] bitRules = getBitRules(binaryNums);
		String oxygenGeneratorBitRule = bitRules[0];
		String co2ScrubberBitRule = bitRules[1];

		// For each bit between 0 and 11, apply bitRule to remove values from values array until only 1 value remains,
		// which will be the rating value.
		String oxygenGeneratorRating = getRating(oxygenGeneratorRatingValues, oxygenGeneratorBitRule);
		String co2GeneratorRating = getRating(co2ScrubberRatingValues, co2ScrubberBitRule);
		assert oxygenGeneratorRating != null;
		assert co2GeneratorRating != null;
		System.out.println(Integer.parseInt(oxygenGeneratorRating, 2) * Integer.parseInt(co2GeneratorRating, 2));
	}

	// Based on getSolutionOne
	private static String[] getBitRules(ArrayList<String> binaryNums) {
		String oxygenBitRule = "";
		String co2BitRule = "";
		for (int i=0; i<binaryNums.get(0).length(); i++) {
			int numberOfOnes = 0;
			for (int j = 0; j < binaryNums.size(); j++) {
				if (binaryNums.get(j).charAt(i) == '1') {
					numberOfOnes++;
				}
			}
			int numberOfZeroes = binaryNums.size() - numberOfOnes;
			if (numberOfOnes > numberOfZeroes) {
				oxygenBitRule = oxygenBitRule + "1";
				co2BitRule = co2BitRule + "0";
			} else if (numberOfZeroes > numberOfOnes) {
				oxygenBitRule = oxygenBitRule + "0";
				co2BitRule = co2BitRule + "1";
			} else {
				oxygenBitRule = oxygenBitRule + "1";
				co2BitRule = co2BitRule + "0";
			}
		}
		return (new String[]{oxygenBitRule, co2BitRule});
	}

	private static String getRating(ArrayList<String> valuesToFilter, String bitRule) {
		for (int bit=0; bit < 12; bit++) {
			int arrIndex = 0;
			while (arrIndex < valuesToFilter.size()) {
				if (bitRule.charAt(bit) != valuesToFilter.get(arrIndex).charAt(bit)) {
					valuesToFilter.remove(arrIndex);
					if (valuesToFilter.size() == 1) {
						return valuesToFilter.get(0);
					}
				} else {
					arrIndex++;
				}
			}
		}
		return null;
	}
}
