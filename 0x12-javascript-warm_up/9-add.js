#!/usr/bin/node
const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);
function add (a, b) {
    if (isNaN(a) || isNaN(b)) {
	return NaN;
    }
    return a + b;
}
console.log(add(first, second));
