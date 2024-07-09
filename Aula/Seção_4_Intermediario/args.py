'''
args - Argumentos não nomeados
* - *args(empacotamento e desempacotamento)
'''
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

# * de argumentos não nomeados
def soma(*args):
  args = list(args) # Transformando a tupla em lista
  print(args, type(args)) # Os valores passados viram uma tupla
  
# def soma(*args):
#   total = 0
#   for numero in args:
#     print(total, '+', numero )
#     total += numero
#     print('Total =', total)
  
# Dessa forma não dá erro na função
soma(1, 2, 3, 4, 5, 6)

def soma(*args):
  total = 0
  for numero in args:
    total += numero
  return total

soma_1_2_3 = soma(1,2,3)
print(soma_1_2_3)

numeros_1 = 1,2,3
# Com o * eu desempacotei
soma_1 = soma(*numeros_1)
print(soma_1)

# sum é uma função que já existe no Python que serve para somar números 
print(sum((1,2,3,4,5,63,963,4,5,2)))
print(sum(numeros_1))