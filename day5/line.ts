class line {
    private x1: number;
    private x2: number;
    private y1: number;
    private y2: number;

    constructor(x1, y1, x2, y2) {
        this.x1 = x1;
        this.x2 = x2;
        this.y1 = y1;
        this.y2 = y2;
    }

    // Returns 2D array of x and y coordinates
    public getStraightLineCoords(this: line): number[][] {
        let coords: number[][] = [];
        if (this.x1 === this.x2 && this.y1 === this.y2) {
            coords.push([this.x1, this.y1]);
        } else if (this.x1 === this.x2) {
            // Determine if y is going up or down for length of line
            let increment : number = this.y1 < this.y2 ? 1 : -1;
            for (let y = this.y1; y !== this.y2; y += increment) {
                coords.push([this.x1, y]);
            }
            coords.push([this.x2, this.y2]);
        } else if (this.y1 === this.y2) {
            // Determine if x is going up or down for length of line
            let increment : number = this.x1 < this.x2 ? 1 : -1;
            for (let x = this.x1; x !== this.x2; x += increment) {
                coords.push([x, this.y1]);
            }
            coords.push([this.x2, this.y2]);
        }
        return coords
    }

    public getAllLineCoords(this: line): number[][] {
        let coords: number[][] = [];
        // Line is single point coordinate
        if (this.x1 === this.x2 && this.y1 === this.y2) {
            coords.push([this.x1, this.y1]);
        // Line is vertical
        } else if (this.x1 === this.x2) {
            let increment : number = this.y1 < this.y2 ? 1 : -1;
            for (let y = this.y1; y !== this.y2; y += increment) {
                coords.push([this.x1, y]);
            }
            coords.push([this.x2, this.y2]);
        // Line is horizontal
        } else if (this.y1 === this.y2) {
            let increment : number = this.x1 < this.x2 ? 1 : -1;
            for (let x = this.x1; x !== this.x2; x += increment) {
                coords.push([x, this.y1]);
            }
            coords.push([this.x2, this.y2]);
        // Line is diagonal
        } else {
            let xIncrement : number = this.x1 < this.x2 ? 1 : -1;
            let yIncrement : number = this.y1 < this.y2 ? 1 : -1;
            let x = this.x1;
            let y = this.y1;
            while (x !== this.x2 || y !== this.y2) {
                coords.push([x, y]);
                x += xIncrement;
                y += yIncrement;
            }
            coords.push([this.x2, this.y2]);
        }
        return coords
    }
}

export { line };