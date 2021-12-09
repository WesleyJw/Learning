# Trabalhando com o Docker

Autor: PhD. Wesley Lima

## O que é Docker?

Na principal definição do termo, temos que docker é uma plataforma aberta para o desenvolvimento, entrega e execução de aplicações. Dcoker nada mais é que um gestor de serviços via containers. A principal ideia por trás do docker, para desenvolvedores, é tornar fácil o desenvolvimento de aplicações, dentro de containers que podem ser utilizados em qualquer lugar.  

Para instalação do docker veja este [link](https://www.tutorialspoint.com/docker/installing_docker_on_linux.htm).

-------------------------------------------------------------------------------------------------------------------------------------------

## Comandos Iniciais

Para saber a versão do docker execute:

```bash
docker version
```

A pavra reservada *docker* informa ao programa Docker no sistema operacional que alguma coisa precisa ser executada. 

Ou para consultar informações gerais:

```bash
docker info
```

É importante fazer login no docker para poder baixar imagens em sua máquina.

```bash
docker login -u="loginName" -p="password"
```


-------------------------------------------------------------------------------------------------------------------------------------------

## Imagens docker

É importante saber que tudo em docker é baseado em imagens. Mas o que seria uma imagem docker? Bem, uma imagem nada mais é do que uma combinação de arquivos de sistemas (conhecido comumente pelo nome file system) e parâmetros. Veja como criamos uma imagem docker: 

```bash
docker run hello-worl
```

- O comando **run** informa que queremos criar uma instância de uma imagem, que é chamada de container.
- O termo **hello-world** é a imagem na qual o container é criado.

No próximo tópico vamos definir o que é um container para suprimir suas dúvidas. É comum elas persistirem até aqui.

A execução do comando acima em seu terminal retornou uma série de *logs* e printou o texto "hello-world", depois sua linha do terminal retornou. Essa imagem docker foi criada com este propósito mesmo. 

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

O segundo bloco de informações é o *output* do primiero comando, veja que nosso progrma docker não encontrou a imagem localmente, fez o *Pull* (download) da imagem do Docker Hub e intanciou um novo container a partir da imagem baixada. No final ele retorunou a linha  de comando do terminal do sistema que está em execução dentro do container.

- O comando **-it** é empregado para informar que queremos executar no modo interativo.
- O termo **/bin/bash** é utilizado para executar o bash shell (terminal) quando o Debian está executando. (debian is up and running).


### Listandos imagens 

É importante saber que o download de uma imagem só acontece na primeira vez que você executa esta imagem, posteriormente o docker verificar se a imagem já existe na suma máquina. Assim, ele utiliza esta imagem local para instanciar os próximos containers. Para verificar as imagens disponíveis no seu sistema (*host*) execute o seguinte comando:   

```console
docker images

REPOSITORY                                      TAG                  IMAGE ID       CREATED         SIZE
wesleyjw/datascienceimg                         latest               093210c05050   2 days ago      3.99GB
debian                                          latest               05d2318291e3   7 days ago      124MB
bash                                            latest               6a03c8e7e2be   2 weeks ago     12.9MB
mongo                                           latest               4253856b2570   3 weeks ago     701MB
ubuntu                                          18.04                5a214d77f5d7   2 months ago    63.1MB
```
Verificando o *output* do comando encontramos cinco imagens na nossa máquina. Podemos verificar os atributos de cada imagem:

- **REPOSITORY**: Representa o nome da imagem.
- **TAG**: É uma parâmetro de marcação lógica da imagem;
- **IMAGE ID**: É usado como identificador único da imagem;
- **CREATED**: Identifica o número de dias desde a criação da imagem;
- **SIZE**: O tamanho da imagem.

### Removendo imagens docker

Para remover imagens docker da  sua máquina vamos utilizar o seguinte comando: 

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
--------------------------------------------------------------------------------------------------------------------

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

Para voltar para a linda de comando (shell do seu sistema operacional) pressione Crtl + p e em seguida Crtl + q. Você pode sair também pressionando Crtl + d ou digitando o comando *exit*, só que neste caso o container é parado (desligado). Utilize a primeira combinação para continuarmos com o exemplo, se já matou o container, não tem problemas execute ele novamente com o comando anterior.  

Agora vamos verificar se o container está em execução.

```console
docker ps
```

Isto retorna o seguinte *output*:


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

Outro comando útil é o *history* para conhecer-mos o histórico de uso do container:

```console
docker history <ContainerID>

docker history acce8600f36c
```

- **ContainerID**: ID do continer.

--------------------------------------------------------------------------------------------------------------------

## Trabalhando com containers

### Docker start

Como inicializar um container:

```console
docker start <ContainerID or ContainerName>

docker start wesleytest ls
```
- O comando **ls** lista os arquivos e pastas de um diretório,  neste caso listará tudo na raiz do container. 

### Docker top

Com este comando é possível verificar os processos de maior recursos dentro do container:

```console
docker top <ContainerID>

docker top  2270220a21e3
```

*output*:

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

--------------------------------------------------------------------------------------------------------------------

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

Quando não especificamos uma tag para versão da imagem escolhida o docker sempre busca a versão *latest*. Com o comando a seguir podemos criar um container com a imagem ubuntu com a tag de versão.


```console
docker run ubuntu:18.04 cat /etc/issue
```
- **cat /etc/issue**  mostra a versão do ubuntu no final da execução.

### Docker -d

Criar um container e executar em bacground. 

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

--------------------------------------------------------------------------------------------------------------------

## Arquitetura de um container

Para entendermos a arquitetura de funcionamento do docker vamos primeiro entender com funciona a virtualização tradicional via máquinas virtuais. Inicialmente todo processo de virtualização era realizado em um servidor (máquina física), dentro de um host (sistema operacional), controlado por um Hypervisor [VMWare ou Hyper /v em Windows] (responsável por gerenciar a virtualização), em seguida vem o novo sistema operacional a ser utilizado e por fim as aplicações. Algumas caraterísticas deste tipo de virtualização é que a memória reservada geralmente é fixa, mesmo que o sistema não utilize tudo ele possui aquela reserva, por outro lado se a plicação precisa de mais memória não será disponível imediatamente. Não é preciso mais explicações para afirmar que este modo existe bastante recursos do servidor.   

![Imagem com a arquitetura de um ambiente de virtualização via máquinas virtuais](./images/virtualization.jpg)

A nova forma de virtualização via containers permite a partir de um servidor com um sistema operacional gerar grupos virtuais via engine doker diretamente com a aplicação. Isto permite muito mais escalabilidade, econômia de recursos, agilidade entre outras cosias.

![Imagem com a arquitetura de um ambiente de virtualização via docker](./images/various_layers.jpg)



