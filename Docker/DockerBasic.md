# Trabalhando com o Docker

Autor: PhD. Wesley Lima

## O que é Docker?

Na principal definição do termo, temos que docker é uma plataforma aberta para o desenvolvimento, entrega e execução de aplicações. Dcoker nada mais é que um gestor de serviços via containers. A principal ideia por trás do docker, para desenvolvedores, é tornar fácil o desenvolvimento de aplicações, dentro de containers que podem ser utilizados em qualquer lugar.

Para instalação do docker veja este [link](https://www.tutorialspoint.com/docker/installing_docker_on_linux.htm).

---

### Comandos Iniciais

Para saber a versão do docker execute:

```bash
docker version
```

A pavra reservada _docker_ informa ao programa Docker no sistema operacional que alguma coisa precisa ser executada.

Ou para consultar informações gerais:

```bash
docker info
```

### Configuração

É importante fazer login no docker para poder baixar imagens em sua máquina.

```bash
docker login -u="loginName" -p="password"
```

Se por acaso você precisar parar o Docker (docker daemon process), utilize o seguinte comando:

```bash
service docker stop
```

Para iniciar o serviço docker novamente utilize,

```bash
service docker start
```

---

## Imagens docker

É importante saber que tudo em docker é baseado em imagens. Mas o que seria uma imagem docker? Bem, uma imagem nada mais é do que uma combinação de arquivos de sistemas (conhecido comumente pelo nome file system) e parâmetros. Veja como criamos uma imagem docker:

```bash
docker run hello-worl
```

- O comando **run** informa que queremos criar uma instância de uma imagem, que é chamada de container.
- O termo **hello-world** é a imagem na qual o container é criado.

No próximo tópico vamos definir o que é um container para suprimir suas dúvidas. É comum elas persistirem até aqui.

A execução do comando acima em seu terminal retornou uma série de _logs_ e printou o texto "hello-world", depois sua linha do terminal retornou. Essa imagem docker foi criada com este propósito mesmo.

Agora criando um novo container, vamos vê como podemos utilizar a imagem do Debian disponível no Dcoker Hub para rodarmos o debian na nossa máquina local. Vamos executar o seguinte comando:

```console

docker run -it debian /bin/bash

Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
5e0b432e8ba9: Pull complete
Digest: sha256:45ee40a844048c2f6d0105899c1a17733530b56d481612608aab5e2e4048570b
Status: Downloaded newer image for debian:latest
root@f365cf13cb79:/#
```

O segundo bloco de informações é o _output_ do primiero comando, veja que nosso progrma docker não encontrou a imagem localmente, fez o _Pull_ (download) da imagem do Docker Hub e intanciou um novo container a partir da imagem baixada. No final ele retorunou a linha de comando do terminal do sistema que está em execução dentro do container.

- O comando **-it** é empregado para informar que queremos executar no modo interativo.
- O termo **/bin/bash** é utilizado para executar o bash shell (terminal) quando o Debian está executando. (debian is up and running).

### Listandos imagens

É importante saber que o download de uma imagem só acontece na primeira vez que você executa esta imagem, posteriormente o docker verificar se a imagem já existe na suma máquina. Assim, ele utiliza esta imagem local para instanciar os próximos containers. Para verificar as imagens disponíveis no seu sistema (_host_) execute o seguinte comando:

```console
docker images

REPOSITORY                                      TAG                  IMAGE ID       CREATED         SIZE
wesleyjw/datascienceimg                         latest               093210c05050   2 days ago      3.99GB
debian                                          latest               05d2318291e3   7 days ago      124MB
bash                                            latest               6a03c8e7e2be   2 weeks ago     12.9MB
mongo                                           latest               4253856b2570   3 weeks ago     701MB
ubuntu                                          18.04                5a214d77f5d7   2 months ago    63.1MB
```

Verificando o _output_ do comando encontramos cinco imagens na nossa máquina. Podemos verificar os atributos de cada imagem:

- **REPOSITORY**: Representa o nome da imagem.
- **TAG**: É uma parâmetro de marcação lógica da imagem;
- **IMAGE ID**: É usado como identificador único da imagem;
- **CREATED**: Identifica o número de dias desde a criação da imagem;
- **SIZE**: O tamanho da imagem.

### Removendo imagens docker

Para remover imagens docker da sua máquina vamos utilizar o seguinte comando:

```console
docker rmi <ImageName or ImageId>

docker rmi 5a214d77f5d7
```

- **ImageName ou Repository**: Nome da imagem;
- **ImageId**: Id da imagem;

Para retornar apenas os Id's da imagens disponíveis execute:

```console
docker images -q
```

- **-q**: Informa ao Docker para retornar apenas os Id's das imagens.

Se você deseja saber mais informações sobre uma imagem específica utilize o comando:

```console
docker inspect <Repository>

docker inspect mongo
```

---

## Docker container

O que é um container docker? Por definição container é um ambiente isolado, disposto em um servidor, o qual dividide um host único (sistema operacional) de controle. Informalmente podemos afirmar que um container é uma parte de memória isolada, onde podemos executar sistemas operacionais, tudo isso controlado pelo docker engine dentro do seu sistema operacional (host).

Para melhroar nosso entendimento considere pensar a seguinte situação: Imagine que seu sistema operacional é um navio cargueiro e você possui uma carga de produtos de diversas naturezas: material de limpeza, produtos de tecnologia, produtos de alimentação que precisão de refrigeração, itens hospitalares, entre outros. Você já percebeu que não é possível transportar tudo isso sem organizar os produtos por tipos e forma de transporte. Já que estamos falando com capitão do navio providencie diversos containers ideias para cada tipo de produto.

Voltando para nossa área agora veja o desenvolvimento de um software que precisa, para funcionar corretamento, de um banco de dados SQL (Postgress), seu administrador do banco (pgAdmin4), um banco de dados NoSQL (mongoDB) juntamente com seu administrador, um framework de desenvolvimento frontend (React) outro para o desenvolvimento backend (Django), mais um servidor para análise de dados e machine learning (jupyter notebook com anaconda). Todas estas ferramentas possuem suas dependências, logo conflitos podem surgir na instalação e configuração de cada uma, quem nunca perdeu dias preparando ambientes de desenvolvimento? Outro grande problema surge quando você precisa compartilhar seu projeto com colegas de trabalho, quem nunca usou o jargão na minha máquina funciona que atire a primeira pedra.

O docker com sua metodologia de criação de container surge para solucionar esta problemática. Com ele é possível instanciar containers com cada uma das aplicações a partir de imagens disponíveis. Então, agora você pode criar os containers com as imagens específicas do seu projeto sem interfêrencias de dependências e compartilhar os comandos utilizados com seus colegas garantindo que estes terão ambientes com as mesmas configurações que você.

Nas boas práticas de uso dos containers, temos que cada container seja utilizado para um único serviço e função, ou seja, se você precisa de um banco de dados Postgress, instancie um container com apenas esta função. Desta forma temos a garantia de que se um container cair (acontecer qualquer problema com ele), apenas a funcinalidade dele vai deixar de operar. Nossa aplicação continua de pé, sendo bem mais rápido e simples, instanciar outro container com a aquela funcionalidade.

### Listando containers

Inicialmente vamos instanciar um container em modo interativo com o comando a seguir:

```console
docker run -it debian /bin/bash
```

Para voltar para a linda de comando (shell do seu sistema operacional) pressione Crtl + p e em seguida Crtl + q. Você pode sair também pressionando Crtl + d ou digitando o comando _exit_, só que neste caso o container é parado (desligado). Utilize a primeira combinação para continuarmos com o exemplo, se já matou o container, não tem problemas execute ele novamente com o comando anterior.

Agora vamos verificar se o container está em execução.

```console
docker ps
```

Isto retorna o seguinte _output_:

```console
name@Inspiron-5448:~$ docker ps
CONTAINER ID   IMAGE                    COMMAND        CREATED          STATUS         PORTS      NAMES
acce8600f36c   debian                   "bash"         10 seconds ago   Up 8 seconds              jolly_zhukovsky
3deb5e8253e1   portainer/portainer-ce   "/portainer"   8 months ago     Up 10 hours    8000:9000  portainer
```

Agora vamos listar todos os containers do sistema, incluindo containers inativos e parados:

```console
docker ps -a
```

- **-a** indica ao comando docker ps para listar todos os containers do sistema operacional.

Outro comando útil é o _history_ para conhecer-mos o histórico de uso do container:

```console
docker history <ContainerID>

docker history acce8600f36c
```

- **ContainerID**: ID do continer.

---

## Trabalhando com containers

### Docker start

Como inicializar um container:

```console
docker start <ContainerID or ContainerName>

docker start wesleytest ls
```

- O comando **ls** lista os arquivos e pastas de um diretório, neste caso listará tudo na raiz do container.

### Docker top

Com este comando é possível verificar os processos de maior recursos dentro do container:

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

Usado para parar um container em execução.

```console
docker stop <ContainerID>

docker stop  2270220a21e3

docker stop <ContainerName>

docker stop debian
```

### Docker rm

Removendo um container

```console
docker rm <ContainerID>

docker rm <ContainerName>

docker rm debian
```

### Docker stats

Verificando as estatísticas de um container.

```console
docker stats <ContainerID>

docker stats <ContainerName>

docker stats debian
```

### Docker logs

Para verificar os logs de um container. Este comando é importante para quando você precisa verificar informações de configurações, de senhas para outras aplicações dependentes.

```console

docker logs <ContainerName> or <ContainerID>

docker logs c959f10607d1

docker logs -f c959f10607d1
```

- **-f**: verificar logs iterativos.

### Docker prune

Remover todos os container inativos

```console
docker prune
```

Seguindo a mesma lógica de comandos temos também: docker attach - para entrar em um container em execução, docker pause - para pausar a execução de um container ativo, docker unpause - para despausar, dcoker kill para matar um container.

### O ciclo de vida de um container

![Imagem diagrama do ciclo de vida de um container](./images/container_lifecycle.jpg)

---

## Trabalhando ainda mais com containers

### Docker --rm

Instaciar um container removendo outros containers de mesma imagem que já existe.

```console
docker run --rm alpine echo "Hello world"
```

- **run**: sempre criar novos containers
- **--rm**: este comando sempre remove um container já existente para execução do segundo.

### Docker exec

Executar comandos em um container já em execução:

```console
docker run exec <ContainerID or ContainerName>  <linuxcomand>

docker run exec wesleytest ls
```

### Docker tag

Quando não especificamos uma tag para versão da imagem escolhida o docker sempre busca a versão _latest_. Com o comando a seguir podemos criar um container com a imagem ubuntu com a tag de versão.

```console
docker run ubuntu:18.04 cat /etc/issue
```

- **cat /etc/issue** mostra a versão do ubuntu no final da execução.

### Docker -d

Criar um container e executar em background.

```console
docker run -d alpine sleep 20
```

- **-d**: executar o container em bacground, ou seja deixa o container rodando com o programa, mas a linha do console volta para o usuario;
- **sleep**: deixar o programa dormindo pelo tempo determinado.

### Juntando diversos comandos docker

Instanciar um container nomea-lo e executar em bacground juntamento com um comando de execução:

```console
docker run -d --name wesleytest alpine sleep 20
```

- **--name**: Nomear o container.

---

## Arquitetura de um container

Para entendermos a arquitetura de funcionamento do docker vamos primeiro entender com funciona a virtualização tradicional via máquinas virtuais. Inicialmente todo processo de virtualização era realizado em um servidor (máquina física), dentro de um host (sistema operacional), controlado por um Hypervisor [VMWare ou Hyper /v em Windows] (responsável por gerenciar a virtualização), em seguida vem o novo sistema operacional a ser utilizado e por fim as aplicações. Algumas caraterísticas deste tipo de virtualização é que a memória reservada geralmente é fixa, mesmo que o sistema não utilize tudo ele possui aquela reserva, por outro lado se a plicação precisa de mais memória não será disponível imediatamente. Não é preciso mais explicações para afirmar que este modo existe bastante recursos do servidor.

![Imagem com a arquitetura de um ambiente de virtualização via máquinas virtuais](./images/virtualization.jpg)

A nova forma de virtualização via containers permite a partir de um servidor com um sistema operacional gerar grupos virtuais via engine doker diretamente com a aplicação. Isto permite muito mais escalabilidade, econômia de recursos, agilidade entre outras cosias.

![Imagem com a arquitetura de um ambiente de virtualização via docker](./images/various_layers.jpg)

---

## Trabalhando com Volumes em Containers

### Docker Volumes

Volume docker são arquivos de sistemas montados no container docker para preservar dados gerados a partir de um container em execução. Estes volumes (arquivos de sistema) são salvos no host, independente do ciclo de vida do container. Desta forma, se durante a execução de um serviço, dentro de um container, dados forem produzidos e salvos, sendo que estes dados precisam persistir mesmo que o container seja destruído, pormeio de volumes é possível compartilhar estes dados do container com o host. Se você indicar o volume compartilhado **"VOL.host:VOL.container"** toda vez que o container executar ele consegue salvar dados neste volume, que persistirá no host e toda vez em que o container subir, ele pode lê os dados salvos e fazer qualquer tipo de atualização. Este processo pode acontecer infinitas vezes.

Como é possível faer o compartilhamento de volumes entre host e container? Vamos instanciar um container e especificar um volume para compartilhamento entre host e container.

```console
docker container run -d --name linux -v "<dir-host:dir-container>" image

#1. exemplo
docker container run -d --name linux -v "/data/server:tmp" ubuntu:18.04

#2. exemplo
docker container run -d --name linux -v "home/user/data:/tmp" ubuntu:18.04 sleep 2000
```

- **-d**: executar o container em background. (lbera a linha do console);
- **--name**: Nome do container;
- **-v**: Especifíca o volume a ser compartilhado;
- **dir-host**: Caminho até o diretório que será compartilhado no lado do host
- **dir-container**: Caminho até o diretório que será compartilhado no lado do container
- **sleep**: Comando executado dentro do container

Outra forma de criar um volume é utilizando o comando _pwd_ para especificar parte de um caminho. Ficnado desta forma o código:

```console
$ pwd

docker container run -d --name linux -v "$PWD/data:/tmp" ubuntu:18.04 sleep 2000
```

---

## Variáveis de ambiente

```console

docker container run --name linux2 -e vartest="variavel de ambiente" ubuntu env

```

---

## Gestão de Portas

```console
docker container run -d --name <containername> -p <PORT.host:PORT.container> image

docker container run -d --name webserver -p 8080:80 nginx
```

- **-p**: Indica o compartilhamento entre portas;
- **PORT.host**: Indica porta do host que será aberta (compartilhada);
- **PORT.container**: Indica porta do container que será aberta (compartilhada);

---

## Dockerfile

Até aqui já aprendemos que para intanciar um container basta fazer o download de uma imagem e executar o docker run com as especificações requeridas. Você deve pensar de onde vem todas estas imagens e como saber a existência delas, não vou entrar em detalhes aqui, mas você pode consultar infinitas imagens no site chamado Docker Hub, bem como também pode subir imagens qeu você mesmo criou, bata fazer login no site.

Tudo certo até aqui? Agora você pode pensar como eu crio minhas imagens com as configurações que preciso, já que, mesmo que suba um container instale diversos programas de desenvolvimento, quando você fizer o stop do container todas estas alterações desaparecem, como persistir isso? Para você não ficar perdendo tempo tendo que fazer todas as mesmas configurações sempre que subir um container, existe o Dockerfile. Um Dockerfile é simplesmente um arquivo de texto com as instruções sobre como você quer construir sua imagem.

Vamos vê como é processo de criação de um Dockerfile:

- **1.**: Abrao editor de texto de sua preferência e crie um arquivo com nome "Dockerfile", com D em caixa alta e sem especificar uma extensão;
- **2.**: Veja abaixo alguns dos comandos utilizados em um Dockerfile:
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

A instrução **FROM** inicializa um novo estágio de construção e define a imagem base para instruções subsequentes. Resumidamente **FROM** define a imagem que será construida. Para saber todos os argumentos suportados por este comando verifique a documentação.

```Dockerfile
FROM debian
```

### RUN

A instrução **RUN** possui duas formas de uso:

```Dockerfile
#(considerando execução no shell)
RUN <command> 

#(considerando um executavel)
RUN ["executable", "param1", "param2"] 
```

A instrução **RUN** executa qualquer comando shell em uma nova camada no topo da imagem, comitando ao final da execução. Veja que ele específica que a execução ocorre em camadas (Layers), por isto é importante não utilizar diversos comando **RUN** em um mesmo arquivo Dockerfile, com risco da imagem ficar muito pesada e cheia de camadas, quanto mais camdas, mais memória utilizada. Lembre que é possível aninhar varios comandos dentro de uma única instrução **RUN** acrescentando o operador lógico **&&**.

### CMD

É possível executar a instrução **CMD** de três formas: 


```Dockerfile
#(considerando um executavel)
CMD ["executable","param1","param2"]

#(com parâmetros default para o ENTRYPOINT)
CMD ["param1","param2"] 

#(considerando execução no shell)
CMD command param1 param2 
```

É importante destacar que só deve existir uma única instrução **CMD** em um executável, havendo mais de uma apenas a última instrução será realizada.

O principal objetivo da instrução **CMD** é fornecer comandos default para a um container em execução. Estes parâmetros default podem ser um executavél, um entrypint, entre outros.

### LABEL

A instrução **LABEL** adiciona metadados a uma imagem. Por exemplo:  quem é mantenedor daquela imagem, o endereço de email ou site, a versão, entre outras coisas. Formas de usar:

```Dockerfile
#Definicao
LABEL <chave>=<valor> <chave>=<valor> <chave>=<valor>

#Exemplo 1.
LABEL "wesleyjw.github.io"="Mantenedor"
LABEL version="1.0"

#Exemplo 2.
LABEL email="contato@gmail.com" description="This text illustrates 
```

### EXPOSE

A instrução **EXPOSE** informa ao docker que o container está ouvindo (listens) em uma porta de rede específica em tempo real. Por default esta isto ocorre via protocolo TCP, mas você pode alter para UDP. Esta instrução é bastante utilizada para comunicação entre containers. 

Uma observação é que esta instrução não é a mesma coisa que o compartilhamento de portas via a instrução **-p**. Forma de usar:

```Dockerfile
#defaul TCP
EXPOSE 80

#para udp
EXPOSE 80/udp
```

### ENV 

A instrução **ENV** define um conjunto de variáveis de ambiente. Estas podem ser empregadas em execuções subsequentes processo de build.

```Dockerfile
ENV My_App=app.py
```

### ADD

A instrução **ADD** copia arquivos, diretórios ou arquivos (remotos, URL, .tar) de uma fonte [src] e adiciona para sistema de arquivos da imagem em um caminho [dest]. Exemplo de uso:

```Dockerfile
ADD [--chown=<user>:<group>] <src>... <dest>
ADD [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

### COPY

A instrução **COPY** copia arquivos ou diretórios de uma fonte [src] e adiciona para o sistema de arquivos da imagem em um caminho [dest]. Exemplo de uso:

```Dockerfile
COPY [--chown=<user>:<group>] <src>... <dest>
COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
```

### ENTRYPOINT

A instrução **ENTRYPOINT** especifica o comando que será executado quando o container inicia. Quando não é especificado o ENTRYPOINT (padrão de entrada) o default é utilizado: /bin/sh -c.  

Veja na documentação vantagens e desvantagens de utilizar entrypoint. Exemplo de uso:

```Dockerfile
#na forma de executavel
ENTRYPOINT ["executable", "param1", "param2"]

#na forma de shell
ENTRYPOINT command param1 param2
```

### VOLUME

A instrução **VOLUME** cria um ponto de montagem com nome específico e o marca como contendo volumes montados externamente do host nativo ou outros containers. Exemplo de uso:

```Dockerfile
VOLUME ["/data"]
```

### WORKDIR

A  instrução **WORKDIR**  define um diretório de trabalho para quanquer instrução **RUN**, **CMD**, **COPY** e **ADD** presentes em um Dockerfile. Se o diretório de trabalho não for definido ele será criado automaticamente. **WORkDIR** nada mais é do que o diretório raiz do container. 

```Dockerfile
WORKDIR /app
```

### Criando um Dockerfile

Vamos criar um **Dockerfile** básico para fundamentar o conhecimento adquirido até aqui. Insira os comandos abaixo no arquivo que você criou  no seu editor com o nome de Dockerfile.

```Dockerfile
FROM debian

LABEL maintener="phd.WesleyJW"

RUN apt-get update && apt-get install -y nginx

CMD ["echo", "Imagem criada."]
```

### Criando uma imagem a partir de um Dockerfile

Para construirmos a nossa imagem a partir de um Dockerfile precisamos apenas executar o comando *build* após a instrução *docker*. Após o comando *build* temos a flag **-t** para chamar o terminal do container e depois temos o nome da imagem juntamente com tag que específica a versão. O ponto no final do comando informa que o arquivo Dockerfile está na mesma origem (pasta) em que o terminal está executando. Se o Dockerfile estiver em um diretório diferente, informe o caminho de destino (/data/imagens).

```Dockerfile
#definicao do comando
docker build -t ImageName:TAGname .

#exemplo
docker build -t myimage:1.0 .

#verificar a nova imagem
docker images
```
---

## Mais sobre containers

### Link

É obvio que você já sabe que para um container se comunicar com outro basta compartilhar portas via flag **-p**, mas existe outra forma ainda mais segura. A comunicação entre containers via link permite um capartilhamento seguro e eficiente. Container link permite multiplos containers se comunicar um com outros. Para fazer o link entre containers basta utilizar a glag **--link**, vamos criar um passo a passo para você conseguir realizar este procedimento. Todos os passos seguidos já foram ensinados aqui, se ligue apenas na última parte.

```Dockerfile
#instanciar um container 
docker run --name=jenkinsa -d jenkins

#lincando dois containers
docker run --name=rec --link=jenkinsa:alias-scr -it ubuntu:latest /bin/bash
```
---
## Docker compose

Imagine uma aplicação grande, com dezenas de containers para poder executar todas as funcionalidades. Subir todos os containers e configurar cada um é uma tarefa cansativa e muito lenta. Para evitar este desperdício de tempo a docker desenvolveu um orquestrador para organizar esta orquestra (containers) e fazê-la funcionar com sincronia como uma das típcas orquestras italianas. Sendo assim, o docker compose nada mais é do que um orquestrador e tem a função de levantar todos os containers, bem como fazer todas as comunicações e configurações que a aplicação requer, tudo isso em apenas um arquivo, com o nome *docker-compose* ea extensão de marcação *.yml*. O docker-compose é um programa a parte, você deve instalar primeiro na sua máquina, bem como ele possui seu próprios comandos. 

### Arquivo Docker-compose

Vamos conhecer um arquivo docker-compose:

```docker-compose
version: "3.8"

services:
  jupyter-service: 
    image: jupyter/datascience-notebook:4.0.3
    container_name: jupyter-datascience
    restart: always
    environment: 
      - JUPYTER_TOKEN=password
    volumes:
      - ./:/home/work
    ports:
      - 8888:8888
      
  rstudio-server:
    image: wesleyjw/rstudio
      container_namer: rstudio-datascience
    environment:
      - PASSWORD-password
      - USERID=$(id -u)
      - GROUPID=$(id -g)
    ports: 
      - 8787:8787
    volumes:
      - ./:/home/rstudio

  postgresDB:
    image: postgres
    container_name: pg_container
    restart: always
    environment:
      POSTGRES_USER: root
      POSTGRES_PASSWORD: root
      POSTGRES_DB: datascience_db
    ports:
      - "5432:5432"
    volumes:
      - ./:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin4_container
    image: dpage/pgadmin4
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: root
    ports:
      - "5050:80"

  mongo:
    image: mongo
    container_name: mongo_container
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example
    volumes:
      - ./:/ect/mongo

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
```

A primeira instrução que deve conter no arquivo docker-compose.yml deve ser a versão do docker-compose que vocẽ está utilizando, você identifica isso com a tag **version**






