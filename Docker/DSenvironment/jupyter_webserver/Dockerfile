FROM ubuntu:xenial

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


