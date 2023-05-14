#!/usr/bin/node
// prints the title of a star ears movie

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
    process.exit(1);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
