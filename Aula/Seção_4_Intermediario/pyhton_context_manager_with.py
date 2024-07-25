import os
'''
Criando arquivos com Python
Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)
Modos:
  r (leitura), w (escrita), x (para criação), a (escreve ao final), b (binário), t (modo texto),
  + (leitura e escrita)
Context Manager - with (abre e fecha)
Métodos úteis:
whrite, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
Vamos falar mais sobre o módulo os, mas: 
os.remove ou unlink - apaga o arquivo
Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load
'''


caminho_arquivo =  'Aula\\Seção_4_Intermediario\\Teste_Aula_Python_Context\\'
caminho_arquivo += 'arquivo_teste_caminho.txt'

# arquivo = open(caminho_arquivo, 'w') # Abrindo o arquivo 

# arquivo.close() # Fechando o arquivo

# A diferença do código acima do de baixo, é que o de baixo vai fecha automaticamente
# with open(caminho_arquivo, 'w+') as arquivo:
#   arquivo.write('Linha 1\n')
#   arquivo.write('Linha 2\n')
#   arquivo.writelines(
#     ('Linha 3\n', 'Linha 4\n')
#   )
#   arquivo.seek(0, 0)
#   print(arquivo.read())
#   print('Lendo')
#   arquivo.seek(0, 0)
#   print(arquivo.readline(), end='')
#   # strip elimina todos os espaços
#   print(arquivo.readline().strip())
#   print(arquivo.readline().strip())
#   print('READLINES')
#   for linha in arquivo.readlines():
#     print(linha.strip())
  
  
  
# print('#' * 40)

# with open(caminho_arquivo, 'r') as arquivo:
#   print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf-8-sig') as arquivo:
  # Para utilizar caracteres especiais, basta clicar em UTF-8, depois Reopen with Encoding e
  #selecionar o Windows 1252
  arquivo.write('Atenção\n')
  arquivo.write('Linha 2\n')
  arquivo.writelines(
    ('Linha 3\n', 'Linha 4\n')
  )
  
# os.remove ou os.unlink() faz a mesma coisa
#os.unlink(caminho_arquivo)
#os.rename(caminho_arquivo, 'aula116.txt') # renomea o caminho do arquivo
