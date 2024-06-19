#!/usr/bin/node

const occu = process.argv[2];

if (isNaN(occu)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < occu; i++) {
    console.log('C is fun');
  }
}
