'''
 Listas em Python
 Tipo list - Mutável
 Suporta vários valores e qualquer tipo 
 Conhecimento reutilizáveis - índices e fatiamento
 Métodos úteis: append, insert, pop, del, clear, extend, +
'''

lista = [123, True, 'Vanessa', 1.2, [], 10, 20, 300]

#Upper = deixa tudo em maiúsculo 
print(lista[2].upper(), type(lista[2]))

# Alterou o valor do índice
lista[-3] = 'Maria'
print(lista[2], type(lista[2]))

# Apagar um índice
del lista[1]
print(lista)

# Adicionar um valor no final da lista
lista.append(50)
print(lista)

# Remover o último índice da lista
lista.pop()
print(lista)
#Posso remover um índice específico também com pop
lista.pop(4)
print(lista)

# Limpar a lista
#lista.clear

# Adiciona um item no índice escolhido
lista.insert(0, 5) # Primeiro valor é para qual índice que deseja mexer, o segundo é o valor que deseja incluir
print(lista)

# União de listas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

# Uma outra forma de juntar listas
lista_a.extend(lista_b)
print(lista_a)

# Copiar uma lista
lista_j = ['Luiz', 'Vanessa']
lista_k = lista_j.copy()
print(lista_k, lista_j)