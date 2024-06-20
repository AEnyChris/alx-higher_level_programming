#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const result = list.filter((item) => item === searchElement);
  return result.length;
};
