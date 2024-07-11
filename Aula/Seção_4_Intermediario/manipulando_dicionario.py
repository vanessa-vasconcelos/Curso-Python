pessoa = {}

# Adicionando chave(índice) e valor no dicionário
pessoa['nome'] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Maria'
print(pessoa)
print()

# Acessando valor da chave(índice) nome
print(pessoa['nome'])
print()

# Dinâmico, pois está colocando em uma variável
chave = 'nome'
pessoa[chave] = 'Vanessa'
print(pessoa[chave])
print()

# Apagar uma chave
del pessoa['sobrenome']
print(pessoa)
print()

# Alterar um valor no dicionário
pessoa[chave] = 'Maria'
print(pessoa)
print()

# Acessar uma chave inexistente, como evitar o erro e manter o código rodando
# get, por padrão retorna None

if pessoa.get('sobrenome') is None:
  print('NÃO EXISTE')
else:
  print(pessoa['sobrenome'])

