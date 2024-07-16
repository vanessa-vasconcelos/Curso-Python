# Mapeamento de dados em list comprehemsion

produtos = [ 
            {'nome': 'p1', 'preco': 20},
            {'nome': 'p2', 'preco': 10},
            {'nome': 'p3', 'preco': 30},
]

# Mapeamento

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.05}
  if produto['preco'] > 20 else {**produto}
  for produto in produtos
]

# Desempacotar o dicionário
print(*novos_produtos, sep='\n')