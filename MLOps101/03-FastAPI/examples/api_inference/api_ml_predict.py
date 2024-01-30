import uvicorn
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from transformers import pipeline


# Define modelo de dado para resposta da API
class Predicao(BaseModel):
    """Modelo de dado para resposta da API"""

    predicao: str
    score: float


class Texto(BaseModel):
    """Modelo de dado para entrada da API"""

    texto: str


class TextoComAuth(BaseModel):
    """Modelo de dado para entrada da API com autenticação"""

    texto: str
    token: str


# Cria aplicação FastAPI
app = FastAPI()

# Carrega modelo de classificação de sentimento
CLASSIFICADOR_SENTIMENTO = pipeline("sentiment-analysis")


@app.get("/")
def home():
    """Rota inicial da API"""
    return {"message": "Bem-vindo à API de exemplo!"}


# Rotas da API
@app.post("/predicao/", response_model=Predicao)
def predicao(texto: Texto):
    """Predição de sentimento

    Args:
        texto (Texto): Texto a ser classificado
    Returns:
        Predicao: Predicao com a predição e o score
    """
    predicao = CLASSIFICADOR_SENTIMENTO([texto.texto])
    return Predicao(predicao=predicao[0]["label"], score=predicao[0]["score"])


# predicao com autenticacao via token
@app.post("/predicao_com_auth/", response_model=Predicao)
def predicao(texto: TextoComAuth):
    """Predição de sentimento com autenticação

    Args:
        texto (Texto): Texto a ser classificado com token de autenticação

    Returns:
        dict: Dicionário com a predição e o score
    """
    if (
        texto.token != "senha123"
    ):  # alerta: em produçao nao deixe a senha no codigo diretamente! Use variaveis de ambiente
        raise HTTPException(status_code=401, detail="Não autorizado")
    predicao = CLASSIFICADOR_SENTIMENTO([texto.texto])
    return Predicao(predicao=predicao[0]["label"], score=predicao[0]["score"])


# predicao com autenticacao via token no cabecalho
@app.post("/predicao_com_auth_cabecalho/", response_model=Predicao)
def predicao(texto: Texto, Authorization: str = Header(...)):
    """Predição de sentimento com autenticação.
    Mesmo método usado por exemplo pela OpenAI, veja: https://platform.openai.com/docs/quickstart?context=curl

    Args:
        texto (Texto): Texto a ser classificado
        Authorization (str): Token de autenticação no cabeçalho
    Returns:
        dict: Dicionário com a predição e o score
    """
    expected_token = "senha123"

    if Authorization != f"Bearer {expected_token}":
        raise HTTPException(status_code=401, detail="Não autorizado")
    predicao = CLASSIFICADOR_SENTIMENTO([texto.texto])
    return Predicao(predicao=predicao[0]["label"], score=predicao[0]["score"])


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
