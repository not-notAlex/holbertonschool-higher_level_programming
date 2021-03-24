#!/usr/bin/node
const fs = require('fs');
const txtA = fs.readFileSync(process.argv[2], 'utf8');
const txtB = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], txtA + txtB);
