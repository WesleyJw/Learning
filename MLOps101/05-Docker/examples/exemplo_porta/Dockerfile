# Use uma imagem base que inclua Python, como python:3
FROM python:3.9-alpine

# Instale o Flask
RUN pip install flask

# Copie o código do aplicativo para o contêiner
COPY app.py /app.py

# Exponha a porta 5000
EXPOSE 5000

# Comando a ser executado ao iniciar o contêiner
CMD ["python", "/app.py"]
