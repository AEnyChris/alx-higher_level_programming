#!/usr/bin/node

const fs = require('fs').promises;
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];

async function writeFile (data) {
  try {
    await fs.writeFile(filepath, data, 'utf8');
  } catch (error) {
    console.error(error);
  }
}

request(url, function (error, response, body) {
  if (error) console.err(error);
  writeFile(body);
});
