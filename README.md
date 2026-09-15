# TP1_docker_15_09_2026
il y aura les different exercices du TP d'Intégration et déploiement continus

##Exercice 3:

C:\Users\arijh>docker --version
Docker version 29.8.0, build 88096ef

C:\Users\arijh>docker images
                                                                                                    i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA

C:\Users\arijh>docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:5e23090353324d887c48ad5e5c56d294eab81588df9605b07d1afe895f9cc8f8
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest

C:\Users\arijh>docker images
                                                                                                    i Info →   U  In Use
IMAGE                ID             DISK USAGE   CONTENT SIZE   EXTRA
hello-world:latest   5e2309035332       25.9kB         9.49kB

C:\Users\arijh>docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/


C:\Users\arijh>docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

C:\Users\arijh>docker ps -a
CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                          PORTS     NAMES
3be1dcd59921   hello-world   "/hello"   About a minute ago   Exited (0) About a minute ago             sweet_solomon

C:\Users\arijh>docker rm 3be1dcd59921
3be1dcd59921

C:\Users\arijh>docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

C:\Users\arijh>docker rmi 5e2309035332
Untagged: hello-world:latest
Deleted: sha256:5e23090353324d887c48ad5e5c56d294eab81588df9605b07d1afe895f9cc8f8

C:\Users\arijh>docker images
                                                                                                    i Info →   U  In Use
IMAGE   ID             DISK USAGE   CONTENT SIZE   EXTRA


##Exercice 4:

C:\Users\arijh>docker pull nginx
Using default tag: latest
latest: Pulling from library/nginx
f340c1b7c1d6: Pull complete
6310eb16bf42: Pull complete
02fc02c4ab8d: Pull complete
956faab5efb3: Pull complete
a44b5c8be616: Pull complete
c12f394dea35: Pull complete
07db7bf2649b: Pull complete
25202a7045eb: Download complete
76f27c02d218: Download complete
Digest: sha256:05b8cb60c354a44ab824ea6e7dc69b46d50762cdbe728a347a5b656e6fb3d7c4
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest

C:\Users\arijh>docker images
                                                                                                    i Info →   U  In Use
IMAGE          ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:latest   05b8cb60c354        253MB         69.2MB

C:\Users\arijh>docker run -d -p 8080:80 --name mon_nginx nginx
1b75cae80db9b8bc79701eaa461e26001dba2a64709e193a6db50d9a917988fc

C:\Users\arijh>docker container ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                     NAMES
1b75cae80db9   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx

C:\Users\arijh>docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                     NAMES
1b75cae80db9   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx

C:\Users\arijh>docker stop mon_nginx
mon_nginx

C:\Users\arijh>docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

C:\Users\arijh>docker ps -a
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS                      PORTS     NAMES
1b75cae80db9   nginx     "/docker-entrypoint.…"   4 minutes ago   Exited (0) 20 seconds ago             mon_nginx

C:\Users\arijh>docker rm mon_nginx
mon_nginx

C:\Users\arijh>docker ps -a
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES

