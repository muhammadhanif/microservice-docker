# microservice-docker
A simple microservice using Docker container

### Requirements
* Docker Engine
* Docker Compose

### Topology

![alt text][topology]

[topology]: https://raw.githubusercontent.com/muhammadhanif/microservice-docker/master/topology.png "Topology"

### APP Stack

* Python: flask
* Node.js: express
* Golang: echo

### How to run
```
git clone https://github.com/muhammadhanif/microservice-docker
```

```
cd microservice-docker
```

```
docker-compose up -d
```

```
docker-compose ps
```

### Accessing web app

Open http://your-docker-host-ip-address:8888 in browser.

### Destroy Containers

```
docker-compose down --rmi all
```
