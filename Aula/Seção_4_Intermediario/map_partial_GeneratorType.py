# map - para mapear dados
from functools import partial # partial é uma função que vai resceber outra função 
from types import GeneratorType

def print_iter(iterator):
  print(*list(iterator), sep='\n')
  print()
  
def aumentar_porcentagem(valor, porcentagem):
  return round(valor * porcentagem, 2) # round arredonda
  

aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [
#   {**p, 'preco': aumentar_dez_porcento(p['preco'])} for p in produtos
# ]

def muda_preco_de_produtos(produto):
  return {**produto, 'preco': aumentar_dez_porcento(produto['preco'])}

# O map vai pegar a função muda_preco_de_produtos e vai passar por todos os valores da lista produtos
novos_produtos = map(muda_preco_de_produtos, produtos) # iterator

novos_produtos = (x for x in produtos) # generation

# Todo generation é iterator, mas nem todo iterator é um generetion

print_iter(produtos)
print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorExit))