# 1. Data Engineering Review

## Introdução aos conceitos de Engenharia de Dados



### Tipos de processamentos


- **Processamento em Batch:**
  
Qunado falamos em processamento em *Batch* no referimos ao processamento que ocorre em lotes, ou seja, estes serviços ocorrem quando um determinado número de ocorrências acontece e em um determinado momento estas ocorrências serão processadas. Exemplos de processamento em batch são: Cargas de um banco de dados, processamento ETL de determinado serviço, entre outros. 

A Principal vantagem  é o processamento de grande volumes de dados, já a desvantagem é que necessista de uma pessoa dedicada para resolver problemas. Sua principal **arquitetura** é a **lambda**. 

- **Processamento em Streaming:**

O processamento em *streaming* acontece em tempo real ou em tempo próximo ao tempo real. Sendo assim, quando ocorre um evento já existe um mecanismo que processa os dados e faz todo o tramento necessário, chegando até mesmo ao ponto de classificação. Exemplos de processamento em streaming são: Compras em cartão de crédito, localização em tempo real, sensores, entre outros.

A principal vantagem é promover a análise em tempo real, e a desvantagem é que necessita de um sistema de coleta rápido e efciaz.  A pricnipal arquitetura para esse processamento é a **Kafka**. 

### O que é Apache Spark

É um projeto open source, que nada mais é que um engine de processamento em ambiente distribuído. Um abiente distibuído seria um cluster de computadores que se comunicam entre si e executam determinadas partes de um mesmo trabalho.

O spark possui uma interface para trabalhar com python, R, java, scala, c#, entre outras linguagens. 

#### API's do spark:

- MLib: Machine learning;
- Streaming: Análises em tempo real;
- SQL: Queries interativas;
- GraphX: processamento gráfico.

### Databricks

É uma solução em cloud (Computação em Nuvem), que tem como objetivo permitir processar clusters de máquinas sparks em cloud. Possui diversas soluções para computação em nuvem. 

####  Criando a conta no Databricks Community

Site da empresa: databricks.com

Entrar em Try databricks  e fazer cadastro. 

Para começar a tabrablhar no databricks, clique m Compute e crie um novo cluster. Preencha os campos com as informações de nome do cluster, linguagem, gpu entre outras. O cluster é criado, porém não possui nada atrelado a ele. 

### Dataframes e Partições no Spark

Os dataframes são estrututras em memória (tabela) para realizar trabalhos. Os dataframes spaks particionadas em diversas máquinas (nós).

Boas pŕaticas de gestão no Data Lake. 

Data               | Data Lake Zone | Consumer Systems
-------------------|----------------|----------------------------
Streaming          |                |Catalogação dos dados
Arquivos de dados  |                |Ferramentas de praparação dos dados
Tabelas relacionais|                |Visualização dos dados
  .-               |        -       | Conexões Externas


- **Explicando a Data Lake Zone:**


Transient Zone                    | Raw Zone                | Trusted Zone          | Refined Zone
---------------------------------|-------------------------|-----------------------|-------------------
Ingestão de dados, categorização,|Aplicação de metadadados,|Qualidade dos dados,   | Enriquecimento dos dados
e Catagologação                  |Proteções e  atributos   |validação              | Automação e workflows 
