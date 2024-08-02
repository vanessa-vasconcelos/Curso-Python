# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

# O método getter é responsável por retornar o valor da propriedade quando ela é acessada. 
# PEGAR O VALOR
# O método setter, por sua vez, é usado para definir o valor da propriedade quando ela é modificada.
#DEFINIR O VALOR

class Caneta: 
  def __init__(self, cor):
    self._cor = cor # O _ significa que não se pode usar ele fora da classe, somente pode ser usado
    # e alterado dentro da classe
    
  
  @property # método não salva valor, ele executa funções
  def cor(self):
    print('ESTOU NO GETTER')
    return self._cor
  
  @cor.setter # o nome da property.setter -> o setter precisa receber um valor
  def cor(self, valor):
    # if valor == 'Rosa':
    #   raise ValueError('Não aceito essa cor')
    print('ESTOU NO SETTER')
    self._cor = valor
  

caneta = Caneta('Azul')
caneta.cor = 'Rosa'
# caneta._cor = 'Rosa'# método não salva valor, ele executa funções
#getter -> obter valor

print(caneta.cor)




############################
#getter
class Caneta: 
  def __init__(self, cor):
    self.cor_tinta = cor
    
    
  
  @property 
  def cor(self):
    print('Property')
    return self.cor_tinta

def mostrar(caneta):
  return caneta.cor

caneta = Caneta('Azul')
#getter -> obter valor
mostrar(caneta)