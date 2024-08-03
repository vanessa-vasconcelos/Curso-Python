# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e retornar o novo objeto. Por isso, new recebe cls.
# __new__ DEVE retornar o novo objeto
# __init__ é o método responsávelpot inicializar a instância. Por isso, init recebe self.
# __init__ NÃO DEVE retornar nada (None)
# Object é a super classe de uma classe 

class A:
  def __new__(cls, *args, **kwargs):
    print('Antes de criar a instancia')
    instance = super().__new__(cls) # com super new eu crio uma instancia dessa classe
    print('Depois')
    instance.x = 213
    return instance # essa instancia vira self no init de baixo
  
  def __init__(self, x):
    self.x = x
    print('Sou o init')
    
  def __repr__(self):
    return 'A()'
  
a = A()
print(a.x)
