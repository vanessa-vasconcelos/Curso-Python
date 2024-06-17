"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero.isdigit():
  numero_inteiro = int(numero)

  if numero_inteiro % 2 == 0:
    print(f'{numero_inteiro} é um número par')
  else:
    print(f'{numero_inteiro} é um número impar')
    
else:
  print('Você não digitou um número inteiro')