#!/usr/bin/node
const fs = require('fs');

const a1 = fs.readFileSync(process.argv[2]).toString();
const a2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], a1 + a2);
