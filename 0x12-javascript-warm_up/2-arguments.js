#!/usr/bin/node

// print agument using consolo.log

const numArgs = process.argv.lenght - 2;

if (numArgs === 0){
	console.log('No argument')}
else if(numArgs === 1){
	console.log('Argument found')
}
else{
	consolo.log('Arguments found')
}
