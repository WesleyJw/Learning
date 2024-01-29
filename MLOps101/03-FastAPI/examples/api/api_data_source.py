import sqlite3
from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


# Definir modelo de dados
class Item(BaseModel):
    id: int
    nome: str
    preco: float


# Criar aplicação FastAPI
app = FastAPI()


def criar_banco_de_dados():
    """Criar banco de dados e tabela"""
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    """
    )
    conn.commit()
    conn.close()


def criar_conexao():
    """Criar conexão com o banco de dados"""
    conn = sqlite3.connect("database.db", check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor


@app.get("/")
def home():
    return {"message": "Bem-vindo à API de exemplo!"}


# Rotas da API
@app.get("/items", response_model=List[Item])
def obter_itens():
    """
    Obter todos os itens do banco de dados
    Returns:
      List(Item): Lista de itens
    """
    conn, cursor = criar_conexao()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    items = [Item(id=item[0], nome=item[1], preco=item[2]) for item in items]
    return items


@app.post("/inserir", response_model=Item)
def criar_item(item: Item):
    """Criar um novo item no banco de dados

    Args:
        item (Item): Item a ser criado

    Returns:
        Item: Item criado
    """
    conn, cursor = criar_conexao()
    cursor.execute(
        "INSERT INTO items (nome, preco) VALUES (?, ?)", (item.nome, item.preco)
    )
    conn.commit()
    item.id = cursor.lastrowid
    return item


@app.get("/items/{item_id}", response_model=Item)
def obter_item(item_id: int):
    """Obter um item do banco de dados

    Args:
        item_id (int): ID do item

    Returns:
        Item: Item obtido
    """
    conn, cursor = criar_conexao()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    item = Item(id=item[0], nome=item[1], preco=item[2])
    return item


@app.post("/atualizar/{item_id}", response_model=Item)
def atualizar_item(item_id: int, item: Item):
    """Atualizar um item do banco de dados

    Args:
        item_id (int): ID do item
        item (Item): Item com os dados atualizados

    Returns:
        Item: Item atualizado
    """
    conn, cursor = criar_conexao()
    cursor.execute(
        "UPDATE items SET nome = ?, preco = ? WHERE id = ?",
        (item.nome, item.preco, item_id),
    )
    conn.commit()
    item.id = item_id
    return item


@app.delete("/items/{item_id}")
def deletar_item(item_id: int):
    """Deletar um item do banco de dados

    Args:
        item_id (int): ID do item

    Returns:
        _type_: Mensagem de sucesso
    """
    conn, cursor = criar_conexao()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    return {"message": f"Item {item_id} deletado"}


# Executar a aplicação
if __name__ == "__main__":
    criar_banco_de_dados()
    uvicorn.run(app, host="0.0.0.0", port=8000)
