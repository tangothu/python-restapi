Commands:
source tasks.sh
tasks add "write some code" 21/08/2019
tasks list
tasks list --expiring-today
tasks done 3


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