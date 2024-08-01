# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
  def __init__(self, nome):
    self.nome = nome
    self._ferramenta = None
    
  @property
  def ferramenta(self):
    return self._ferramenta
  
  @ferramenta.setter
  def ferramenta(self, ferramenta):
    self._ferramenta = ferramenta
    

class FerramentaDeEscrever:
  def __init__(self, nome):
    self.nome = nome
    
  @property
  def escrever(self):
    return f'{self.nome} está escrevendo'
  

escritor = Escritor('Vanessa')
maquina_de_escrever = FerramentaDeEscrever('Digitadora')
escritor.ferramenta = maquina_de_escrever # Aqui está associando a classe Escritor.função ferramenta
# com a classe FerramentaDeEscrever
print(escritor.ferramenta.escrever)