# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
from datetime import datetime
import string
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'random_python.txt'

locale.setlocale(locale.LC_ALL, '')

def converte_para_brl(numero: float) -> str:
  brl = locale.currency(numero, symbol=True, grouping=True)
  return brl

data = datetime(2024, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)

# print(json.dumps(dados, indent=2, ensure_ascii=False))


with open(CAMINHO_ARQUIVO, 'r') as arquivo:
  texto = arquivo.read()
  template = string.Template(texto)
  print(template.safe_substitute(dados))