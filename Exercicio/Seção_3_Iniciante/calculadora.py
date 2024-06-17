#Pedir dois números e um operador lógico para o usuário
#Só sera feito com os seguintes operadores: 
# + - * / 

entrada_numero_01 = input('Digite um número: ')
entrada_operador = input('Digite um operador lógico: + (adição) - (subtração) * (multiplicação) / (divisão):  ')
entrada_numero_02 = input('Digite outro número: ')

if entrada_numero_01.isdigit():
  numero_01 = int(entrada_numero_01)
elif entrada_numero_01.isalpha():
  print('Escreva somente números')
else:
  numero_01 = float(entrada_numero_01)
  
if entrada_numero_02.isdigit():
  numero_02 = int(entrada_numero_02)
elif entrada_numero_02.isalpha():
  print('Escreva somente números')
else:
  numero_02 = float(entrada_numero_02)
  print(type(numero_02))
  
  
while entrada_operador == '+':
  resultado = numero_01 + numero_02
  print(resultado)
  break
  
while entrada_operador == '*':
  resultado = numero_01 * numero_02
  print(resultado)
  break
  
while entrada_operador == '-':
  resultado = numero_01 - numero_02
  print(resultado)
  break
  
while entrada_operador == '/':
  resultado = numero_01 / numero_02
  print(resultado)
  break