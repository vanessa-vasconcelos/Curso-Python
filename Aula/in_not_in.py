"""
Strings são iteráveis
"""

nome_teste = 'Vanessa'
print(nome_teste[2])
print(nome_teste[-2])
# Irá percorrer todas as letras da variável e caso tenha a letra 'e' no nome_teste, ele retorna True
print('e' in nome_teste) 
print('z' in nome_teste) 
print('z' not in nome_teste) # Retorna True
print('e' not in nome_teste) # Retorna False


nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} está em {nome}')
else: 
  print(f'{encontrar} não está em {nome}')