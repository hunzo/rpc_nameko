# RPC test
## Start rabbitmq
```shell
docker-compose up -d
```
## Install nameko
```shell
pipenv install nameko
```
## Start RPC server
```shell
nameko run server amqp://guest:guest@localhost:5672
```
## Connect with Client
```shell
python client.py
```
