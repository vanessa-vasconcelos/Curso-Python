''' 
Funções recursivas e recursividade
- funcções que podem se chamar de volta 
- úteis p/ dividir problemas grandes em partes menores 
# Toda função recursiva deve ter:
- Um problema que possa ser dividido em partes menores
- Um caso recursivo que resolve o pqueno problema 
- Um caso base que para a recursão
'''
def recursiva(inicio=0, fim=10):
  # Caso base
  if inicio >= 10:
    return fim
  
  # CASO RECURSIVO
  # CONTAR ATÉ CHEGAR AO FINAL
  inicio += 1
  return recursiva(inicio, fim)
  
  
print(recursiva())
print()

def factorial(n):
  if n <= 1:
    return 1
  
  return n * factorial(n - 1)

print(factorial(10))