#!/usr/bin/node

const fs = require('fs');

const src1 = process.argv[2];

const src2 = process.argv[3];

const dest = process.argv[4];

function callback (err, data) {
  if (err) {
    return console.log(err);
  }

  fs.appendFile(dest, data, function (err) {
    if (err) console.log(err);
  });
}

fs.readFile(src1, 'utf8', callback);

fs.readFile(src2, 'utf8', callback);
