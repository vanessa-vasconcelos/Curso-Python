# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# FOO - Bar são palavras usadas como placeholder para palavras que podem mudar na programação
#Classes abstradas:são apenas um tipo abstrato  de como as classes que a herdarem devem se comportar.
from abc import ABC, abstractmethod

#class Log(metaclass=ABCMeta)
# Tanto o início de cima quanto o início de baixo são a mesma coisa
class Log(ABC):  
  @abstractmethod # Isso significa que a classe Log não pode ser usada diretamente
  def _log(self, msg): ...
  
  def log_error(self, msg):
    return self._log(f'Error: {msg}')
  
  def log_success(self, msg):
    return self._log(f'Success: {msg}')
  
class LogPrintmixin(Log):
  def _log(self, msg): # É obrigatório implementar esté método, pq o log é abstrato
    print(f'{msg} ({self.__class__.__name__})')
    
l = LogPrintmixin()
l.log_error('Oi')