# Empacotamento e desempacotamento de dicionários 
a, b = 1, 2
a,b = b, a
#print(a, b)
print()

pessoa = {
  'nome': 'Aline',
  'sobrenome': 'Souza'
}

dados_pessoa = {
  'idade': 16,
  'altura': 1.6
}

# Dessa forma, a e b seram as chaves nome e sobrenome
a,b = pessoa
print(a, b)

# Desse jeito, a e b seram o valor das chaves
a,b = pessoa.values()
print(a, b)

# Com items ele retorna uma tupla com uma chave e um valor
a,b = pessoa.items()
print(a, b)

#desempacotamento interno
(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

# Empacotamento no for
for valor in pessoa.items():
  print(valor)
  
# Desempacotamento no for
for chave, valor in pessoa.items():
  print(chave, valor)

# Unir dois dicionários, posso criaroutro dicionário e extrair os valores dos dicionarios anterios e 
#colocar em um terceiro

# Extrair todos os dados do dicionário pessoa
pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

# args e kwargs
# kwargs - keyword argumentos (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
  print('NÃO NOMEADOS:', args)
  
  for chave, valor in kwargs.items():
    print(chave, valor)
  

#mostro_argumentos_nomeados(1, 2, nome='Joana', qlq=123)

# Desempacotar
#mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
  'arg1': 1,
  'arg2': 2,
  'arg3': 3,
  'arg4': 4,
  'arg5': 5,
  'arg6': 6,
}

mostro_argumentos_nomeados(**configuracoes)