#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const xx = Object.values(dict);
const uniqxx = [...new Set(xx)];
const a = {};
for (const z1 in uniqxx) {
  const list = [];
  for (const z2 in totalist) {
    if (totalist[z2][1] === uniqxx[z1]) {
      list.unshift(totalist[z2][0]);
    }
  }
  a[uniqxx[z1]] = list;
}
console.log(a);
