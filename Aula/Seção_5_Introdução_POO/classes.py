'''
class - Classes são moldes para criar novos objetos 
As classes geram novos objetos (instâncias) que podem ter seus próprios artibutos e métodos
Os objetos gerados pela classe podem usar seus dados internos para realizar várias ações.
Por convenção, usamos PascalCase para nome de classes.
'''

# string = 'Luiz' #str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
  ...
  
p1 = Pessoa()
p1.nome = 'Vanessa'
p1.sobrenome = 'Vaconcelos'

p2 = Pessoa()
p2.nome = 'Marta'
p2.sobrenome = 'Santos'

# Como quero acessar o valor de nome não utiliza ()
print(p2.nome)
print(p2.sobrenome)
 
print(p1.nome)
print(p1.sobrenome)