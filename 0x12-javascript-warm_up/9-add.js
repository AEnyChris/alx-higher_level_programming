#!/usr/bin/node

function add (a, b) {
  const num1 = parseInt(a);
  const num2 = parseInt(b);

  return num1 + num2;
}

const sum = add(process.argv[2], process.argv[3]);
console.log(sum);
