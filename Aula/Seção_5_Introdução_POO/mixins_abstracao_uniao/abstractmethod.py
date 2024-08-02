from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    # @abstractmethod
    def name(self):
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name): ...


class Foo(AbstractFoo):
  # name = ''
  
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

      # Isso é a mesma coisa de eu fazer name = ''
  # @property
  # def name(self): 
  #   return self._name
  
  # @name.setter
  # def name(self, name):
  #   self._name = name  
  
  
foo = Foo('Bar')
print(foo.name)