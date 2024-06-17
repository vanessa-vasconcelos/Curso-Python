'''
enumerate - enumera iteráveis (índices)
'''

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# Vai mostrar o índice e o valor

lista_enumerada = list(enumerate(lista))

print(lista_enumerada)

for item in enumerate(lista):
  print(item)

