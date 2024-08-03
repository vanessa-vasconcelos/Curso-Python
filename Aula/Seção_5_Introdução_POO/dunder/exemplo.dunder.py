class Ponto():
  def __init__(self, x, y, z='String'):
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self) -> str: 
    class_name = type(self).__name__
    return f'{class_name} (x = {self.x!r}, y = {self.y!r}, z = {self.z!r})'
  
  def __add__(self, other):
    novo_x = self.x + other.x
    novo_y = self.y + other.y
    return Ponto(novo_x, novo_y)
  
  def __gt__(self, other):
    resultado_self = self.x + self.y
    resultado_other = other.x + other.y
    return resultado_self > resultado_other
 
if __name__ == '__main__': 
  p1 = Ponto(4, 2)
  p2 = Ponto(6, 4)
  p3 = p1 + p2 # Quando faz isso, vai ser chamada a função __add__, e p3 vai ser o que add devolver
  print(p3)
  print('P1 é maior que P2', p1 > p2)
  print('P2 é maior que P1', p2 > p1)