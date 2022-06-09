FROM rocker/rstudio:4.0.5

LABEL maintaner="Wesley Lima" \ 
    email="<wesley.datascientist@gmail.com>" \
    url="wesleyjw.github.io"  

RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    libhdf5-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libxml2-dev \
    libpng-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    libglpk40 \
    libgit2-28 \
    && apt-get clean all && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN Rscript -e "install.packages(c('RPostgreSQL', 'RPostgres', 'sqldf', 'rmarkdown', 'tidyverse', 'workflowr', 'shiny'))"