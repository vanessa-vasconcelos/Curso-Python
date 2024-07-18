#Exercício - Adiando execução de funções

def soma(x):
  return x + soma_sempre_cinco

def multiplica(x):
  return x * multiplica_sempre_dez

def criar_funcao(funcao, *args):
  return funcao(*args)

def soma_sempre_cinco(x):
  return x + 5

def multiplica_sempre_dez(x):
  return x * 10