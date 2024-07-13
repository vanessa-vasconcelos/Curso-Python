# List comprehension em Python
# É uma forma rápida para criar listas a partir de iteráveis

print(list(range(10)))
print()

lista = []
for numero in range(10):
  lista.append(numero)
print(lista)
print()


# Tem como fazer essa lista com List comprehensiom
lista = [numero for numero in range(10)]
print(lista)
print()

# Multiplicar cada numero da lista por 2
lista = [numero * 2 for numero in range(10)]
print(lista)

