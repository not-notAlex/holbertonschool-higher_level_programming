#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const dic = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      if (tasks[i].completed) {
        if (dic[tasks[i].userId] === undefined) {
          dic[tasks[i].userId] = 1;
        } else {
          dic[tasks[i].userId]++;
        }
      }
    }
    console.log(dic);
  }
});
