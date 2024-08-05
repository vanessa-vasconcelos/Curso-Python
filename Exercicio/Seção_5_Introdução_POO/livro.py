def adicionar_pref(metodo):
  def interno(self, *args, **kwargs):
    resultado = metodo(self, *args, **kwargs)
    return f'INFO: {resultado}'
  return interno

class Livro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor
  
  @adicionar_pref
  def mostrar_info(self):
    infos = f'Título: {self.titulo}, Autor: {self.autor}'
    return infos
  

livro1 = Livro('Como eu era antes de você', 'Collen Hoover')
livro2 = Livro('Carnificina', 'Emma Grey')

print(livro1.mostrar_info())
print(livro2.mostrar_info())