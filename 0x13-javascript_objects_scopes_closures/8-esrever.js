#!/usr/bin/node
exports.esrever = function (list) {
  let a = list.length - 1;
  let z = 0;
  while ((a - z) > 0) {
    const aux = list[a];
    list[a] = list[z];
    list[z] = aux;
    z++;
    a--;
  }
  return list;
};
