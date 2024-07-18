#copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dados import produtos
import copy

novos_produtos = [
  {**p, 'preco': round(p['preco'] * 1.1, 2)} 
  for p in produtos]


produtos_decrescentes = sorted(produtos, key=lambda p: p['nome'])
produtos_crescentes = sorted(produtos, key=lambda p: p['nome'], reverse=True)



print(*novos_produtos, sep='\n')
print()
print(*produtos, sep='\n')
print()
print(*produtos_decrescentes, sep='\n')
print()
print(*produtos_crescentes, sep='\n')

