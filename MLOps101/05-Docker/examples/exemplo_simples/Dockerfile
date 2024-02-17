# Use a imagem base do Python alpine: versao mais leve do Python
FROM python:3.9-alpine 

# Copie o script Python para o diretório de trabalho do contêiner
COPY script.py /app/script.py

# Copie o arquivo de dependências para o diretório de trabalho do contêiner
COPY requirements.txt ./requirements.txt

# Instale as dependências do script Python (se houver) - (-t aponta) apontando para o diretório /app
RUN pip install -r requirements.txt -t /app

# Defina o diretório de trabalho como /app
WORKDIR /app

# Instale as dependências do script Python (se houver)
# RUN pip install -r requirements.txt

# Execute o script Python quando o contêiner for iniciado
CMD ["python", "script.py"]
