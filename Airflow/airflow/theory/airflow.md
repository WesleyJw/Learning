# Uma Revisão sobre o Airflow

Apache Airflow é uma plataforma para desenvolvimento, agendamento e monitoramento de workflows orientados a bacth (conjunto finitio de atividades em um determinado tempo). Airflow é um framework em python que permite a construção de worflows conectando viltualmente qualquer tecnologia.

## Características de usar o Airflow

### Principais vantagens

- Implementação de completos e complexos Pipelines utilizando código Python.
- Versionamento.
- Fácil integração com outros sistemas por conta da comunidade.
- Ricas opções para trabalhar com agendamento.
    - Processamento incremental.
    - ○ Redução de custos.
- Backfilling para reprocessar dados históricos.
- Interface Web para Monitoramento e Debugging.
- Open Source e API's

### Construindo a Primeira DAG

```python
from airflow import DAG
import airflow.utils.dates
from airflow.operators.bash import BashOperator

dag = DAG(
    dag_id="first-dag",
    description="The first Ariflow Dat to test instalation",
    start_date=airflow.utils.dates.days_ago(14),
    schedule_interval="@daily"
)

task_echo_message = BashOperator(
    task_id="echo_message",
    bash_command="echo Hello World",
    dag=dag
)

task_echo_message
```

## Interface de linha de comando do Airflow

```bash
# Conectando ao container.
docker container exec -it airflow bash

# Listando os comandos disponíveis.
airflow --help

# Verificando as informações do ambiente.
airflow info

# Verificando as configurações.
airflow config list

# Verificando as conexões do ambiente.
airflow connections list

# Listando as dags disponíveis.
airflow dags list

# Listando as tasks de uma determinada dag.
airflow tasks list <dag-id>
airflow tasks list hello_world

# Testando a execução de uma determinada task. para executar na real <run>
airflow <tasks> <test> <dag_id> <task_id> <execution-date>
airflow tasks test hello_world echo_message 2021-07-01
```

## Definições 

Workloads ou Cargas de Trabalho

Uma **DAG** é composta por tarefas que podem ser de três tipos.
-  Operadores que são tarefas predefinidas que agrupadas formam a execução da DAG. 
- Sensores que é uma subclasse especial de Operadores que trabalham aguardando um evento externo acontecer.
- Taskflow que é uma função Python personalizada empacotada como uma Tarefa.

Ainda mais sobre DAGs - Core do Airflow.
- Reuni tarefas juntas.
- Especifica suas dependências e relacionamentos.
- Define como e quando serão executadas.

Declarando uma DAG.

```python
#Através de um Context manager.
with DAG("etl-db-producao") as dag:
    op = DummyOperator(task_id="task")

#Através de um construtor padrão.
my_dag = DAG("etl-db-producao")
op = DummyOperator(task_id="task", dag=my_dag)

#Através de um decorator - transforma uma função em uma dag.
@dag(start_date=days_ago(2))
def generate_dag():
    op = DummyOperator(task_id="task")
dag = generate_dag()

```

### Executando DAG's

DAG's são executadas de duas formas.
- Acionamento manual ou por API.
- Intervalo de agendamento.
    - `with DAG("etl-db-producao", schedule_interval="@daily"):`
    - `with DAG("etl-db-producao", schedule_interval="0 * * * *"):`
- Argumentos padrões
```python
default_args = {
    'start_date': datetime(2016, 1, 1),
    'owner': 'airflow'
    }
with DAG('etl-db-producao', default_args = default_args) as dag:
    op = DummyOperator(task_id='dummy')
print(op.owner)
```

### Control Flow (Fluxo de Controle de Tarefas)
Tarefas têm dependências entre elas
- Extração será executada, em seguida será criada uma bifurcação onde ele pode executar a tarefa de transfomação ou de carga `extracao >> [transformacao, carga]`
- A tarefa de notificação tem dependência da tarefa de carga. `carga << notificacao`
Podemos definir as dependências através dos métodos.
- `extracao.set_downstream([transformacao, carga])`
- `carga.set_upstream(notificacao)`

Formas de controlar a execução de tarefas.
- Branching: Determina qual tarefa mover a partir de uma condição.
- Latest Only: Só é executada em DAGs em execução no presente.
- Depends on Past: Tarefas podem depender de si mesmas de uma execução anterior.
- Trigger Rules: Permite definir as condições para um DAG executaruma tarefa.

### Edges Labels (Rótulos para tarefas)

Podemos definir labels para documentar as relações e dependências entre tarefas.
- `get_acuracy_op >> check_acuracy_op >> Label("Limit 90%") >> [deploy_op, retrain_op] >> notify_op`
- `get_acuracy_op.set_downstream(check_acuracy, Label("Métrica ACC"))`

## Tasks

A unidade de execução mais básica do Airflow.
Podem ser de três tipos.
- Operadores , Sensores e Taskflow.
O relacionamento é definido através das dependências (upstream e downstreams).

- Estados de cada tarefa.

    - none: a tarefa ainda não foi enfileirada para execução (suas dependências ainda não foram atendidas).
    - scheduled: O agendador determinou que as dependências da Tarefa são atendidas e deve ser executado.
    - queued: A tarefa foi atribuída a um executor e está aguardando um trabalhador.
    - running: a tarefa está sendo executada em um trabalhador (ou em um executor local / síncrono).
    - success: a tarefa terminou em execução sem erro.
    - failed: a tarefa teve um erro durante a execução e falhou ao executar.
    - skipped: a tarefa foi ignorada devido a ramificação, LatestOnly ou semelhante.
    - upstream_failed: uma tarefa upstream falhou e a regra de acionamento diz que precisávamos dela.
    - up_for_retry: A tarefa falhou, mas ainda restam novas tentativas e será reprogramada.
    - up_for_reschedule: A tarefa é um Sensor que está em modo de reprogramação.
    - sensing: a tarefa é um sensor inteligente
    - removed: a tarefa desapareceu do DAG desde o início da execução.

## Xcoms - Cross Comunications entre tarefas

Transferência de dados entre tarefas.
- X-coms (Cross-communications) - push e pull metadados.
- Uploading e Downloading em serviços de armazenamento (Bancos de dados, serviços, arquivos)

## Montando um pipeline de dados

Requisitos do Pipeline.

- Necessidade de separar os dados do ambiente OLTP para o ambiente OLAP.
- Todas as tarefas devem ser executadas diariamente.
- Todo o processo deve ser notificado.
- O ambiente de stage deve ser limpo.
- Todos os logs devem ser mantidos.

- Criando um container mysql (Servidor OLTP - Fonte dos dados)

O OLTP, do inglês "On-line Transaction Processing", é o termo usado para se referir aos sistemas transacionais. O OLTP ou Processamento de Transações Online é um tipo de processamento de dados que consiste na execução de várias transações que ocorrem simultaneamente (transações bancárias online, compras, entrada de pedidos ou envio de mensagens de texto, por exemplo). Essas transações são tradicionalmente chamadas de transações econômicas ou financeiras, registradas e protegidas para que uma empresa possa acessar as informações a qualquer momento para fins contábeis ou de relatórios.

`docker run -d --name mysql_oltp -p "3306:3306" -v "C:\Wesley\airflow\data:/home" -e MYSQL_ROOT_PASSWORD=airflow mysql:8.0.27`

Para se conectar com o container criado

`docker container exec -it mysql_oltp`

- Criando um container postgres (Servidor OLAP - Destino dos dados)

OLAP, do inglês "On-line Analytical Processing", trata da capacidade de analisar grandes volumes de informações nas mais diversas perspectivas dentro de um Data Warehouse (DW). O OLAP também faz referência às ferramentas analíticas utilizadas no BI para a visualização das informações gerenciais e dá suporte para as funções de análises do negócio organizacional.

`docker run -d --name postgres_olap -p "3254:5432" -v "C:\Wesley\airflow\data:/home" -e POSTGRES_PASSWORD=airflow -d postgres`

Para se conectar com o container criado

`docker container exec -it postgres_olap`

Dentro do container do postgres, para entrar no banco de dados, use:

`psql -h localhost -U postgres`

Conectar no container do airflow como super usuário:

`docker container exec -it --user root 54452a99d6acb819ba00b59bc7630f4a67a6606bded9701e8dccb1607f56d2ad bash`

### Diferenças OLTP x OLAP

O OLTP permite a execução em tempo real de um grande número de transações por um grande número de pessoas, enquanto o processamento analítico online (OLAP) geralmente envolve a consulta dessas transações (também chamadas de registros) em um banco de dados para fins analíticos. O OLAP ajuda as empresas a extrair insights de dados de transações para que possam usá-los em tomadas de decisões mais informadas.

Configurando o Airflow para enviar E-mails

Site para serviço de smtp
*mailtrap.io*

Servidor SMTP
- Criar uma conta no Mailtrap.
- Configurar o arquivo de configurações do Airflow.

Conectar no container do airflow como super usuário:

`docker container exec -it --user root 54452a99d6acb819ba00b59bc7630f4a67a6606bded9701e8dccb1607f56d2ad bash`

Instalando o vim e o utilitário de rede no container airflow:

Conectar no container do airflow como super usuário:

`apt-get update && apt-get install vim iputils-ping -y`

Inspecionar o container para obter o ip

`docker inspect postgres_olap`