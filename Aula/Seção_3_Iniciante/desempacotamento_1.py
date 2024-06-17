'''
Desempacotamento em chamadas de métodos de funções
'''

string = 'ABCD'
lista = ['Maria', 'Helena',1, 2, 3, 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
  [ 'Maria', 'Helena', ], 
  ['Elaine', ],
  ['Luiz', 'João', 'Eduarda',],
  # ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]

# a, b, *_, c = (lista)
# print(a, c)

# for nome in lista:
#   print(nome, end=' ')
  
# Os dois retorna a mesma coisa e do mesmo jeito
# print(*lista)
# print('Maria', 'Helena',1, 2, 3, 'Eduarda')

print(*salas, sep='\n')