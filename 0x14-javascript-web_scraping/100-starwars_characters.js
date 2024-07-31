#!/usr/bin/node

const request = require('request');

const mainUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
let characters;

request(mainUrl, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  characters = data.characters;
  for (let i = 0; i < characters.length; i++) {
    request(characters[i], function (nerror, nresponse, nbody) {
      const charData = JSON.parse(nbody);
      console.log(charData.name);
    });
  }
});

/*
request(mainUrl, function (error, response, body) {
  if (error) console.error(error);
  const data = JSON.parse(body);
  for (let i = 0; i < data.results.length; i++) {
    for (let j = 0; j < data.results[i].characters.length; j++) {
      if (data.results[i].characters[j].includes('18')) count++;
    }
  }
  console.log(count);
}); */
