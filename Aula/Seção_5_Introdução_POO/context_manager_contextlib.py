# Context Manager com função - Criando e usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
  try:
    print('Abrindo arquivo')
    arquivo = open(caminho_arquivo, modo, encoding="utf_8_sig")
    yield arquivo
  # except Exception as e:
  #   print("Ocorreu erro", e)
  finally:
    print('Fechando o arquivo')
    arquivo.close()
   
with my_open('Aula\Seção_5_Introdução_POO\context_teste_contextlib.txt', 'w') as arquivo:
  arquivo.write('Linha 1 \n')
  arquivo.write('Linha 2 \n')
  arquivo.write('Linha 3 \n')
  arquivo.write('Linha 4 \n')
  arquivo.write('Linha 5 \n')
  print('WITH', arquivo)