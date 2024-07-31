# Atributos de classe


class Pessoa:
  ano_atual = 2024
  
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
  def get_ano_nascimento(self):
    return Pessoa.ano_atual - self.idade
  
p1 = Pessoa('Vanessa', 22)
p2 = Pessoa('Luiza', 17)

print(Pessoa.ano_atual)
#Pessoa.ano_atual = 1 # Quando o valor é alterado, ele altera o resultado final também

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())