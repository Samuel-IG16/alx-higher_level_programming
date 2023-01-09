#!/usr/bin/node

const SquareModel = require('./5-square');

module.exports = class Square extends SquareModel {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    this.print(c);
  }
};
