QuickStart is here:

https://angular.io/guide/quickstart

This QuickStart information at the above link will help with setup.

The tutorial is here:

https://angular.io/tutorial

Change to the official tutorial are in this section:

https://angular.io/tutorial/toh-pt6

"Rather than require a real API server, this example simulates communication with the remote server by adding the InMemoryWebApiModule"

Instead of using the InMemoryWebApiModule you will be able to use MongoDB with bottle API all running on the localhost.

Set up

1 - install everything in the QuickStart, MongoDB, Python, Bottle (python web framework for api)
2 - create database heroes in Mongo
3 - load seed data
	db.heronames.insertMany([
	      { id: 0,  name: 'Zero' },
	      { id: 11, name: 'Mr. Nice' },
	      { id: 12, name: 'Narco' },
	      { id: 13, name: 'Bombasto' },
	      { id: 14, name: 'Celeritas' },
	      { id: 15, name: 'Magneta' },
	      { id: 16, name: 'RubberMan' },
	      { id: 17, name: 'Dynama' },
	      { id: 18, name: 'Dr IQ' },
	      { id: 19, name: 'Magma' },
	      { id: 20, name: 'Tornado' }
	]);

4 - Open new terminal $> python ./API-Python/mongo-api.py

5 - Open new terminal
	$> cd ./angular-tour-of-heros

	$> npm start

Thanks to Google for the excellent tutorial. Thanks to the people that wrote articles on how to overcome the CORS problems.

Good Luck.

