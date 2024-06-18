'''
Valores padrão para parâmetros
Ao definir uma função, os parânmetros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor
padrão será usado.
Refatorar: editar o seu código'''

def soma(x, y, z=None):
  if z is not None:
    print(f'{x=} {y=} {z=}', z + x + y)
  else:
    print(f'{x=} {y=}', x + y)
    
soma(1, 2)
soma(3, 4)
soma(100, 200)
soma(7, 9, 0)
