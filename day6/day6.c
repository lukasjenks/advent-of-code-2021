#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

struct Fish {
  int *fish;
  int numberOfFish;
};

// declare function that returns array of integers
struct Fish getPuzzleInput(char* fileName) {
    FILE* file = fopen(fileName, "r");
    if (file == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    char *line = malloc(sizeof(char) * 2048);
    fscanf(file, "%s", &line[0]);

	int *puzzleInput = (int *)malloc((sizeof(int)) * 2048);
	if (puzzleInput == NULL) {
	  printf("Error encountered while mallocing for puzzleInput\n");
	  exit(1);
	}
	
    int numOfNums = 0;
	int puzzleInputInsertIndex = 0;
    for (int i=0; i<strlen(line); i++) {
        if (isdigit(line[i])) {
            puzzleInput[puzzleInputInsertIndex] = atoi(&line[i]);
            puzzleInputInsertIndex++;
            numOfNums++;
        }
    }
	free(line);

    puzzleInput = realloc(puzzleInput, numOfNums * sizeof(int));
	if (puzzleInput == NULL) {
	  printf("Error encountered while reallocing for puzzleInput\n");
	  exit(1);
	}

	struct Fish Fish;
	Fish.fish = puzzleInput;
	Fish.numberOfFish = numOfNums;
    return Fish;
}

int getNumberOfFish(struct Fish fish, int numberOfDays) {
	for (int i=0; i<numberOfDays; i++) {
	  for (int j=0; j<fish.numberOfFish; j++) {
		switch(fish.fish[j]) {
		case 0:
		  fish.fish[j] = 6;
		  fish.fish = realloc(fish.fish, (fish.numberOfFish+1) * sizeof(int));
		  if (fish.fish == NULL) {
			printf("Error encountered while reallocing for fish.fish\n");
			exit(1);
		  }
		  fish.fish[fish.numberOfFish] = 9; //9 instead of 8 because it will get decremented
		  fish.numberOfFish++;
		  break;
		default:
		  fish.fish[j]--;
		  break;
		}
	  }
	}
    return fish.numberOfFish;
}


int main() {
    struct Fish fish = getPuzzleInput("day6PuzzleInput.txt");
	int numOfFish = getNumberOfFish(fish, 256);
	// 256 - 80 = 176, prior call to getNumberOfFish changes fish.fish array.
	printf("Part One Solution: %d\nPart Two Solution: %d\n", getNumberOfFish(fish, 80), getNumberOfFish(fish, 176));
	free(fish.fish);
}
