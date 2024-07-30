class Pessoa:
  # quando é dentro de uma classe é chamado de método
  def __init__(self, nome, sobrenome): # o primeiro parametro é necessário reservar para a classe 
    #"self". É como se a classe self fosse o p1 ou p2
   self.nome = nome # Isso aqui é a mesma coisa disso aqui: p1.nome = 'Vanessa'
   self.sobrenome = sobrenome
  
p1 = Pessoa('Vanessa', 'Vaconcelos')
# p1.nome = 'Vanessa'
# p1.sobrenome = 'Vaconcelos'

p2 = Pessoa('Marta', 'Santos')
# p2.nome = 'Marta'
# p2.sobrenome = 'Santos'

# Como quero acessar o valor de nome não utiliza ()
print(p2.nome)
print(p2.sobrenome)
 
print(p1.nome)
print(p1.sobrenome)