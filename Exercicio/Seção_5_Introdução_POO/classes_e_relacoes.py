"""
Exercício com classes
1 - Crie uma classe Carro (Nome)
2 - Crie uma classe Motor (Nome)
3 - Crie uma classe Fabricante (Nome)
4 - Faça ligação entre Carro tem um Motor
OBS: Um motor pode ser de vários carros , mas um carro só tem um motor
5 - Faça a ligação entre Carro e um Fabricante
OBS: Um fabricante pode fabricar vários carros, mas um carro só pode ter um fabricante
Exiba o nome do carro, motor e fabricante na tela
"""

class Carro:
  def __init__(self, nome):
    self.nome = nome
    self._motor = None
    self._fabricante = None
    
  @property
  def motor(self):
    return self._motor  
  
  @motor.setter
  def motor(self, valor):
    self._motor = valor
  
  @property
  def fabricante(self):
    return self._fabricante  
  
  @fabricante.setter
  def fabricante(self, valor):
    self._fabricante  = valor
  
class Motor:
  def __init__(self, nome):
    self.nome = nome
    
class Fabricante:
  def __init__(self, nome):
    self.nome = nome
    
fusca = Carro('Fusca')
volkswagen = Fabricante('volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)
    
fiat_uno = Carro('fiat Uno')
fiat = Fabricante('fiat')
motor_1_0 = Motor('1.0')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)