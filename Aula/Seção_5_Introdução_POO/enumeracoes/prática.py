import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])
# Fazer a mesma coisa só que com classe
class Direcoes(enum.Enum):
  ESQUERDA = enum.auto()
  DIREITA = enum.auto()
  ACIMA = enum.auto()
  ABAIXO = enum.auto()

print(Direcoes(1).name, Direcoes['ESQUERDA'], Direcoes.ESQUERDA.value)

def mover(direcao: Direcoes):
  if not isinstance(direcao, Direcoes):
    raise ValueError('Direção não encontrada')
  
  print(f'Movendo para {direcao.name}, ({direcao.value})')
  
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
mover(Direcoes.ACIMA)
mover(Direcoes.ABAIXO)
# mover('lado')