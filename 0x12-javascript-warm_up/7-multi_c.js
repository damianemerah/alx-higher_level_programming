#!/usr/bin/node

let x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) { console.log('Missing number if occurrences'); } else {
  while (x > 0) {
    console.log('C is fun');
    x--;
  }
}
