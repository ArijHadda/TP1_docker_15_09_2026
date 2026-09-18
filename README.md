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


##Exercice 5:

$ docker build -t tp1-app .
[+] Building 55.9s (10/10) FINISHED                          docker:desktop-linux
 => [internal] load build definition from Dockerfile                         0.0s
 => => transferring dockerfile: 200B                                         0.0s
 => [internal] load metadata for docker.io/library/python:3.13               1.4s
 => [internal] load .dockerignore                                            0.0s
 => => transferring context: 2B                                              0.0s
 => [1/5] FROM docker.io/library/python:3.13@sha256:6faba2c56370992b0456e1  50.1s
 => => resolve docker.io/library/python:3.13@sha256:6faba2c56370992b0456e11  0.0s
 => => sha256:7af818fe6364cc23e3187871665225f2ed1ffd6f965d90898 250B / 250B  0.1s
 => => sha256:c5b14f510815b7cd08ec1fcfa5a5222e352011816f1 27.66MB / 27.66MB  7.5s
 => => sha256:1599fa592074badc651117d15e0d7cc070b21d3dd9b65 6.09MB / 6.09MB  7.4s
 => => sha256:44fed46b68cf907ddf6afb6bc4211842f016a087 236.34MB / 236.34MB  44.5s
 => => sha256:cbc19164244e861d91ebd80a17e2c78c5be43a8059 67.80MB / 67.80MB  28.1s
 => => sha256:00f78834a2fef03250be89a7741ff39d0e6bbd86029 25.64MB / 25.64MB  7.0s
 => => sha256:27ee9a8250487842a26b1ffa1215982ba9ae27010b 49.34MB / 49.34MB  13.5s
 => => extracting sha256:27ee9a8250487842a26b1ffa1215982ba9ae27010bce1997d5  1.2s
 => => extracting sha256:00f78834a2fef03250be89a7741ff39d0e6bbd860298ea129a  0.5s
 => => extracting sha256:cbc19164244e861d91ebd80a17e2c78c5be43a8059a32ab6fc  1.7s
 => => extracting sha256:44fed46b68cf907ddf6afb6bc4211842f016a0876b02fc2791  4.5s
 => => extracting sha256:1599fa592074badc651117d15e0d7cc070b21d3dd9b658d5a3  0.4s
 => => extracting sha256:c5b14f510815b7cd08ec1fcfa5a5222e352011816f10ad254e  0.5s
 => => extracting sha256:7af818fe6364cc23e3187871665225f2ed1ffd6f965d908985  0.0s
 => [internal] load build context                                            0.0s
 => => transferring context: 78B                                             0.0s
 => [2/5] WORKDIR /TP1                                                       0.3s
 => [3/5] COPY requirements.txt .                                            0.0s
 => [4/5] RUN pip install --no-cache-dir -r requirements.txt                 3.0s
 => [5/5] COPY app.py .                                                      0.0s
 => exporting to image                                                       0.9s
 => => exporting layers                                                      0.6s
 => => exporting manifest sha256:bbc67911c2fd48afcab02081441020fe36b9327bc0  0.0s
 => => exporting config sha256:0398f27d44f5320e3ef066ccaabdbe544052072a7f47  0.0s
 => => exporting attestation manifest sha256:0a07f6e1545950177c5976009c4020  0.0s
 => => exporting manifest list sha256:dae28ed4b63d2d8b806d4baf64a1841027e03  0.0s
 => => naming to docker.io/library/tp1-app:latest                            0.0s
 => => unpacking to docker.io/library/tp1-app:latest                         0.2s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/jzc040891wvm52xumpliffuch

$ docker images
                                                              i Info →   U  In Use
IMAGE            ID             DISK USAGE   CONTENT SIZE   EXTRA
nginx:latest     05b8cb60c354        253MB         69.2MB        
tp1-app:latest   dae28ed4b63d       1.62GB          418MB        

$ docker run -d -p 8080:8080 --name tp1-container tp1-app
c782481dac82ec84d813a0b0b3d5a666f44cce864e77194f9a6391b0556feef0

$ docker ps
CONTAINER ID   IMAGE     COMMAND           CREATED          STATUS          PORTS                                         NAMES
c782481dac82   tp1-app   "python app.py"   36 seconds ago   Up 35 seconds   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   tp1-container

>pour tester sur le navigateur: http://localhost:8080/


## Exercice 6:

$ docker compose up --build
$ docker compose logs app
app-1  | Connexion à MongoDB réussie !
app-1  |  * Serving Flask app 'app'
app-1  |  * Debug mode: off
app-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
app-1  |  * Running on all addresses (0.0.0.0)
app-1  |  * Running on http://127.0.0.1:8080
app-1  |  * Running on http://172.18.0.2:8080
