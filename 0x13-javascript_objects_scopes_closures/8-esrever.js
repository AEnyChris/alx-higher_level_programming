#!/usr/bin/node

exports.esrever = function (list) {
  const newArray = new Array(list.length);
  for (let i = 0; i < list.length; i++) {
    newArray[i] = list[list.length - (i + 1)];
    console.log(i);
  }
  return newArray;
};
