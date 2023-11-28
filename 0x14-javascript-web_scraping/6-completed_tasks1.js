#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const count = 0;

request.get(url, (error, response, body) => {
	if(error) {
		console.log(error);
	}else {
		const data = JSON.parse(body);
		let userId  = data.userId;
		let completed = data.completed;

		for(let i = 0; i < 

	}
});
