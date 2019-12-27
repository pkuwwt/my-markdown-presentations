
# How to Share Data with Docker Volume

  * Reference: 
    * [How To Share Data between Docker Containers](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-docker-containers) by Melissa Anderson
	* [How To Share Data Between the Docker Container and the Host](https://www.digitalocean.com/community/tutorials/how-to-share-data-between-the-docker-container-and-the-host) by Melissa Anderson

---

## Introduction

  * Docker is a popular containerization tool to provide a OS-like environment for applications to run
  * In general Docker container are ephemeral, however, data sharing or persitent is usually required
  * Docker Volumes can be created and attached to a container or multiple containers
  * Note: There is no file-lock when multiple containers mount the same volume
  * Prerequisites:
    * A non-root user with `sudo` privileges. Reference [Initial Server Setup with Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-18-04)
	* Docker installed: Step1 and Step2 of [How To Install and Use Docker on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)
	* Note: Docker also works on other OSs.


---

## Step 1 -- Creating an Independent Volume

  * Command: `docker volume create --name DataVolume1`
  * Test the volume, where
    * `ubuntu` is a docker image, pull it beforehand: `docker pull ubuntu`
	* `--rm` means the newly created container will be deleted when stopped
	* `-it` means to start an interactive terminal
	* After the container is stopped by command line `exit` or `Ctrl-D`, the `Example1.txt` is still in the volume

```bash
docker run -it --rm -v DataVolume1:/datavolume1 ubuntu`
echo "Examples" >/datavolume1/Example1.txt
exit
```

  * Inspect the volume: `docker volume inspect DataVolume1`
  * Verify the data:

```bash
docker run --rm -it -v DataVolume1:/datavolume1 ubuntu
cat /datavolume1/Example1.txt
```

---

## Step 2 -- Creating a Volume that Persists when the Container is Removed

  * Create a volume when creating a docker: 

```bash
docker run -it --name=Container2 -v DataVolume2:/datavolume2 ubuntu`
echo "Example2" >/datavolume2/Example2.txt
exit
```

  * When we restart `Container2`, `DataVolume2` will be mounted automatically

```bash
docker start -ai Container2
cat /datavolume2/Example2.txt
exit
```

  * The volume is not allowed to be deleted if referenced by a container

```bash
docker volume rm DataVolume2 # Error
```

  * When we delete `Container2`, the volume `DataVolume2` is still there

```bash
docker rm Container2
docker volume ls
docker volume rm DataVolume2 # Success
```

---

## Step 3 -- Creating a Volume from an Existing Directory with Data

  * `-v` option will automatically create a volume if not existed yet
  * Now we create a volume in a container, and show its data in another container

```bash
docker run -ti --rm -v DataVolume3:/var ubuntu
exit
docker run --rm -v DataVolume3:/datavolume3 ubuntu ls datavolume3
```

  * We will see the content in the original `/var` directory

---

## Step 4 -- Sharing Data Between Multiple Docker Containers

  * Create `Container4` and `DataVolume4`

```bash
docker run -ti --name=Container4 -v DataVolume4:/datavolume4 ubuntu
echo "This file is shared between containers" >/datavolume4/Example4.txt && exit
```

  * Create `Container5` and Mount Volumes from `Container4`, append some data

```bash
docker run -ti --name=Container5 --volumes-from Container4 ubuntu
echo "Both containers can write to DataVolume4" >>/datavolume4/Example4.txt && exit
```

  * View changes made in `Container5` (NB: **there is no file-lock in docker**)

```bash
docker start -ai Container4
cat /datavolume4/Example4.txt && exit
```

  * Start `Container5` and mount the volume Read-Only

```bash
docker run -ti --name=Container6 --volumes-from Container4:ro ubuntu
rm /datavolume4/Example4.txt # Error
```

---

## Step 5 -- Sharing data between host and docker

  * Mounting a host directory `/tmp` to a container directory `/data`

```bash
docker run -ti --name=Container6 -v /tmp:/data ubuntu
echo "This file is shared between containers" >/data/Example5.txt
exit
```

  * Access data from host

```bash
cat /tmp/Example5.txt
```

  * Revise data in host and access it in container

```bash
echo "Appended data" >>/tmp/Example5.txt
docker -ai Container6
cat /data/Example5.txt
exit
```

  * Clean up

```bash
docker rm Container6
```
