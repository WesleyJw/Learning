import argparse

# Criação do objeto ArgumentParser
parser = argparse.ArgumentParser(description="Exemplo de script com argumento")

# Adição do argumento
parser.add_argument("--nome", type=str, help="Nome a ser exibido")
parser.add_argument("--idade", type=int, help="Nome a ser exibido", default=32)

# Parse dos argumentos da linha de comando
args = parser.parse_args()

# Exibição do nome fornecido como argumento
print(f"Olá, {args.nome}! Você tem {args.idade} anos.")

# Execute in terminal with:
#  python3 exemplos/script_com_argumento.py --nome Wesley
