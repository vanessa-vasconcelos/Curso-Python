from typing import Any


def meu_repr(self):
  return f'{type(self).__name__}({self.__dict__})'

class Meta(type):
  def __new__(mcs, name, bases, dct):
    print('METACLASS NEW')
    cls = super().__new__(mcs, name, bases, dct)
    cls.__repr__ = meu_repr
    return cls
  
  
  def __call__(self, *args, **kwds):
    instance = super().__call__(*args, **kwds)
    print(instance.__dict__)
    return instance

class Pessoa:
  def __new__(cls, *args, **kwargs):
    print('MEU NEW')
    instancia = super().__new__(cls)
    return instancia
  
  def __init__(self, nome):
    print('MEU INIT')
    self.nome = nome
    
p1 = Pessoa('Vanessa')
