"use strict";
exports.__esModule = true;
exports.line = void 0;
var line = /** @class */ (function () {
    function line(x1, y1, x2, y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }
    // Returns 2D array of x and y coordinates
    line.prototype.getLineCoords = function () {
        var coords = [];
        if (this.x1 === this.x2 && this.y1 === this.y2) {
            coords.push([this.x1, this.y1]);
        }
        else if (this.x1 === this.x2) {
            // Determine if x is going up or down
            var increment = this.y1 < this.y2 ? 1 : -1;
            for (var y = this.y1; y !== this.y2; y += increment) {
                coords.push([this.x1, y]);
            }
            coords.push([this.x2, this.y2]);
        }
        else if (this.y1 === this.y2) {
            var increment = this.x1 < this.x2 ? 1 : -1;
            for (var x = this.x1; x !== this.x2; x += increment) {
                coords.push([x, this.y1]);
            }
            coords.push([this.x2, this.y2]);
        }
        return coords;
    };
    return line;
}());
exports.line = line;
