#!/usr/bin/node
module.exports = {
    callMeMoby: function (n, f) {
	for (let i = 0; i < n; i++) {
	    f();
	}
    }
};
