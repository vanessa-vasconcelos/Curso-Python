class Pessoa:
  ano_atual = 2024
  
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
  def get_ano_nascimento(self):
    return Pessoa.ano_atual - self.idade
  
dados = {'nome': 'Vanessa', 'idade': 22}
p1 = Pessoa(**dados) # isso é a mesma coisa se fizesse como no exemplo abaixo
#p1 = Pessoa(nome='Vanessa', idade=22)

# p1.nome = 'EITA'
# print(p1.idade)

# O __dict__ é editável
# p1.__dict__['outra'] = 'coisa' # retorna no dicionário outra: coisa
# p1.__dict__['nome'] = 'EITA'
# del p1.__dict__['idade']
# print(p1.__dict__) # retornar um dicionário com os valores do meu objeto
# print(vars(p1)) # Vai retornar a mesma coisa que o __dict__
# print(p1.outra)
print(vars(p1))