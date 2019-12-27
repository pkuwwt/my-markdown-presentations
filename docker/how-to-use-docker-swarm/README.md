
# How to Use Docker Swarm

  * Steps:
    * Preparation: install docker, configure firewall and ports 
	* Create docker swarm cluster
	* Add worker node to swarm cluster
	* Launch service in docker swarm

---

## Preparation

  * Install docker on each machine (node)
  * Make sure the following ports are available on all nodes:
    * TCP 2377: cluster management communications
	* TCP and UDP 7946: communications between nodes
	* UDP 4789: overlay network traffic
	* Service ports: e.g. 80
  * Some system open these port by default. If not, try the following firewall configuration:

```bash
for port in 2377/tcp 7946/tcp 7946/udp 4789/udp 80/tcp; do
    sudo ufw allow $port
done
sudo ufw reload && sudo ufw enable
sudo systemctl restart docker
```

  * If overlay network is created with encryption (`--opt encrypted`), make sure **ip protocol 50 (ESP)** traffic is allowed

---

## Create docker swarm cluster

  * Init a cluster on a machine with its ip. This node acts as manager node.

```bash
docker swarm init --advertise-addr 192.168.0.11
```

Output:
```background=black
Swarm initialized: current node (iwjtf6u951g7rpx6ugkty3ksa) is now a manager.
To add a worker to this swarm, run the following command:
    docker swarm join --token SWMTKN-1-v1cmjzq9ntx3zmck9kpgt... 192.168.0.11:2377
To add a manager to this swarm, 
   run 'docker swarm join-token manager' and follow the instructions.
```

  * `docker swarm join` is used to add worker to the cluster, the token is only required at join time.
  * Check the status of the manager node: `docker node ls`.

---

## Add worker node to swarm cluster

  * Add another machine to the cluster by

```bash
docker swarm join --token your-token 192.168.0.11.2377`
```

  * Then we can use `docker node ls` on the manager node to list the nodes in the cluster

---


## Launch service in docker swarm

  * Similar to `docker run`, we can create a service from image `httpd`

```bash
docker pull httpd
docker service create --name webserver -p 80:80 httpd
```

  * Operations

```bash
docker service scale webserver=2  # scale
docker service rm webserver       # delete
docker service ps webserver       # list services of webserver
docker node ps                    # list services
```

  * Now we can view the web service by accessing `http://192.168.0.11/` or ips of other nodes.

---

## Reference

  * [How to Install and Configure Docker Swarm on Ubuntu](https://www.dataquest.io/blog/install-and-configure-docker-swarm-on-ubuntu/)
  * [Swarm Tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/)

