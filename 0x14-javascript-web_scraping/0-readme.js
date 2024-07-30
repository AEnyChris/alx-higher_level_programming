#!/usr/bin/node

const fs = require('fs').promises;
const filepath = process.argv[2];

async function readFile (filepath) {
  try {
    const data = await fs.readFile(filepath);
    console.log(data.toString());
  } catch (error) {
    console.error(error);
  }
}

readFile(filepath);
