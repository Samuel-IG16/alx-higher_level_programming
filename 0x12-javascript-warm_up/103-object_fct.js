#!/usr/bin/node
const myObject = {
    type: 'object',
    value: 12
};
console.log(myObject);
myObject.incr = function () {
    return this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
