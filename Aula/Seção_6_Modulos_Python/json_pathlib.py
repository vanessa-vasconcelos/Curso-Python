# Usamos a pathlib para trabalhar com caminhos, pastas e arquivos de forma que um código funcione 
# em Linux, Windows e Mac
# Hard Coding é uma prática não recomendada de utilizar valores fixos no código fonte da aplicação
from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias / 'arquivo.txt')

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch() # Salva o arquivo na memória / pc
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