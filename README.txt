This is a demo of using the Cat API (https://thecatapi.com).

To use this demo, you have to request an API at the following url:

http://thecatapi.com/api-key-registration.html

One you have your API key, please modify the docker-compose.yaml from 

API_KEY=MjI4NTA2

to 

API_KEY=<your api key>

Once you have recieved your key you can run the demo by running the following
command:


docker-compose up --build

To run the demo run the following command:

curl http://0.0.0.0:5000/cat

To see history of the cat pics one has requested:

curl http://0.0.0.0:5000/history

