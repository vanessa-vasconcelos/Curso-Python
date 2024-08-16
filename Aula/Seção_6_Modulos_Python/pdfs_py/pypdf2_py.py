# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2

from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdf'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS / 'R20230210.pdf'
PASTA_NOVA.mkdir(exist_ok=True) # Cria uma pasta nova

reader = PdfReader(RELATORIO_BACEN) # Ler o pdf

# Ele mostra quantas páginas tem o pdf
# print(len(reader.pages))

# for page in reader.pages:
#   print(page)
#   print()

page0 = reader.pages[0] # Consigo pegar a pagina 1 do pdf
imagem0 = page0.images[0]

# print(page0.extract_text())
# print(page0.images)
# with open(PASTA_NOVA / imagem0.name, 'wb') as imagem:
#   imagem.write(imagem0.data

# Cria um arquivo novo para cada página do pdf
for i, page in enumerate(reader.pages):
  writer = PdfWriter()
  with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as arquivo:
        writer.add_page(page)
        writer.write(arquivo)
        
files = [
  PASTA_NOVA / 'page1.pdf',
  PASTA_NOVA / 'page0.pdf',
]

merger = PdfMerger()
for file in files:
  merger.append(file)
  
merger.write(PASTA_NOVA / 'MERGED.pdf')
merger.close()