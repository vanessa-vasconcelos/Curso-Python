# D:\Bibliotecas\Area de Trabalho\Curso Python\teste_fotos
# caminho = 'D:\\Bibliotecas\\Area de Trabalho\\Curso Python\\teste_fotos'
import os

caminho = os.path.join('D:\Bibliotecas\Area de Trabalho\Curso Python\Aula\Seção_6_Modulos_Python\\teste_fotos')

# O listdir vai listar do diretorio
for pasta in os.listdir(caminho):
  caminho_completo_pasta = os.path.join(caminho, pasta)
  print(caminho_completo_pasta)
  if not os.path.isdir(caminho_completo_pasta):
    continue
  
  for imagem in os.listdir(caminho_completo_pasta):
    print(imagem)