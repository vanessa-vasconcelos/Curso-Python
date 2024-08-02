# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

#class Foo(objetc): # parenteses com a super clase dentro, transformando isso em herança

class Pessoa:
  def __init__(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome
    
  def falar_nome_class(self):
    print(self.nome, self.sobrenome, self.__class__.__name__)
    
# A classe Cliente herda tudo da classe pessoa
class Cliente(Pessoa): 
  ...
  
class Aluno(Pessoa):
  ...
  
c1 = Cliente('Vanessa', 'Vasconcelos')
c1.falar_nome_class()
a2 = Aluno('Helena', 'Barros')
a2.falar_nome_class()

help(Cliente)