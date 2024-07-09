'''
Exercícios com funções

2 - Crie uma função que fala se um número é par ou ímpar. Retorne se o número é par ou ímpar
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
      print(f'O {numero} é um número par.')
    else:
      print(f'O {numero} é um número ímpar.')

par_ou_impar(6)
