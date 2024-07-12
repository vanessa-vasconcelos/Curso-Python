'''
Sets são eficientes para remover valores duplicados de iteráveis
- Seus valores serão sempre únicos
- Ele elimina natural mente valores duplicados
- Não aceitam valores mutáveis
- Não tem índices
- Não geram ordem
- São iteráveis (for, in. not in)
'''

s1 = {1, 2, 3, 3, 3, 3, 3, 3, 1}
print(s1)
print()

# Uma forma de eliminar valores duplicados de listas e tuplas, no entanto, como o set não garante a ordem dos valores, essa
#não é a melhor forma para realizar tal processo
l1 = [1, 2, 3, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)
print()

# Não aceita lista ou outro set dentro dele
# s1 = {1, 2, 3, 3, 3, 3, 3, 3, 1, {123}} # Tal ação gera erro no código
# print(s1)

# Consigo utilizar formas de saber se determinado valor está dentro do set
print(3 in s1)

for numero in s1:
  print(numero)