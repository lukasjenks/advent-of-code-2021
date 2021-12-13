#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <bits/stdc++.h>
#include <string>

using namespace std;
class Crabs
{
    // Access specifier
    public:
 
    // Data Members
    int *crabArray;
    int *sortedCrabArray;
    int numCrabs;
    int minPosition;
    int maxPosition;

    int minCost;
    int minCostPosition;

    int minCost2;
    int minCostPosition2;

    // Member Functions
    int getFuelCost(int crabIndex, int position, int modifier) {
        if (modifier == 0) {
            return crabArray[crabIndex] > position ? crabArray[crabIndex] - position : position - crabArray[crabIndex];
        } else if (modifier == 1) {
            // each movement counts as 1 fuel + 1 fuel/number of times moved
            int numMovements = crabArray[crabIndex] > position ? crabArray[crabIndex] - position : position - crabArray[crabIndex];
            int fuelCount = 0;
            for (int i = 0; i < numMovements; i++) {
                fuelCount += 1 + i;
            }
            return fuelCount;
        } else {
            return -1;
        }
    }

    int getTotalFuelCost(int position, int modifier) {
        int totalFuelCost = 0;
        for (int i=0; i<numCrabs; i++) {
            totalFuelCost += getFuelCost(i, position, modifier);
        }
        return totalFuelCost;
    }

    int getSolution(int number) {
        int minCost = int(INFINITY);
        for (int i=minPosition; i<maxPosition; i++) {
            int fuelCost;
            if (number == 1) {
                fuelCost = getTotalFuelCost(i, 0);
            } else if (number == 2) {
                fuelCost = getTotalFuelCost(i, 1);
            }

            if (fuelCost < minCost) {
                minCost = fuelCost;
                minCostPosition = i;
            }
        }
        return minCost;
    }
};

std::string readStringFromFile(std::string fileName) {
    std::ifstream file(fileName);
    std::stringstream buffer;
    buffer << file.rdbuf();
    return buffer.str();
}

Crabs getCrabArray(std::string input) {
    // More space than it needs
    int *crabArray = new int[input.length()];
    std::string delimiter = ",";
    size_t pos = 0;
    std::string token;
    int i = 0;
    int maxPosition = 0;
    int minPosition = int(INFINITY);
    while ((pos = input.find(delimiter)) != std::string::npos) {
        token = input.substr(0, pos);
        crabArray[i] = std::stoi(token);
        if (crabArray[i] > maxPosition) {
            maxPosition = crabArray[i];
        }
        if (crabArray[i] < minPosition) {
            minPosition = crabArray[i];
        }
        i++;
        input.erase(0, pos + delimiter.length());
    }
    crabArray[i] = std::stoi(input);

    Crabs crabs;
    crabs.crabArray = crabArray;
    crabs.numCrabs = i+1;
    crabs.minPosition = minPosition;
    crabs.maxPosition = maxPosition;
    return crabs;
}

int main() {
    std::string fileContent = readStringFromFile("puzzle-input.txt");
    Crabs crabs = getCrabArray(fileContent);
    std::cout << "Part One Solution: " + std::to_string(crabs.getSolution(1)) << std::endl;
    std::cout << "Part Two Solution: " + std::to_string(crabs.getSolution(2)) << std::endl;
}