'''
Métodos úteis do Set:
add, update, clear, discard
'''

s1 = set()

# Adicionar valor no set
s1.add('Vanessa')
s1.add(22)
print(s1)

# Atualiza o set com o valor que deseja
s1.update(('Olá mundo', 2, 4, 10)) # Para a frase ir toda junta e não separada por letra, tem que abrir o segundo ()
print(s1)

# Limpar o set
#s1.clear()
print(s1)

# Elimina um valor em específico
s1.discard('Vanessa') # Coloca o valor que deseja eliminar do set
print(s1)