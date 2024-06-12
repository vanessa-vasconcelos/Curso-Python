"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

entrada_hora = input('Digite a hora em número inteiro: ')
nome = input('Digite o seu nome: ')

try:
  hora = int(entrada_hora)

  if hora >= 0 and hora <= 11:
    print(f'Bom dia, {nome}')
  elif hora >= 12 and hora <= 17:
    print(f'Boa tarde, {nome}')
  elif hora >= 18 and hora <= 23:
    print(f'Boa noite, {nome}')
  else:
    print('Não conheço essa hora')

except:
  print('Você não digitou a hora em número inteiro.')