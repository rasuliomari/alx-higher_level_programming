#!/usr/bin/node

// A function that prints the number of arguments
// already printed and the new argument value. (see example below)

let count = 0;
exports.logMe = function (item) { console.log(`${count++}: ${item}`); };
