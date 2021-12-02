const getSolution1 = (sonarReadings) => {
	let increased = 0;
	for (let i=1; i<sonarReadings.length; i++) {
		if (sonarReadings[i] > sonarReadings[i-1]) {
			increased++;
		}
	}
	return increased;
}

const getSolution2 = (sonarReadings) => {
	let s = sonarReadings; // for brevity during arithmetic
	let increased = 0;
	// First comparison at index 3 - sum of 3,2,1 vs 2,1,0
	for (let i=3; i<sonarReadings.length; i++) {
		// Precompute common arithmetic: s[i-1] + s[i-2]
		let i1i2 = s[i-1] + s[i-2];

		// First group: s[i-1] + s[i-2] + s[i-3]
		// Second group: s[i] + s[i-1] + s[i-2]
		let firstGroup = i1i2 + s[i-3];
		let secondGroup = s[i] + i1i2;
		if (secondGroup - firstGroup > 0) {
			increased++;
		}
	}
	return increased;
}

const getPuzzleInput = () => {
	const fs = require('fs')

	try {
		const data = fs.readFileSync('./day1PuzzleInput.txt', 'utf8')
		const puzzleInput = data.split("\n").map( Number );
		return puzzleInput;
	} catch (err) {
	    console.error(err)
	}
}

const main = () => {
	let puzzleInput = getPuzzleInput();
	console.log(getSolution1(puzzleInput));
	console.log(getSolution2(puzzleInput));
}

main();
