
# Task restapi project

Kevin Tan's demo of python restapi based on flask and swagger

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 



### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
Unix bash
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
git clone https://github.com/tangothu/python-restapi
python3 -m pip install --upgrade pip
pip3 install virtualenv
virtualenv -p `which python3` venv
source venv/bin/activate
```
To run the application local
```
cd python-restapi
python build_database.py
python server.py
```

To run the application from bash to create / delete / query tasks
``` 
source tasks.sh
tasks add "write some code" 21/08/2019
tasks list
tasks list --expiring-today
tasks done 3
```


## Running the tests

TODO

## Deployment

This project runs on localhost and deployment is TODO

## Authors

* **Kevin Tan** - *Initial work* - [python-restapi](https://github.com/tangothu/python-restapi)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Other notes

Log location:
/tmp/python_restapi_logfile.log

Notes:
swagger UI:
http://localhost:5000/api/ui/#/

curl Examples: 
GET(get 1):
curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/tasks/1'

GET(get all):
curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/tasks'

PUT(update):
curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/problem+json' -d '{ "title": "my new task" }' 'http://localhost:5000/api/tasks/1'
 
DELETE(delete):
curl -X DELETE --header 'Accept: text/html' 'http://localhost:5000/api/tasks/3'

POST(create):
curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ "title": "Do 10000 JIRAs" }' 'http://localhost:5000/api/tasks'

