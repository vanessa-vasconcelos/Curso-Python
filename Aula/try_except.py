'''
Introdução ao try/except
try - tentar executar o código
exception - ocorreu algum erro ao tentar executar
'''

numero = input('Vou dobrar o número que você digitar: ')

# isdigit() verifica se o usuário digitou apenas números (se colocar ponto ele retorna false)
# if numero.isdigit():
#   numero_float = float(numero)
#   print(f'O dobro de {numero} é {numero_float * 2:.2f}')
# else:
#   print('Isso não é um número')

try:
  print('STR:', numero)
  numero_float = float(numero)
  print(f'O dobro de {numero} é {numero_float * 2:.2f}')
  print('FLOAT', numero_float)
  print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
  print('Isso não é um número')