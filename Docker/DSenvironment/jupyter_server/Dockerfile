FROM jupyter/datascience-notebook:r-4.1.1

USER root

RUN  apt-get update && \
    apt-get install -y \
    libhdf5-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libxml2-dev \
    libpng-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libglpk40 \
    libgit2-28 &&\
    apt-get clean && rm -rf var/lib/apt/lists/*

USER $NB_UID

RUN conda install --quiet --yes \
    'psycopg2' \
    'nltk'\
    'r-rpostgresql' \
    'r-RPostgres' \
    'r-sqldf' \
    'r-getpass' \
    'r-lme4' \
    'r-tidyverse' \
    'r-rmarkdown' \
    'r-workflowr' \
    'r-shiny'  && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

WORKDIR /home/work
