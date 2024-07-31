#!/usr/bin/node

const request = require('request');

const mainUrl = process.argv[2];
// const searchUrl = 'https://swapi-api.alx-tools.com/api/people/?search=Wedge';
// let wedgeUrl;
let count = 0;

/* Search for Wedge's url
request(searchUrl, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  wedgeUrl = data.results[0].url;
});
*/

// Count movies with Wedges's url
request(mainUrl, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  for (let i = 0; i < data.results.length; i++) {
    for (let j = 0; j < data.results[i].characters.length; j++) {
      if (data.results[i].characters[j].includes('18')) count++;
    }
    // if (data.results[i].characters.includes(wedgeUrl)) count++;
  }
  console.log(count);
});
