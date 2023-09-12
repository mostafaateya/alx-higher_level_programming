#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let a = 0;
  for (let z1 = 0; z1 < list.length; z1++) {
    if (searchElement === list[z1]) {
      a++;
    }
  }
  return a;
};
