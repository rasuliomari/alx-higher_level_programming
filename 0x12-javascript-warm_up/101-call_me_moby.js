#!/usr/bin/node

// This function that executes x times a function.

exports.callMeMoby = function callMeMoby (x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
