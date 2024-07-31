#!/usr/bin/node

const fs = require('fs').promises;
const filepath = process.argv[2];
const data = process.argv[3];

async function writeFile () {
  try {
    await fs.writeFile(filepath, data, 'utf8');
  } catch (error) {
    console.error(error);
  }
}

writeFile();
