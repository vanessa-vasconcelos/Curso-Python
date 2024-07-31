'''
Métodos de classe + factories (fábricas)
São métodos onde 'self' será 'cls', ou seja, ao invés de receber a instância no primeiro 
parâmetro, recebemos a própria classe.
'''

class Pessoa:
  ano = 2024
  
  def __init__(self, nome, idadde):
    self.nome = nome
    self.idade = idadde
    
  @classmethod # permite que a classe seja chamada, mas semprecisar passar nenhum valor
  def metodo_de_classe(cls): # ele recebe a própria classe como parâmetro
    # cls - é a mesma coisa que colocar Pessoa
    print('Hey')
    
  # factories methods = método que cria um novo objeto com alguma lógica
  @classmethod # permite que a classe seja chamada, mas semprecisar passar nenhum valor
  def criar_com_50_anos(cls, nome): # ele recebe a própria classe como parâmetro
    return cls(nome, 50)# cls - é a mesma coisa que colocar Pessoa()
    
  @classmethod
  def cria_sem_nome(cls, idade):
    return cls('Anônimo', idade)  
  
  
p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônimo', 17)
p4 = Pessoa.cria_sem_nome(23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()