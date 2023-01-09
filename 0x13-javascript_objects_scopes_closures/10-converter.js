#!/usr/bin/node

exports.converter = function (base) {
  function convert (number) {
    return number.toString(base);
  }

  return convert;
};
