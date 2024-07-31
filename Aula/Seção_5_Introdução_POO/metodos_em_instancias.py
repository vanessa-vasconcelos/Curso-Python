# Métodos em instância de classes Python
# Hard coded - É algo que foi escrito diretamente do código'
# Classes - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados 
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância. 


class Carro:
  def __init__(self, nome_veiculo='sei la'):
    #self.nome = alguma_coisa # Hard coded
    self.nome = nome_veiculo
    
  def acelerar(self):
    print(f'{self.nome} está acelerando...')
    
fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome_veiculo='Celta')
print(celta.nome)
celta.acelerar()