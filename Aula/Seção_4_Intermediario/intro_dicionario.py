'''
* Dicionário em Python (tipo dict)
* Dicionários são estruturas de dados do tipo par de "chave" e "valor".
* Chaves podem ser consideradas como o "índice" que vimos na lista e podem ser de tipo imutáveis como:
tsr, int, float, bool, tuple, etc.
* O valor pode ser de qualquer tipo, incluindo outro dicionário.
* Usamos as chaves - {} - ou a classe dict para criar dicionário.
* Imutáveis = str, int, float, bool, tuple
* Mutável = dict, list
'''

pessoa = { 
  'nome': 'Vanessa',
  'sobrenome': 'Vasconcelos',
  'idade': 22,
  'altura': 1.6,
  'endereços': [
    {'rua': 'tal tal', 'numero': 123},
    {'rua': 'bla bla', 'numero': 789},
  ]         
}

# Sobreescrevir o dicionario 'pessoa'
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

# print(pessoa, type(pessoa))

print(pessoa['nome'])
print(pessoa['idade'])
print()
for chave in pessoa:
  print(chave, pessoa[chave])