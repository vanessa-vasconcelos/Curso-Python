import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'csv_writer.csv'

lista_clientes = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(CAMINHO_CSV, 'w', encoding='utf-8-sig') as arquivo:
  nome_colunas = lista_clientes[0].keys()
  escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
  escritor.writeheader()
  
  for cliente in lista_clientes:
    escritor.writerow(cliente)

# with open(CAMINHO_CSV, 'w', encoding='utf-8-sig') as arquivo:
#   nome_colunas = lista_clientes[0].keys()
#   escritor = csv.writer(arquivo)
  
#   escritor.writerow(nome_colunas)
  
#   for cliente in lista_clientes:
#     escritor.writerow(cliente.values())