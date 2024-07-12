# Métodos úteis dos dicionários em Python
# len - quantas chaves 
# keys - iterável com a chaves / tenho somente as chaves
# values - iterável com valores / tenho somente os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

pessoa = {
  'nome': 'Vanessa',
  'sobrenome': 'Vasconcelos'
} 

#print(pessoa.__len__())
# Mas como a forma acima é complicada, é usada de outra forma
#print(len(pessoa))

# print(pessoa.keys())
# conversão 
# print(list(pessoa.keys()))

# print(pessoa.values())
# print(list(pessoa.values()))

# print(pessoa.items())
# print(list(pessoa.items()))
# for chave, valor in pessoa.items():
#   print(chave, valor)

# pessoa.setdefault('idade', 1)
# print(pessoa['idade'])