num_1 = input('Digite um valor: ')
num_2 = input('Digite outro valor: ')

valor_1 = int(num_1)
valor_2 = int(num_2)

if valor_1 < valor_2:
  print(f'O {valor_1} é menor que {valor_2} ')
elif valor_1 ==  valor_2:
  print('Os os dois valores são iguais')
else:
  print(f'O {valor_1} é maior que {valor_2}')