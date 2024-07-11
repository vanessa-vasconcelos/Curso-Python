# Métodos úteis dos dicionários em Python
# get - obtém uma chave
# pop - Apaga um item com a chave especifica (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

p1 = {
  'nome': 'Vanessa',
  'sobrenome': 'Vasconcelos'
} 

# Retorna o valor da chave nome
#print(p1.get('nome'))
# Casdo a chave não exista, você pode determinar um valor padrão 
#print(p1.get('nome', 'Não existe'))

#nome = p1.pop('nome')
#print(nome)
#print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

p1.update({
  'nome': 'Taki',
  'idade': 22
})
print(p1)

# Ou pode fazer assim
p1.update(nome='novo valor', idade=22)

# Uma outra forma também é assim, pode ser feito com tupla ou lista
tupla = ('nome', 'valor novo'), ('idade', 30)
p1.update(tupla)
print(p1)
