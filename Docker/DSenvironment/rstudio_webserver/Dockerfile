FROM rocker/rstudio:4.0.5

LABEL maintaner="Wesley Lima" \ 
    email="<wesley.datascientist@gmail.com>" \
    url="wesleyjw.github.io"  

RUN apt-get update && \
    apt-get upgrate -y && \
    apt-get install -y \
    libhdf5-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    libxml2-dev \
    libpng-dev \
    zliblg-dev \
    libbz2-dev \
    liblzma-dev \
    libglpk40 \
    libgit2-28 \
    && apt-get clean all && \
    apt-get purge && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN Rscript -e "install.packages(c('rmarkdown', 'tidyverse', 'workflowr', 'shiny'))"

COPY user-settings /home/rstudio/.rstudio/monitored/user-settings
COPY .Rprofile /home/rstudio/