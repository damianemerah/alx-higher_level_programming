#!/usr/bin/node

// Script that prints first argument

console.log(typeof process.argv[2] === 'undefined' ? 'No argument' : process.argv[2]);
