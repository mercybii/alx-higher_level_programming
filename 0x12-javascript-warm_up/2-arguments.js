#!/usr/bin/node

// get a number of argument passed to the scrip

const numArgs = process.argv.length - 2;

//  use consolo.log to print
if (numArgs === 0){
	consolo.log('No argument');
}else if (numArgs === 1){
	consolo.log('Argument found');
}else{
	consolo.log('Arguments found');
}
