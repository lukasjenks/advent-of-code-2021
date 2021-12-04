import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Day3 {
	public static void main(String[] args) {
		ArrayList<String> binaryNums = getPuzzleInput("./day3puzzleinput.txt");
		getSolutionOne(binaryNums);
		getSolutionTwo(binaryNums);
	}

	private static ArrayList<String> getPuzzleInput(String fileName) {
		try {
			ArrayList<String> lines = new ArrayList<>(Files.readAllLines(Paths.get(fileName)));
			return lines;
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
		System.out.println("gammaRate: " + gammaRate);
		System.out.println("epsilonRate: " + epsilonRate);
		// output product of gammaRate converted to decimal and epsilonRate converted to decimal
		System.out.println(Integer.parseInt(gammaRate, 2) * Integer.parseInt(epsilonRate, 2));
	}

	private static String getBitRule(ArrayList<String> binaryNums, String chemical) {
		String bitRule = "";
		for (int i=0; i<binaryNums.get(0).length(); i++) {
			int numberOfOnes = 0;
			for (int j=0; j<binaryNums.size(); j++) {
				if (binaryNums.get(j).charAt(i) == '1') {
					numberOfOnes++;
				}
			}
			int numberOfZeroes = binaryNums.size() - numberOfOnes;
			if (numberOfOnes > numberOfZeroes) {
				if (chemical.equals("oxygen")) {
					bitRule = bitRule + "1";
				} else if (chemical.equals("co2")) {
					bitRule = bitRule + "0";
				}
			} else if (numberOfOnes < numberOfZeroes) {
				if (chemical.equals("oxygen")) {
					bitRule = bitRule + "0";
				} else if (chemical.equals("co2")) {
					bitRule = bitRule + "1";
				}
			} else if (numberOfOnes == numberOfZeroes) {
				if (chemical.equals("oxygen")) {
					bitRule = bitRule + "1";
				} else if (chemical.equals("co2")) {
					bitRule = bitRule + "0";
				}
			}
		}
		return bitRule;
	}

	// If 0 and 1 are equally common, keep both...
	private static void getSolutionTwo(ArrayList<String> binaryNums) {
		String oxygenMask = getBitRule(binaryNums, "oxygen");
		String co2Mask = getBitRule(binaryNums, "co2");
		ArrayList<String> oxygenValues = new ArrayList<String>(binaryNums);
		ArrayList<String> co2Values = new ArrayList<String>(binaryNums);
		int numCols = binaryNums.get(0).length();
		// Now apply mask to remove entries from the arrays
		int i = 0, j = 0;
		calcOxygen:
		for (i=0; i<numCols; i++) {
			//System.out.println("oxygen");
			//System.out.println(i);
			for (int x=0; x<oxygenValues.size(); x++) {
				//System.out.println("i: " + i + " x: " + x);
				//System.out.println("oxygenMask is " + oxygenMask);
				//System.out.println("oxygenValues is " + oxygenValues.get(x));
				//System.out.println("oxygenMask char at i is: " + oxygenMask.charAt(i));
				//System.out.println("oxygenValues char at i is: " + oxygenValues.get(x).charAt(i));
				if (oxygenMask.charAt(i) != oxygenValues.get(x).charAt(i)) {
					//System.out.println("Removing oxygen value at index: " + x);
					System.out.println("Old size of oxygenValues: " + oxygenValues.size());
					//System.out.println("Size is: " + oxygenValues.size());
					oxygenValues.remove(x);
					System.out.println("New size of oxygenValues: " + oxygenValues.size());
					//System.out.println(oxygenValues);

					if (oxygenValues.size() == 1) {
						//System.out.println("break; found oxygen");
						break calcOxygen;
					}
				}
			}
		}
		calcCo2:
		for (j=0; j<numCols; j++) {
			//System.out.println("co2");
			//System.out.println(j);
			//System.out.println(co2Values.size());
			for (int x=0; x<co2Values.size(); x++) {
				if (co2Mask.charAt(j) != co2Values.get(x).charAt(j)) {
					co2Values.remove(x);
					//System.out.println(co2Values);
					if (co2Values.size() == 1) {
						//System.out.println("break; found co2");
						break calcCo2;
					}
				}
			}
		}
		System.out.println("oxygenMask: " + oxygenMask);
		System.out.println("co2Mask: " + co2Mask);
		System.out.println("oxygenValues: " + oxygenValues);
		System.out.println("co2Values: " + co2Values);
		//System.out.println("oxygen scrubber rating:" + oxygenValues.get(0));
		//System.out.println("co2 scrubber rating:" + co2Values.get(0));
		//System.out.println("oxygen srubber rating: " + Integer.parseInt(oxygenValues.get(0),2));
		//System.out.println("co2 srubber rating: " + Integer.parseInt(co2Values.get(0),2));
		// output product of co2 converted to decimal and oxygen converted to decimal
		System.out.println(Integer.parseInt(oxygenValues.get(0), 2) * Integer.parseInt(co2Values.get(0), 2));
	}
}

