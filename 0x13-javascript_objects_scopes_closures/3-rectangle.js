#!/usr/bin/node
// Define a class Reactangle with fiels w and h
// and a print method

module.exports = class Rectangle {
  constructor (w, h) {
    if (!(w <= 0 || w === undefined || h <= 0 || h === undefined)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
