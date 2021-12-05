import java.util.*;
import java.util.stream.Collectors;
import java.util.Collections;
import java.io.*;
import java.nio.file.*;

public class Day3 {
	public static void main(String[] args) {
		ArrayList<String> binaryNums = getPuzzleInput("./day3puzzleinput.txt");
		assert binaryNums != null;
		String[] bitRules = getSolutionOne(binaryNums);
		getSolutionTwo(binaryNums, bitRules);
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

	private static String[] getSolutionOne(ArrayList<String> binaryNums) {
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
			if (numberOfOnes >= numberOfZeroes) {
				gammaRate = gammaRate + "1";
				epsilonRate = epsilonRate + "0";
			} else {
				gammaRate = gammaRate + "0";
				epsilonRate = epsilonRate + "1";
			}
		}
		// output product of gammaRate converted to decimal and epsilonRate converted to decimal
		System.out.println(Integer.parseInt(gammaRate, 2) * Integer.parseInt(epsilonRate, 2));
		return(new String[]{gammaRate, epsilonRate});
	}

	private static void getSolutionTwo(ArrayList<String> binaryNums, String[] bitRules) {
		ArrayList<String> oxygenGeneratorRatingValues = new ArrayList<String>(binaryNums);
		ArrayList<String> co2ScrubberRatingValues = new ArrayList<String>(binaryNums);
		String oxygenGeneratorBitRules = bitRules[0];
		String co2ScrubberBitRules = bitRules[1];

		// For each bit between 0 and 11, apply bitRule to remove values from values array until only 1 value remains,
		// which will be the rating value.
		String oxygenGeneratorRating = getRating(oxygenGeneratorRatingValues, oxygenGeneratorBitRules);
		String co2GeneratorRating = getRating(co2ScrubberRatingValues, co2ScrubberBitRules);
		System.out.println(Integer.parseInt(oxygenGeneratorRating, 2) * Integer.parseInt(co2GeneratorRating, 2));
	}

	private static String getRating(ArrayList<String> valuesToFilter, String bitRule) {
		System.out.println("Bitrule is: " + bitRule);
		//System.out.println(bitRule);
		for (int bit=0; bit < valuesToFilter.get(0).length(); bit++) {
			for (int arrIndex = 0; arrIndex < valuesToFilter.size(); arrIndex++) {
				//System.out.println(bitRule.charAt(bit) + " vs: " + valuesToFilter.get(arrIndex).charAt(bit));
				if (bitRule.charAt(bit) != valuesToFilter.get(arrIndex).charAt(bit)) {
					//System.out.println("Removed.");
					valuesToFilter.remove(arrIndex);
					if (valuesToFilter.size() == 1) {
						return valuesToFilter.get(0);
					}
				} else {
					//System.out.println("Didn't remove.");
				}
			}
		}
		System.out.println("Didn't filter down to only one value. values left are: ");
		System.out.println(valuesToFilter);
		return valuesToFilter.get(0);
	}
}
