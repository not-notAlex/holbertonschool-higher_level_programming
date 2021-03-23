#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((i, index) => i * index);
console.log(list);
console.log(newList);
