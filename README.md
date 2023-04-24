With Docker

Start by installing Docker if you haven't already done so. Then, open your terminal and run the following command:

````commandline
docker run -p 6379:6379 --name some-redis -d redis
````

This downloads the official Redis Docker image from Docker Hub and runs it on port 6379 in the background.

To test if Redis is up and running, run:
````commandline
docker exec -it some-redis redis-cli ping
````
You should see:
````commandline
PONG
````

<h5>Workers</h5>

````commandline
celery -A app.celery worker --loglevel=info -P threads
celery -A app.celery worker -l info --pool=solo
````

<h5>Flower</h5>

````commandline
celery -A app.celery flower --address=127.0.0.6 --port=5556 
celery -A app.celery flower --basic_auth=admin:admin --address=127.0.0.6 --port=5556
````


> É necessário rodar o worker e o flower ao mesmo tempo!

````commandline
flask shell
from app import divide 
task = divide.delay(1, 2)

from celery.result import AsyncResult

task = AsyncResult('deb23a1c-ac84-4a27-b926-14b05c4f2a69')
````
