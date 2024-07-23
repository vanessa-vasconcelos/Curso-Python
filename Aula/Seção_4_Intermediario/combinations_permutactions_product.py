'''
Comnations, Permutations e Product - Intertools
Combinação = Ordem não importa - iterável + tamanho do grupo
Permutação = Ordem importa
Produto = Ordem importa e repete valores únicos
'''
from itertools import combinations, permutations, product

def print_iter(iterador):
  print(*list(iterador), sep='\n')
  print()

pessoas = [
  ' João', 'Joana', 'Luiz', 'Letícia'
]
camisetas = [
  ['preta', 'branca'],
  ['p', 'm', 'g'],
  ['masculino', 'feminino']
] 

print_iter(combinations(pessoas, 2)) # quero junção dos valores de pessoas em grupo de 2
print_iter(permutations(pessoas, 3)) 
print()

print_iter(product(*camisetas))

