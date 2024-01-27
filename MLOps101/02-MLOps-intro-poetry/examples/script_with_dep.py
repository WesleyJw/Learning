import argparse

import pandas as pd


def ler_arquivo(caminho):
    """Lê um arquivo CSV e retorna um DataFrame"""
    return pd.read_csv(caminho, sep=";", header=1)


# Criação do objeto ArgumentParser
parser = argparse.ArgumentParser(description="Exemplo de script com argumento")

# Adição do argumento
parser.add_argument(
    "--caminho",
    type=str,
    help="Caminho para o arquivo de entrada",
    default="exemplos/exemplo.csv",
)

# Parse dos argumentos da linha de comando
args = parser.parse_args()

# Leitura do arquivo
df = ler_arquivo(args.caminho)

# Exibição do DataFrame
print(df)
