const assert = require('assert').strict;
names = ["Allan", "Bob"];
try{
	assert(names, "Two people like it");
	console.log("Two people like this!")
}catch(error){
	console.log("Errors", error);
}
