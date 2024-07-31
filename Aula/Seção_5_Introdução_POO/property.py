# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
# O property você pode chamar como se fosse um atributo
# EX: @property

  # class Retangulo:
  #   def __init__(self, largura, altura):
  #       self.largura = largura
  #       self.altura = altura
    
  #   def calcular_area(self):
  #       return self.largura * self.altura


  # retangulo = Retangulo(5, 3)
  # area = retangulo.calcular_area()
  # print(area)

# Com property ficaria assim
  # @property
  #   def area(self):
  #       return self.largura * self.altura


# retangulo = Retangulo(5, 3)
# print(retangulo.area)  # Saída: 15

# Agora, a chamada retangulo.area retorna o valor da área sem a necessidade de 
# chamarmos explicitamente o método.
# Com o property obtenho somente o valor do resultado, sem poder fazer alguma alteração

  

class Caneta: 
  def __init__(self, cor):
    self.cor_tinta = cor
    
    
  
  @property # Um m[etodo que se comporta como atributo
  def cor(self):
    print('Property')
    return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)





####################################################################
# class Caneta: 
#   def __init__(self, cor):
#     self.cor_tinta = cor
    
#   # Faz um método onde o nome do atributo acima pode mudar, mas para o cliente não dá erro, pois
#   # o cliente está chamando o método
#   def get_cor(self):
#     print('GET COR')
#     return self.cor_tinta
  

# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())