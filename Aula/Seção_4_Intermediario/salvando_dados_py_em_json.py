import json

# pessoa = {
#   "nome": "Luiz Otávio 2",
#   "sobrenome": "Miranda",
#   "enderecos": [
#     {
#       "rua": "R1","numero": 32},
#     {
#       "rua": "R2","numero": 55}
#   ],
#   "altura": 1.8,
#   "numeros_preferidos": (
#     2,
#     4,
#     6,
#     8,
#     10
#   ),
#   "dev": True,
#   "nada": None
# }

# with open('salvando_dados_json.json', 'w', encoding='utf-8-sig') as arquivo:
#   # faz dump no arquivo e dumps realiza o dump na string
#   json.dump(
#     pessoa,
#     arquivo, 
#     ensure_ascii=False, # esse do final, faz com que no doc json os caracteres saem certinho,
#   # mas é recomendado não colocar isso
#     indent=2, # ele vai deixar o dicionário formatado
#     ) 

with open('salvando_dados_json.json', 'r') as arquivo:
  # é para carregar uma string
  pessoa = json.load(arquivo)
  print(pessoa)
  print(type(pessoa))