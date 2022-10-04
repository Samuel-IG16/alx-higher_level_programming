#!/usr/bin/node
module.exports = {
    addMeMaybe: function (n, f) {
	return f(n + 1);
    }
};
