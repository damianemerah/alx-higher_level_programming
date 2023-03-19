#!/usr/bin/node

const count = process.argv.length;
const { argv } = process;

console.log(count === 2 ? 'undefined is undefined' : count === 3 ? `${argv[2]} is undefined` : `${argv[2]} is ${argv[3]}`);
