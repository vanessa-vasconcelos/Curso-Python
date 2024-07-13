'''
Função lambda em Python
A função lambda é uma função como qualquer outra em Python. Porém, são funções anônimas que
contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
'''

lista_01 = [4, 32, 1, 5, 35, 6, 6, 21]
# Ela ordena a lista de forma crescente
lista_01.sort() 
# Para deixar em ordem decrescente basta acrescentrar o reverse=True
lista_01.sort(reverse=True) 
print(lista_01)
print()

lista_02 = [
     {'nome': 'Luiz', 'sobrenome': 'miranda'},
     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
     {'nome': 'Daniel', 'sobrenome': 'Silva'},
     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
     {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def orderna(item):
  return item['nome']

lista_02.sort(key=orderna)

# o lambda retorna a mesma coisa da função acima
lista_02.sort(key=lambda item: item['nome'])
  
def exibir(lista):
  for item in lista:
    print(item)


print()
print()

l1 = sorted(lista_02, key=lambda item: item['nome'])
l2 = sorted(lista_02, key=lambda item: item['sobrenome'])
exibir(l1)
exibir(l2)