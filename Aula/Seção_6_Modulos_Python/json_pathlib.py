# Usamos a pathlib para trabalhar com caminhos, pastas e arquivos de forma que um código funcione 
# em Linux, Windows e Mac
# Hard Coding é uma prática não recomendada de utilizar valores fixos no código fonte da aplicação
from pathlib import Path
from shutil import rmtree

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch() # Salva o arquivo na memória / pc
caminho_arquivo.write_text("Olá Mundo")
caminho_arquivo.unlink()

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True) # Cria um diretório
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo.touch()
outro_arquivo.write_text('Hey')

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
  file = files / f'file_{i}.txt'
  file.touch()

  if file.exists():
    file.unlink()
  else: 
    file.touch()
    
  with file.open('a+') as text_file:
    text_file.write('Olá Mundo \n')
    text_file.write(f'file_{i}.txt')
  
def rmtree(root: Path, remove_root=True):
  for file in root.glob('*'):
    if file.is_dir():
      rmtree(file, False)
      file.rmdir()
    else:
      print('FILE: ', file)
      file.unlink()
      
  if remove_root: 
    root.rmdir()
  
rmtree(caminho_pasta)


# print(arquivo)
# arquivo.write_text("Olá Mundo")
# arquivo.write_text("Olá Mundo de novo")
# print(arquivo.read_text())
#arquivo.unlink() # apaga o arquivo 
# caminho_arquivo.write_text('')
# with caminho_arquivo.open('a+') as file:
#   file.write('Uma linha \n')
#   file.write('Uma linha \n')
  
# print(caminho_arquivo.read_text())