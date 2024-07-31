#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const output = {};

request(url, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  for (let i = 1; i <= 10; i++) {
    let count = 0;
    for (let j = 0; j < data.length; j++) {
      if (data[j].userId === i) {
        if (data[j].completed === true) {
          count++;
        }
      }
    }
    if (count) {
      output[`${i}`] = count;
    }
  }
  console.log(output);
});
