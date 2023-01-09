#!/usr/bin/node
const list = require('./101-data').dict;
const sorted = {};

Object.keys(list).forEach(key => {
  if (sorted[list[key]] === undefined) sorted[list[key]] = [];

  sorted[list[key]].push(key);
}
);
console.log(sorted);
