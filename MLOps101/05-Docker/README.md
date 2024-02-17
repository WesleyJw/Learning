# Working with Docker

Author: PhD. Wesley Lima

## What is Docker?

In the primary definition of the term, Docker is an open platform for developing, delivering, and running applications. Docker is essentially a service manager via containers. The main idea behind Docker, for developers, is to make application development easy within containers that can be used anywhere.

For Docker installation, refer to this [link](https://www.tutorialspoint.com/docker/installing_docker_on_linux.htm).

---

## Container Architecture

To understand the functioning architecture of Docker, let's first understand how traditional virtualization via virtual machines works. Initially, all virtualization processes were carried out on a server (physical machine), within a host (operating system), controlled by a Hypervisor [VMWare or Hyper/V on Windows] (responsible for managing virtualization), followed by the new operating system to be used, and finally the applications. Some characteristics of this type of virtualization are that the reserved memory is usually fixed, even if the system doesn't utilize it all, it still holds that reservation; however, if the application needs more memory, it won't be available immediately. It's needless to say that this mode consumes a lot of server resources.

![Image depicting the architecture of virtualization via virtual machines](./images/virtualization.jpg)

The new form of virtualization via containers allows generating virtual groups directly with the application via the Docker engine from a server with an operating system. This allows much more scalability, resource efficiency, agility, among other things.

![Image depicting the architecture of virtualization via Docker](./images/various_layers.jpg)

---

## Getting Started with Docker via Command Line

To check the Docker version, execute:

```bash
docker version
```

The keyword _docker_ informs the Docker program in the operating system that something needs to be executed.

Or to check general information:

```bash
docker info
```

### Configuration

It's important to log in to Docker to be able to download images onto your machine.

```bash
docker login -u="loginName" -p="password"
```

If by chance you need to stop Docker (docker daemon process), use the following command:

```bash
service docker stop
```

To start the Docker service again, use:

```bash
service docker start
```

---

## Docker Images

It's important to know that everything in Docker is based on images. But what exactly is a Docker image? Well, an image is nothing more than a combination of system files (commonly known as the file system) and parameters. Here's how we create a Docker image:

```bash
docker run hello-world
```

- The **run** command indicates that we want to create an instance of an image, which is called a container.
- The term **hello-world** is the image in which the container is created.

In the next section, we'll define what a container is to dispel any doubts you may have. It's common for them to persist up to this point.

Executing the above command in your terminal returned a series of _logs_ and printed the text "hello-world", then your terminal line returned. This Docker image was created for this purpose.

Now, creating a new container, let's see how we can use the Debian image available on Docker Hub to run Debian on our local machine. Let's execute the following command:

```console

docker run -it debian /bin/bash

Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
5e0b432e8ba9: Pull complete
Digest: sha256:45ee40a844048c2f6d0105899c1a17733530b56d481612608aab5e2e4048570b
Status: Downloaded newer image for debian:latest
root@f365cf13cb79:/#
```

The second block of information is the _output_ of the first command, note that our Docker program didn't find the image locally, fetched the image from Docker Hub, and instantiated a new container from the downloaded image. In the end, it returned the command line of the system terminal that is running inside the container.

- The **-it** command is used to indicate that we want to run in interactive mode.
- The term **/bin/bash** is used to execute the bash shell (terminal) when Debian is running. (debian is up and running).

### Listing Images

It's important to know that downloading an image only happens the first time you run this image; subsequently, Docker checks if the image already exists on your machine. Thus, it uses this local image to instantiate future containers. To check the available images on your system (_host_), execute the following command:

```console
docker images

REPOSITORY                                      TAG                  IMAGE ID       CREATED         SIZE
wesleyjw/datascienceimg                         latest               093210c05050   2 days ago      3.99GB
debian                                          latest               05d2318291e3   7 days ago      124MB
bash                                            latest               6a03c8e7e2be   2 weeks ago     12.9MB
mongo                                           latest               4253856b2570   3 weeks ago     701MB
ubuntu                                          18.04                5a214d77f5d7   2 months ago    63.1MB
```

Reviewing the output of the command, we find five images on our machine. We can check the attributes of each image:

- **REPOSITORY**: Represents the image's name.
- **TAG**: A logical tagging parameter of the image;
- **IMAGE ID**: Used as the unique identifier of the image;
- **CREATED**: Identifies the number of days since the creation of the image;
- **SIZE**: The size of the image.

### Removing Docker Images

To remove Docker images from your machine, use the following command:

```console
docker rmi <ImageName or ImageId>

docker rmi 5a214d77f5d7
```

- **ImageName or Repository**: Image name;
- **ImageId**: Image ID;

To return only the IDs of the available images, execute:

```console
docker images -q
```

- **-q**: Instructs Docker to return only the IDs of the images.

If you want to know more information about a specific image, use the command:

```console
docker inspect <Repository>

docker inspect mongo
```

---

## Docker Container

What is a Docker container? By definition, a container is an isolated environment, arranged on a server, which separates a single host (operating system) for control. Informally, we can say that a container is a isolated portion of memory, where we can run operating systems, all controlled by the Docker engine within your operating system (host).

To better understand, consider the following situation: Imagine your operating system is a cargo ship, and you have a cargo of products of various natures: cleaning materials, technology products, refrigeration-requiring food products, medical items, among others. You've realized that it's not possible to transport all of this without organizing the products by types and mode of transport. Since we're talking to the ship's captain, arrange various containers ideal for each type of product.

Returning to our area now, consider the development of software that needs, to

 function correctly, a SQL database (Postgres), its database administrator (pgAdmin4), a NoSQL database (MongoDB) along with its administrator, a frontend development framework (React), another for backend development (Django), plus a server for data analysis and machine learning (Jupyter Notebook with Anaconda). All these tools have their dependencies, so conflicts may arise during the installation and configuration of each one. Who hasn't lost days preparing development environments? Another big problem arises when you need to share your project with coworkers, who hasn't used the phrase "it works on my machine"?

Docker, with its container creation methodology, emerges to solve this problem. With it, it's possible to instantiate containers with each of the applications from available images. So now you can create containers with the specific images of your project without interference from dependencies and share the commands used with your colleagues, ensuring that they will have environments with the same configurations as yours.

In the best practices of using containers, each container should be used for a single service and function, meaning if you need a Postgres database, instantiate a container with just that function. This way, we ensure that if a container fails (any problem occurs with it), only its functionality will cease to operate. Our application continues to run, and it's much faster and simpler to instantiate another container with that functionality.

### Listing Containers

First, let's instantiate a container in interactive mode with the following command:

```console
docker run -it debian /bin/bash
```

To return to the command line (shell of your operating system), press Ctrl + p and then Ctrl + q. You can also exit by pressing Ctrl + d or typing the _exit_ command, but in this case, the container is stopped. Use the first combination to continue with the example; if you've already killed the container, no worries, run it again with the previous command.

Now let's check if the container is running.

```console
docker ps
```

This returns the following _output_:

```console
name@Inspiron-5448:~$ docker ps
CONTAINER ID   IMAGE                    COMMAND        CREATED          STATUS         PORTS      NAMES
acce8600f36c   debian                   "bash"         10 seconds ago   Up 8 seconds              jolly_zhukovsky
3deb5e8253e1   portainer/portainer-ce   "/portainer"   8 months ago     Up 10 hours    8000:9000  portainer
```

Now let's list all containers on the system, including inactive and stopped containers:

```console
docker ps -a
```

- **-a** instructs the docker ps command to list all containers on the operating system.

Another useful command is _history_ to know the usage history of the container:

```console
docker history <ContainerID>

docker history acce8600f36c
```

- **ContainerID**: Container ID.

---

## Working with Containers

### Docker start

How to initialize a container:

```console
docker start <ContainerID or ContainerName>

docker start wesleytest ls
```

- The **ls** command lists the files and folders of a directory; in this case, it will list everything in the root of the container.

### Docker top

With this command, it's possible to check the processes consuming the most resources within the container:

```console
docker top <ContainerID>

docker top  2270220a21e3
```

_output_:

```console
UID         PID        PPID         C            STIME        TTY          TIME         CMD
root        3682       3657         0            09:22        ?            00:00:09     /portainer
```

### Docker stop

Used to stop a running container.

```console
docker stop <ContainerID>

docker stop  2270220a21e3

docker stop <ContainerName>

docker stop debian
```

### Docker rm

Removing a container

```console
docker rm <ContainerID>

docker rm <ContainerName>

docker rm debian
```

### Docker stats

Checking container statistics.

```console
docker stats <ContainerID>

docker stats <ContainerName>

docker stats debian
```

### Docker logs

To check the logs of a container. This command is important when you need to verify configuration information, passwords for other dependent applications.

```console

docker logs <ContainerName> or <ContainerID>

docker logs c959f10607d1

docker logs -f c959f10607d1
```

- **-f**: check iterative logs.

### Docker prune

Removing all inactive containers

```console
docker system prune
```

Following the same logic of commands, we also have: docker attach - to enter a running container, docker pause - to pause the execution of a running container, docker unpause - to unpause, docker kill to kill a running container.

### The Life Cycle of a Container

![Image depicting the life cycle of a container](./images/container_lifecycle.jpg)

---

## Further Work with Containers

### Docker --rm

Instantiate a container while removing other containers of the same image that already exist.

```console
docker run --rm alpine echo "Hello world"
```

- **run**: always create new containers
- **--rm**: this command always removes an existing container to execute the second one.

### Docker exec

Execute commands in a running container:

```console
docker run exec <ContainerID or ContainerName>  <linuxcomand>

docker run exec wesleytest ls
```

### Docker tag

When we don't specify a tag for the image version, Docker always fetches the _latest_ version. With the following command, we can create a container with the Ubuntu image tagged with the version.

```console
docker run ubuntu:18.04 cat /etc/issue
```

- **cat /etc/issue** displays the Ubuntu version at the end of execution.

### Docker -d

Create a container and run it in the background.

```console
docker run -d alpine sleep 20
```

- **-d**: run the container in the background, meaning the console returns to the user;
- **sleep**: puts the program to sleep for the determined time.

### Combining various Docker commands

Instantiate a container, name it, and run it in the background along with an execution command:

```console
docker run -d --name wesleytest alpine sleep 20
```

- **--name**: Naming the container.

---

## Working with Volumes in Containers

### Docker Volumes

Docker volumes are filesystems mounted within a Docker container to preserve data generated by a running container. These volumes (filesystems) are saved on the host, independent of the container's lifecycle. This means that if data is produced and saved during the execution of a service within a container, and these data need to persist even if the container is destroyed, volumes allow sharing this container data with the host. By specifying the shared volume as **"VOL.host:VOL.container"**, every time the container runs, it can save data in this volume, which persists on the host. Each time the container starts, it can read the saved data and perform any necessary updates. This process can occur indefinitely.

How can you share volumes between the host and container? Let's instantiate a container and specify a volume for sharing between the host and container.

```console
docker container run -d --name linux -v "<dir-host:dir-container>" image

# Example 1
docker container run -d --name linux -v "/data/server:/tmp" ubuntu:18.04

# Example 2
docker container run -d --name linux -v "home/user/data:/tmp" ubuntu:18.04 sleep 2000
```

- **-d**: Run the container in the background. (Frees up the console line);
- **--name**: Name of the container;
- **-v**: Specify the volume to be shared;
- **dir-host**: Path to the directory to be shared on the host side;
- **dir-container**: Path to the directory to be shared on the container side;
- **sleep**: Command executed inside the container.

Another way to create a volume is by using the _pwd_ command to specify part of a path. In this case, the code looks like this:

```console
$ pwd

docker container run -d --name linux -v "$PWD/data:/tmp" ubuntu:18.04 sleep 2000
```

### Some Commands for Volumes

To list all volumes that have been created, execute the following command:

```console
docker volume ls

# Pending volumes
docker volume ls -f dangling=true
```

To remove a volume:

```console
docker volume rm vol_name1 vol_name2
```

Remove pending volumes:

```console
docker volume prune
```

Removing the container and the volume together:

```console
docker rm -v containerName
```

---

## Environment Variables

```console
docker container run --name linux2 -e vartest="environment variable" ubuntu env
```

---

## Port Management

```console
docker container run -d --name <containername> -p <PORT.host:PORT.container> image

docker container run -d --name webserver -p 8080:80 nginx
```

- **-p**: Indicates port sharing;
- **PORT.host**: Indicates the host port to be opened (shared);
- **PORT.container**: Indicates the container port to be opened (shared);

---

## Dockerfile

Up to this point, we've learned that to instantiate a container, we simply need to download an image and execute the docker run command with the required specifications. You might wonder where all these images come from and how to know about their existence. I won't go into detail here, but you can find countless images on a site called Docker Hub, and you can also upload images you've created yourself by simply logging in to the site.

All good so far? Now you might be thinking, how do I create my images with the configurations I need? Even if you start a container and install various development programs, when you stop the container, all these changes disappear. How can you persist this? To avoid wasting time having to make all the same configurations every time you start a container, there's the Dockerfile. A Dockerfile is simply a text file with instructions on how you want to build your image.

Let's see the process of creating a Dockerfile:

- **1.**: Open your preferred text editor and create a file named "Dockerfile," with a capital D and without specifying an extension;
- **2.**: See below for some of the commands used in a Dockerfile:
  - **I** - ADD;
  - **II** - COPY;
  - **III** - ENV;
  - **IV** - EXPOSE;
  - **V** - FROM;
  - **VI** - LABEL;
  - **VII** - STOPSIGNAL;
  - **VIII** - USER;
  - **IX** - VOLUME;
  - **X** - WORDIR;
  - **XI** - ONBUILD;
  - **XII** - CMD.

### FROM

The **FROM** instruction initializes a new build stage and sets the base image for subsequent instructions. In short, **FROM** defines the image to be built. To know all the arguments supported by this command, check the documentation.

```Dockerfile
FROM debian
```

### RUN

The **RUN** instruction has two usage forms:

```Dockerfile
# (considering execution in shell)
RUN <command> 

# (considering an executable)
RUN ["executable", "param1", "param2"] 
```

The **RUN** instruction executes any shell command in a new layer on top of the image, committing it at the end of execution. Note that it specifies that the execution occurs in layers (Layers), so it's important not to use multiple **RUN** commands in the same Dockerfile, as this could result in the image becoming too heavy and full of layers. The more layers, the more memory used. Remember that you can nest multiple commands within a single **RUN** instruction by adding the logical operator **&&**.

### CMD

The **CMD** instruction can be executed in three ways:

```Dockerfile
# (considering an executable)
CMD ["executable","param1","param2"]

# (with default parameters for ENTRYPOINT)
CMD ["param1","param2"] 

# (considering execution in shell)
CMD command param1 param2 
```

It's important to note that there should only be a single **CMD** instruction in an executable; if there are more than one, only the last instruction will be performed.

The main purpose of the **CMD** instruction is to provide default commands for a running container. These default parameters can be an executable, an entrypoint, among others.

### LABEL

The **LABEL** instruction adds metadata to an image. For example, who maintains that image, the email address or website, the version, among other things. Usage forms:

```Dockerfile
# Definition
LABEL <key>=<value> <key>=<value> <key>=<value>

# Example 1
LABEL "wesleyjw.github.io"="Maintainer"
LABEL version="1.0"

# Example 2
LABEL email="contact@gmail.com" description="This text illustrates 
```

### EXPOSE

The **EXPOSE** instruction informs Docker that the container is listening on a specific network port at runtime. By default, this happens via the TCP protocol, but you can change it to UDP. This instruction is widely used for communication between containers.

An important note is that this instruction is not the same as port sharing via the **-p** instruction. Usage:

```Dockerfile
# Default

 TCP
EXPOSE 80

# For UDP
EXPOSE 80/udp
```

### ENV 

The **ENV** instruction defines a set of environment variables. These can be employed in subsequent build process executions.

```Dockerfile
ENV My_App=app.py
```

### ADD

The **ADD** instruction copies files, directories, or files (remote, URL, .tar) from a source [src] and adds them to the image's filesystem at a path [dest]. Usage example:

```Dockerfile
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

### COPY

The **COPY** instruction copies files or directories from a source [src] and adds them to the image's filesystem at a path [dest]. Usage example:

```Dockerfile
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

### ENTRYPOINT

The **ENTRYPOINT** instruction specifies the command that will be executed when the container starts. If the ENTRYPOINT is not specified (default entrypoint), the default is used: /bin/sh -c.  

Refer to the documentation for advantages and disadvantages of using entrypoint. Usage example:

```Dockerfile
# As an executable
ENTRYPOINT ["executable", "param1", "param2"]

# As a shell command
ENTRYPOINT command param1 param2
```

### VOLUME

The **VOLUME** instruction creates a mount point with a specific name and marks it as containing externally mounted volumes from the native host or other containers. Usage example:

```Dockerfile
VOLUME ["/data"]
```

### WORKDIR

The **WORKDIR** instruction sets a working directory for any **RUN**, **CMD**, **COPY**, and **ADD** instructions that follow it in the Dockerfile. If the working directory is not defined, it will be created automatically. **WORKDIR** is simply the root directory of the container.

```Dockerfile
WORKDIR /app
```

### Creating a Dockerfile

Let's create a **Dockerfile** to work with Jupyter in our data science environment to solidify the knowledge acquired so far. Insert the commands below into the file you created in your editor with the name Dockerfile.

```Dockerfile
FROM ubuntu:xenial

LABEL maintainer="PdD Wesley Lima"

RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    build-essential \
    byobu \
    curl \
    git-core \
    htop \
    pkg-config \
    python3-dev \
    python-pip \
    python-setuptools \
    python-virtualenv \
    unzip \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

ENV PATH /opt/conda/bin:$PATH

EXPOSE 8888 

#Setup File System
RUN mkdir ds
ENV HOME=/ds
ENV SHELL=/bin/bash
WORKDIR /ds

CMD ["jupyter", "notebook","--ip=0.0.0.0","--allow-root", "--no-browser"]
```

The first specification in the **Dockerfile** is the image we will use to create the environment, with the **FROM** tag. Next, we use the **LABEL** tag to define the person who created the image. Then, with the **RUN** tag, we execute various commands in the container shell, including system updates, installation of various libraries and development tools such as git and python, among others. In the next **RUN**, the Anaconda framework is downloaded and installed. With the **ENV** tag, an environment variable is defined for Anaconda execution, and with **EXPOSE**, the port that will be open is defined. Another **RUN** is executed to create the *ds* folder, followed by two environment variables, one to point the *HOME* directory to the created *ds* folder and another to define the *SHELL* as */bin/bash*. Finally, with the **WORDIR** tag, the container's working directory is defined as the *ds* folder. The last **CMD** tag indicates that after the container is created and everything is installed, a command will be executed in the terminal as defined: run the jupyter-notebook with the parameters of the defined IP at 0.0.0.0, as root, and indicating not to open the container's browser.

### Creating an Image from a Dockerfile

To build our image from a Dockerfile, we only need to execute the *build* command after the *docker* instruction. After the *build* command, we have the **-t** flag to call the container terminal, followed by the name of the image along with the tag specifying the version. The period at the end of the command indicates that the Dockerfile is in the same location (folder) where the terminal is executing. If the Dockerfile is in a different directory, specify the destination path (/data/images).

```Dockerfile
#command definition
docker build -t ImageName:TAGname .

#example
docker build -d -t jupyter-server .

#check the new image
docker images

#check the jupyter access token
docker logs containerID
```

To open the Jupyter notebook, open your browser and navigate to the container's address "localhost:8888". A login page will open; to access it, you must enter your access token. Retrieve it via the container log output. Look for the link containing the information "token=yr4cbyr983yre98ydry4bcyr74ybc78r48ryf" and paste it into the Jupyter login page. Your environment is ready.

---

## More about Containers

### Linking

You already know that to communicate between containers, you simply need to share ports via the **-p** flag, but there's another even more secure way. Container linking allows for secure and efficient sharing. Container linking enables multiple containers to communicate with each other. To link containers, simply use the **--link** flag. Let's create a step-by-step guide for you to perform this procedure. All the steps outlined have already been taught here; pay attention only to the last part.

```Dockerfile
#instantiate a container 
docker run --name=jenkinsa -d jenkins

#linking two containers
docker run --name=rec --link=jenkinsa:alias-scr -it ubuntu:latest /bin/bash
```
---
## Docker Compose

Imagine a large application with dozens of containers needed to execute all its functionalities. Starting all the containers and configuring each one is a tiresome and very slow task. To avoid this waste of time, Docker developed an orchestrator to organize this orchestra (containers) and make it work in synchrony like one of the typical Italian orchestras. Therefore, Docker Compose is nothing more than an orchestrator and its function is to start all the containers, as well as make all the communications and configurations required by the application, all in just one file, named *docker-compose* with the extension *.yml*. Docker-compose is a separate program, you must install it first on your machine, and it has its own commands.

### Docker-compose File

Let's get to know a docker-compose file:

```Dockerfile
version: "3.8"

services:
  jupyter-service: 
    build: 
      context: ./jupyter_server
      dockerfile: Dockerfile
    container_name: jupyter-datascience
    restart: always
    environment: 
      - JUPYTER_TOKEN=password
    volumes:
      - /home/wesley/DSEnvironment/jupyter_vol:/home/work
    ports:
      - "8888:8888"
      
  rstudio-service:
    build: 
      context: ./rstudio_server
      dockerfile: Dockerfile
    container_name: rstudio-datascience
    environment:
      - PASSWORD=password
    ports: 
      - "8787:8787"
    volumes:
      - /home/wesley/DSEnvironment/rstudio_vol:/home/rstudio

  postgresDB:
    image: postgres
    container_name: pg_container
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
      POSTGRES_DB: postgres
    ports:
      - "15432:5432"
    volumes:
      - /home/wesley/DSEnvironment/postgres_vol:/var/lib/postgresql/data
    networks:
      - postgresDB-network

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin4_container
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: email@gmail.com
      PGADMIN_DEFAULT_PASSWORD: root
    ports:
      - "5050:80"
    depends_on:
      - postgresDB
    networks:
      - postgresDB-network

  mongo:
    image

: mongo
    container_name: mongo_container
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    volumes:
      - /home/wesley/DSEnvironment/mongodb_vol:/ect/mongo

  mongo-express:
    image: mongo-express
    container_name: express_container
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
      ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/ 

networks:
  postgresDB-network:
    driver: bridge   
```

The first instruction that should be in the docker-compose.yml file is the version of docker-compose you are using, identified with the **version: "3.8"** tag.

The next tag informs the services that will be started by docker-compose. Using the **services** tag, note that the indentation forms a block of information. Thus, we have 6 services started with this file: jupyter-service, rstudio-service, postgresDB, pgadmin, mongo, and mongo-express.

After the **services** tag, there are two different ways to inform the image to be used in the container. The first two ways allow you to call an image from a Dockerfile which has its own configurations. To call an image from a Dockerfile in docker-compose, first use the **build** tag, then specify the path with the **context** tag, and finally specify the name of the file composing the Dockerfile with the **dockerfile** tag.

The next tags provide some additional configurations for our compose. For example, if you do not inform with the **container_name** tag, the container name will be the same as the service. The **restart** tag with the *always* instruction informs that the container will be restarted whenever it goes down. The **environment** tag specifies the environment variables; each service can have one or more environment variables. The **volumes** tag identifies the directory path to be shared between the host and the container. Finally, the **ports** tag releases access ports between the host and container.

Some containers still have additional tags. The **depends_on** tag informs that for the pgadmin service to be executed, the postgresDB service needs to be up, which makes total sense since we need the postgres database to use pgadmin. The **network** tag creates an access network, which can be used by containers sharing the same network.

---
## Docker Hub

Docker Hub serves as a host for Docker images. Here, you can access all available images, including official and unofficial ones (images created by third parties). Therefore, it's possible to pull ready-to-use images. However, depending on the service and workgroup, it's much more practical to make your customized image available on Docker Hub and use it from anywhere without needing any Dockerfile.

To upload your image to Docker Hub, you first need to register and create an account on the Docker Hub website. With your Docker file ready, build it specifying the name tag: userlorgin/image_name:version_name.

```Dockerfile
docker build -t wesleyjw/rstudio-serve:1.0 .
```
If you have already created the image without this specification, you can modify the image's tag name with the command below:

```Dockerfile
docker tag  rstudio-service wesleyjw/rstudio-serve:1.0
```

After creating the tag for your image, let's *push* it to Docker Hub with the commands below:

- 1. Docker login

Log in to the Docker client, if you haven't already done so:

```bash
docker login -u usernmae -p password
```
- 2. Docker image push

```bash
docker image push wesleyjw/rstudio-serve:1.0
```

Now, simply open your Docker Hub and check your image.

## Restore a dataset in postgresDB

```console
 sudo docker exec -i pg_container pg_restore --verbose --clean --no-acl --no-owner -h localhost -U postgres -d dvdrentail < /home/wesley/Downloads/dvrental/dvdrental.tar
```