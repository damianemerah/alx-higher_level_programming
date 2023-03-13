#!/usr/bin/node

const x = Math.floor(+process.argv[2]);

if (isNaN(x))
	console.log('Missing size');
else
{
	let y = x;
	while (y > 0)
	{
		let row = '';
		for(let i = 0; i < x; i++)
			row += 'X';
		console.log(row);
		y--;
	}
}
