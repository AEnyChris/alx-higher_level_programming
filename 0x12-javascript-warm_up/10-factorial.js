#!/usr/bin/node

function factorial (a) {
  const num = parseInt(a);
  if (num <= 1 || isNaN(num)) {
    return 1;
  }
  return a * factorial(a - 1);
}

const result = factorial(process.argv[2]);
console.log(result);
