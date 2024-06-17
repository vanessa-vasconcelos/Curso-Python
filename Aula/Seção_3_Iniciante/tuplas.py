'''
Tupla - Uma lista imutável
'''
# Para criar um a tupla, é opcional os parenteses no inicio e fim
nomes = 'Maria', 'Helena', 'Luiz'

# Convertendo uma lista para tupla
nomes_lista = ['Maria', 'Helena', 'Luiz']
nomes_tupla = tuple(nomes_lista)
# Convertendo tupla em lista
nome_LISTA_2 = list(nomes_tupla)
print(type(nomes_tupla))