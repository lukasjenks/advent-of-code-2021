#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// declare function that returns array of integers
int *getPuzzleInput(char* fileName) {
    FILE* file = fopen(fileName, "r");
    if (file == NULL) {
        printf("Error opening file\n");
        exit(1);
    }

    char *line;
    fscanf(file, "%s", &line[0]);

    int numOfNums = 0;
    for (int i=0; i<strlen(line); i++) {
        if (isdigit(line[i])) {
            printf("%c", line[i]);
            numOfNums++;
        }
    }

    int *puzzleInput = malloc((sizeof(int) * numOfNums) + 1);
    int puzzleInputInsertIndex = 0;
    for (int i=0; i<strlen(line); i++) {
        if (isdigit(line[i])) {
            puzzleInput[puzzleInputInsertIndex] = atoi(&line[i]);
            puzzleInputInsertIndex++;
        }
    }

    printf("\n");
    for (int i=0; i<sizeof(puzzleInput); i++) {
        printf("%d ", puzzleInput[i]);
    }
    return puzzleInput;
}

int getNumberOfFish() {
    return 0;
}

int main() {
    getPuzzleInput("day6EX.txt");
}