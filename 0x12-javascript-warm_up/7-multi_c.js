#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
    console.log('Missing number of occurrences');
} else {
   for (let i = 0; i < times; i++) {
       console.log('C is fun');
    }
}
