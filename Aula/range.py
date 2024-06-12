''''
For + Range 
range --> range(start, stop, step)
'''

numeros = range(10) # quando passa somente um número, ele é o stop, nesse caso, vai de 0 a 10, mas o último não é incluido
# numeros = range(5, 10) 
# numeros = range(5, 10, 2) #pula de 2 em 2 

for numero in numeros:
  print(numero)