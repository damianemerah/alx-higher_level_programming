#!/usr/bin/node

// Script that prints String based on argment passed

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
