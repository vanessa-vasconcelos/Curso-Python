salas = [
  [ 'Maria', 'Helena', ], 
  ['Elaine', ],
  ['Luiz', 'João', 'Eduarda',],
  # ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]
]

# Primeiro cochete = acessa a lista, segundo cochete = acessa o valor
# print(salas[1][0])
# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
  print(f'A sala é{sala}')
  for aluno in sala:
    print(aluno)