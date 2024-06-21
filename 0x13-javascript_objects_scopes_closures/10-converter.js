#!/usr/bin/node

exports.converter = function (base) {
  function theConvert (num) {
    return num.toString(base);
  }
  return theConvert;
};
