from dataclasses import dataclass


@dataclass(init=False) # Com isso, ele n cria um init, eu mesma tenho que criar um init na classe
class Pessoa:
  nome: str
  sobrenome: str
  
  def __init__(self, nome, sobrenome):
    self.nome = nome
    self.sobrenome = sobrenome
    self.nome_completo = f'{self.nome} {self.sobrenome}'
  
  def __post_init__(self):
    print('POST INIT')
    # self.nome_completo = f'{self.nome} {self.sobrenome}'
  
  # @property
  # def nome_completo(self):
  #   return f'{self.nome} {self.sobrenome}'
  
  # @nome_completo.setter
  # def nome_completo(self, valor):
  #   nome, *sobrenome = valor.split()
  #   self.nome = nome
  #   self.sobrenome = ' '.join(sobrenome)
  
if __name__ == '__main__':
  p1 = Pessoa('Vanessa', 'Vasconcelos')
  # p1.nome_completo = 'Maria Helena Barras'
  print(p1)
  print(p1.nome_completo)