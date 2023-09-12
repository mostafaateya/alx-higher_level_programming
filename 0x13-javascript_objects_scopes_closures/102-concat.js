#!/usr/bin/node
const a = require('a');

const a1 = a.readFileSync(process.argv[2]).toString();
const a2 = a.readFileSync(process.argv[3]).toString();
a.writeFileSync(process.argv[4], a1 + a2);
