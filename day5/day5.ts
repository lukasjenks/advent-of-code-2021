import { stdin, stdout } from 'process';
import { line } from './line';

/*
    Following function is purposefully verbose for readability. 
*/
function getPuzzleInput (fileName : string) : [any[], number, number] {
	const fs = require('fs')
    let coordLines = [];
    let maxX = 0;
    let maxY = 0;

	try {
		const data : string = fs.readFileSync(fileName, 'utf8')
		const lines = data.split("\n");
        let insertIndex = 0;
        for (let lineNum=0; lineNum < lines.length; lineNum++)  {
            let coords : string[] = lines[lineNum].split(" -> ");
            let x1 : number = parseInt(coords[0].split(",")[0].trim());
            let y1 : number = parseInt(coords[0].split(",")[1].trim());
            let x2 : number = parseInt(coords[1].split(",")[0].trim());
            let y2 : number = parseInt(coords[1].split(",")[1].trim());

            if (x1 == x2 || y1 == y2) {
                coordLines.push({x1: x1, y1: y1, x2: x2, y2: y2});
                maxX = Math.max(maxX, x1, x2);
                maxY = Math.max(maxY, y1, y2);
            }
        }
        //console.log(coordLines);
	} catch (err) {
	    console.error(err)
	}
    //console.log(coordLines);
    return [coordLines, maxX, maxY];
}

function getSolutionOne(coordLines, maxX : number, maxY : number) : void {
    let grid = [];
    for (let y = 0; y <= maxY+1; y++) {
        grid[y] = [];
        for (let x = 0; x <= maxX+1; x++) {
            grid[y][x] = 0;
        }
    }
    for (let lineDef of coordLines) {
        let lineObj = new line(lineDef.x1, lineDef.y1, lineDef.x2, lineDef.y2);
        let coordsToAdd = lineObj.getLineCoords();
        console.log(lineDef)
        console.log(coordsToAdd);
        for (let coord of coordsToAdd) {
            // y, x
            grid[coord[1]][coord[0]]++;
        }
    }
    printGridMap(grid, maxX, maxY);
}

function printGridMap(grid: any[], maxX : number, maxY : number) {
    stdout.write("x  0 1 2 3 4 5 6 7 8 9\n");
    stdout.write("----------------------\n");
    for (let y = 0; y <= maxY; y++) {
        stdout.write(y.toString() + "| ");
        for (let x = 0; x <= maxX; x++) {
            stdout.write(grid[y][x].toString() + " ");
        }
        stdout.write("\n");
    }
}

const main = () => {
    const [coordLines, maxX, maxY] = getPuzzleInput('./day5EX.txt');
    //console.log(coordLines, maxX, maxY);
    getSolutionOne(coordLines, maxX, maxY);
}

main();

// 55523 too high

// 1814 wrong
// 1784 wrong