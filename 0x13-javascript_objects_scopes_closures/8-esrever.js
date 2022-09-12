#!/usr/bin/node

exports.esrever = function (list) {
  const reversed = [];

  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }

  return reversed;
};
