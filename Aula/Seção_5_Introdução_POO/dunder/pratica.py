# __neg__(self) - self
# __str__(self) - str
# __repr__(self) - str

class Ponto():
  def __init__(self, x, y, z='String'):
    self.x = x
    self.y = y
    self.z = z
    
  def __str__(self) -> str: # quer uma string do meu objeto
    return f'({self.x}, {self.y})'
    
  def __repr__(self) -> str: # comunicação com os desenvolvedores de como quero que esse objeto seja 
    #criado
    class_name = type(self).__name__
    return f'{class_name} (x = {self.x!r}, y = {self.y!r}, z = {self.z!r})'
    
p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))