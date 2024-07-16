lista = []
for x in range(3):
  for y in range(3):
    lista.append((x, y))
# print(lista)

# Gera o mesmo resultado
lista_01 = [ 
  (x, y)
  for x in range(3) 
  for y in range(3)
]

# Para cada x estou gerando uma nova lista comprehension
lista_01 = [ 
  [(x, 
    letra) for letra in 'Vanessa']
  for x in range(3) 
]
print(lista_01)
