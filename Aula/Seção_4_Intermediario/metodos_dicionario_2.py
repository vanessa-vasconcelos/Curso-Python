# Métodos úteis dos dicionários em Python
# copy - retorna uma cópia rasa (shallow copy = ). O copy não copia uma lista que está dentro de um 
#dicionário ou qualquer outro agrupador dentro do dicionário, nesse caso, vai apontar para a mesma memória 

import copy

d1= {
  'c1': 1,
  'c2': 2,
  'li': [0, 1, 2]
} 

d2 = d1.copy()

# Caso queira fazer a cópia de tudo, basta importar o copy e utilizar deepcopy que é uma cópia profunda
d2 = copy.deepcopy(d1)

d2['c1'] = 1000
d2['li'][1] = 999999
print(d1)
print(d2)

