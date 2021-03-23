#!/usr/bin/node
exports.esrever = function (list) {
  let s = 0;
  let e = list.length - 1;
  while (s < e) {
    const temp = list[s];
    list[s] = list[e];
    list[e] = temp;
    e--;
    s++;
  }
  return list;
};
