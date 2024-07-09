'''
Exercícios com funções

1 - Crie uma função que multiplica todos os argumentos não nomeados recebidos. Retorne o total para uma variável e mostre
o valor da variável.
'''
def multiplicacao(*args):
  total = 1
  for numero in args:
   total *= numero
  return total

total = multiplicacao(1, 2, 3)
print(total)
print(1 * 2 * 3)
 