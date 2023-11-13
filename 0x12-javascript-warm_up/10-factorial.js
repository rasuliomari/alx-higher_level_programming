#!/usr/bin/node

// The script that computes and prints a factorial.

function factorial (n) {
  if ((isNaN(n)) || (n === 1)) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const passVar = factorial(parseInt(process.argv[2]));
console.log(passVar);
