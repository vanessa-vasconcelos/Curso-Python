'''
Operações úteis do Set:
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos
'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Unir dois sets
s3 = s1 | s2
print(s3)

# Valores presentes nos dois sets
s4 = s1 & s2
print(s4)

# A ordem importa na hora da diferença
s5 = s1 - s2
print(s5)

# Valor que não tem nos dois sets
s6 = s2 ^ s1
print(s6)
