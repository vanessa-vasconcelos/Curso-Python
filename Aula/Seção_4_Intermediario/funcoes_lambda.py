def executa(funcao, *args):
  return funcao(*args)

def soma (x,y):
  return x + y

def cria_multiplicador(multiplicador):
  def multiplica(numero):
    return numero * multiplicador
  return multiplica

duplica = cria_multiplicador(2)

# Essa lambda é a mesma coisa da função soma
print(executa(lambda x, y: x + y, 2, 3)) # O 2 e 3 são parametros que quero passar para x e y

# Este estrá fazendo a mesma coisa que a função cria_multiplicador
duplica = executa(lambda m: lambda n: n * m, 2)
print(duplica(2))


print(executa(lambda *args: sum(args), 1, 2, 3, 4, 53, 6,))