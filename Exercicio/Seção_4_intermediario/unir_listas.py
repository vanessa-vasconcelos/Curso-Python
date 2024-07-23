# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

# min(parametro1, parametro2) - retorna quem possue o menor valor dos parametros
# max(parametro1, parametro2) - retorna quem possue o maior valor dos parametros

def ziper(list1, list2):
  intervalo_maximo = min(len(list1), len(list2))
  return [
    (list1[i], list2[i]) for i in range(intervalo_maximo)
  ]
  

lista_cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estado = ['BA', 'SP', 'MG', 'RJ']

lista_certa = ziper(lista_cidade, lista_estado)
print(ziper(lista_cidade, lista_estado))
print()

# O Python já possui uma função que se cgama zip que realiza as mesmas coisas, com a mesmoa lógica

lista_cidade = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estado = ['BA', 'SP', 'MG', 'RJ']
print(list(zip(lista_cidade, lista_estado)))
print()


# itertools = faz a mesma coisa de zip só que invertido na lógica do valor, invés de ser por base
# na lista menor, ela faz com base na lista maior

from itertools import zip_longest
print(list(zip_longest(lista_cidade, lista_estado, fillvalue='Sem cidade')))