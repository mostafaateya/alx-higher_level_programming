#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let z1 = 0; z1 < this.height; z1++) {
      let a = '';
      for (let z2 = 0; z2 < this.width; z2++) {
        a += c;
      }
      console.log(a);
    }
  }
}

module.exports = Square;
