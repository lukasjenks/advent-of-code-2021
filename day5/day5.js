"use strict";
exports.__esModule = true;
var process_1 = require("process");
var line_1 = require("./line");
/*
    Following function is purposefully verbose for readability.
*/
function getPuzzleInput(fileName) {
    var fs = require('fs');
    var coordLines = [];
    var maxX = 0;
    var maxY = 0;
    try {
        var data = fs.readFileSync(fileName, 'utf8');
        var lines = data.split("\n");
        var insertIndex = 0;
        for (var lineNum = 0; lineNum < lines.length; lineNum++) {
            var coords = lines[lineNum].split(" -> ");
            var x1 = parseInt(coords[0].split(",")[0].trim());
            var y1 = parseInt(coords[0].split(",")[1].trim());
            var x2 = parseInt(coords[1].split(",")[0].trim());
            var y2 = parseInt(coords[1].split(",")[1].trim());
            if (x1 == x2 || y1 == y2) {
                coordLines.push({ x1: x1, y1: y1, x2: x2, y2: y2 });
                maxX = Math.max(maxX, x1, x2);
                maxY = Math.max(maxY, y1, y2);
            }
        }
        //console.log(coordLines);
    }
    catch (err) {
        console.error(err);
    }
    //console.log(coordLines);
    return [coordLines, maxX, maxY];
}
function getSolutionOne(coordLines, maxX, maxY) {
    var grid = [];
    for (var y = 0; y <= maxY + 1; y++) {
        grid[y] = [];
        for (var x = 0; x <= maxX + 1; x++) {
            grid[y][x] = 0;
        }
    }
    for (var _i = 0, coordLines_1 = coordLines; _i < coordLines_1.length; _i++) {
        var lineDef = coordLines_1[_i];
        var lineObj = new line_1.line(lineDef.x1, lineDef.y1, lineDef.x2, lineDef.y2);
        var coordsToAdd = lineObj.getLineCoords();
        console.log(lineDef);
        console.log(coordsToAdd);
        for (var _a = 0, coordsToAdd_1 = coordsToAdd; _a < coordsToAdd_1.length; _a++) {
            var coord = coordsToAdd_1[_a];
            // y, x
            grid[coord[1]][coord[0]]++;
        }
    }
    printGridMap(grid, maxX, maxY);
}
function printGridMap(grid, maxX, maxY) {
    process_1.stdout.write("x  0 1 2 3 4 5 6 7 8 9\n");
    process_1.stdout.write("----------------------\n");
    for (var y = 0; y <= maxY; y++) {
        process_1.stdout.write(y.toString() + "| ");
        for (var x = 0; x <= maxX; x++) {
            process_1.stdout.write(grid[y][x].toString() + " ");
        }
        process_1.stdout.write("\n");
    }
}
var main = function () {
    var _a = getPuzzleInput('./day5EX.txt'), coordLines = _a[0], maxX = _a[1], maxY = _a[2];
    //console.log(coordLines, maxX, maxY);
    getSolutionOne(coordLines, maxX, maxY);
};
main();
// 55523 too high
// 1814 wrong
// 1784 wrong
