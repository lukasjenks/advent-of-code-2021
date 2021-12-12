import { stdout } from 'process';
import { line } from './line';

/*
    Following function is purposefully verbose for readability. 
*/
function getPuzzleInput (fileName : string, questionNumber: number) : [any[], number, number] {
	const fs = require('fs');
    let coordLines = [];
    let maxX = 0;
    let maxY = 0;

	try {
		const data : string = fs.readFileSync(fileName, 'utf8')
		const lines = data.split("\n");
        for (let lineNum=0; lineNum < lines.length; lineNum++)  {
            let coords : string[] = lines[lineNum].split(" -> ");
            let x1 : number = parseInt(coords[0].split(",")[0]);
            let y1 : number = parseInt(coords[0].split(",")[1]);
            let x2 : number = parseInt(coords[1].split(",")[0]);
            let y2 : number = parseInt(coords[1].split(",")[1]);

            if (questionNumber === 1) {
                if (x1 == x2 || y1 == y2) {
                    coordLines.push({x1: x1, y1: y1, x2: x2, y2: y2});
                    maxX = Math.max(maxX, x1, x2);
                    maxY = Math.max(maxY, y1, y2);
                }
            } else if (questionNumber === 2) {
                coordLines.push({x1: x1, y1: y1, x2: x2, y2: y2});
                maxX = Math.max(maxX, x1, x2);
                maxY = Math.max(maxY, y1, y2);
            }
        }
	} catch (err) {
	    console.error(err);
        return err;
	}
    return [coordLines, maxX, maxY];
}

function getSolution(coordLines, maxX : number, maxY : number, partNumber: number) : void {
    let grid = [];
    for (let y = 0; y <= maxY+1; y++) {
        grid[y] = [];
        for (let x = 0; x <= maxX+1; x++) {
            grid[y][x] = 0;
        }
    }
    for (let lineDef of coordLines) {
        let lineObj = new line(lineDef.x1, lineDef.y1, lineDef.x2, lineDef.y2);
        let coordsToAdd : number[][];
        if (partNumber === 1) {
            coordsToAdd = lineObj.getStraightLineCoords();
        } else if (partNumber === 2) {
            coordsToAdd = lineObj.getAllLineCoords();
        }
        for (let coord of coordsToAdd) {
            grid[coord[1]][coord[0]]++;
        }
    }
    console.log("Part " + partNumber + " Solution: " + countOverlaps(grid, maxX, maxY));
}

// Function purely for visualizing grid for testing
function printGridMap(grid: any[], maxX : number, maxY : number) {
    stdout.write("x  ");
    for (let x = 0; x <= maxX; x++) {
        stdout.write(x + " ");
    }
    stdout.write("----------------------\n");
    for (let y = 0; y <= maxY; y++) {
        stdout.write(y.toString() + "| ");
        for (let x = 0; x <= maxX; x++) {
            stdout.write(grid[y][x].toString() + " ");
        }
        stdout.write("\n");
    }
}

function countOverlaps(grid: number[][], maxX : number, maxY : number) : number {
    let overlaps = 0;
    for (let y = 0; y <= maxY; y++) {
        for (let x = 0; x <= maxX; x++) {
            if (grid[y][x] > 1) {
                overlaps++;
            }
        }
    }
    return overlaps;
}

const main = () => {
    let [coordLines, maxX, maxY] = getPuzzleInput("./day5PuzzleInput.txt", 1);
    getSolution(coordLines, maxX, maxY, 1);
    [coordLines, maxX, maxY] = getPuzzleInput("./day5PuzzleInput.txt", 2);
    getSolution(coordLines, maxX, maxY, 2);
}

main();

// 55523 too high

// 1814 wrong
// 1784 wrong

// 20424 too low for part two