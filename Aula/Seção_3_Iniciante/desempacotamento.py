# Introdução ao desempacotamento + tuples (tuplas)
nomes = ['Maria', 'Helena', 'Samanta']
nome1, nome2, nome3 = nomes
print(nome2)

# Ou pode fazer
nome1, nome2, nome3 = ['Maria', 'Helena', 'Samanta']

# Quando precisa somente de um valor de uma lista, o resto dos valores precisam está em algum lugar
# *nome_da_variavel = vai guardar todo o valor que resta, que não deseja pegar da lista
_, nome5, *_ = ['Maria', 'Helena', 'Samanta']
print(nome5)