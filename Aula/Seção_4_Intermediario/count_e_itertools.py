# count é um iterador sem fim (itertools)

from itertools import count

c1 = count(8, 8)
r1 = range(10, 100, 8)
# count ele entrega o valor e soma mais 1 com o next
print(next(c1))
print()

print('count')
for i in c1:
  if i >= 100:
    break
  print(i)
  
print()

print('raqnge')
for i in r1:
  if i > 100:
    break
  print(i)
  