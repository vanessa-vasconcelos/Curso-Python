import pprint

def p(v):
  pprint.pprint(novos_produtos, sort_dicts=False, width=40)
  

produtos = [ 
  {'nome': 'p1', 'preco': 20},
  {'nome': 'p2', 'preco': 10},
  {'nome': 'p3', 'preco': 30},
]

# Mapeamento


# print(novos_produtos)
# p(novos_produtos)

# Filtro: eu não quero determinada coisa na minha lista se a condição for verdadeira
# if é depois do for 

lista = [ n for n in range(10) if n < 5]
print(lista)

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  if produto['preco'] > 20 else {**produto}
  for produto in produtos
  if produto['preco'] >= 20 and (produto['preco'] * 1.05)> 10
]

p(novos_produtos)