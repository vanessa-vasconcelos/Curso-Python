# Escopo da classe e de métodos da classe

class Animal:
  # Stributo de classe: nome = 'Leão'
  
  def __init__(self, nome):
    self.nome = nome # atributos de instância
    
    variavel = 'valor'
    print(variavel)
    
  def comendo(self, alimento):
    return f'{self.nome} está comendo {alimento}'
  
  def executar(self, *args, **kwargs):
    return self.comendo(*args, **kwargs)
  
leao = Animal(nome='Leão')
print(leao.nome)
print(leao.executar('maçã'))