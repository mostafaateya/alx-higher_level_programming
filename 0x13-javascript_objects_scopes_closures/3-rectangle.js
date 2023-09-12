#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let z1 = 0; z1 < this.height; z1++) {
      let a = '';
      for (let z2 = 0; z2 < this.width; z2++) {
        a += 'X';
      }
      console.log(a);
    }
  }
}

module.exports = Rectangle;
