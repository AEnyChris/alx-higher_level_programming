#!/usr/bin/node
// Define a class Reactangle with fiels w and h
// and a print, rotate and double method

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
