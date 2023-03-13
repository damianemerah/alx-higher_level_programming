#!/usr/bin/node

// Script that prints String based on argment passed

const count = process.argv.length;

console.log(count === 3 ? 'Argument found' : count > 3 ? 'Arguments found' : 'No argument found');
