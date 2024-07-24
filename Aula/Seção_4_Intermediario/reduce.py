# reduce - faz a redução de um iterável em um valor - reduzir valores em um valor 
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

def funcao_do_reduce(acumulador, produto):
  print('acumulador',acumulador)
  print('produto', produto)
  print()
  return acumulador + produto['preco']

total = reduce(
  #funcao_do_reduce, 
  lambda ac, p: ac + p['preco'],
  produtos, 
  0 # o numero é o valor inicial
)
print('Total é', total)

# total = 0
# for p in produtos:
#   total += p['preco']

# OU
# print(sum([p['preco] for p in produtos]))

# print(round(total, 2))

# Reduce faz a mesma coisa

