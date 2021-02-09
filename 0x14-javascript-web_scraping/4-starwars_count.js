#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const i in films) {
      const chars = films[i].characters;
      for (const c in chars) {
        if (chars[c].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
