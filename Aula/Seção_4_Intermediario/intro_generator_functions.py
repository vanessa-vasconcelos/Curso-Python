# Introdução as Generator functions em Python

# def generator(n=0):
#   yield 1 # Pausa
#   print('Continuando...') 
#   yield 2 # Pausa
#   print('Continuando...')
#   yield 3
#   print('Vou terminar...')
#   return 'Acabou'


def generator(n=0, maximum=10):
  while True:
    yield n
    
    n += 1
    
    if n > maximum:
      return

gen = generator(n=5, maximum=19)

for n in gen: 
  print(n)