#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (error, response, body) => {
	if (error){
    console.log(error);
  	} else {
	  const data = JSON.parse(body);

	  for(let i = 0; i < data.results.length; i++){
		  for(let j = 0; j < data.results[i].characters.length; j++){
			  if(data.results[i].characters[j].includes('18'))
                		count++;
		  }
	  }
	  console.log(count);
  }
});

