#!/usr/bin/node

const numArray = process.argv.slice(2);

if (isNaN(numArray[0]) || numArray.length === 1) {
  console.log(0);
} else {
  console.log(numArray.sort((a, b) => (b - a))[1]);
}
