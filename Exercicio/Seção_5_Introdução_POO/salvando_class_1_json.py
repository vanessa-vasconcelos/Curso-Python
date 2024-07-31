# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'Exercicio\Seção_5_Introdução_POO\salvando_classe.json'

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
p1 = Pessoa('Vanessa', 22) 
p2 = Pessoa('Helena', 14) 
p3 = Pessoa('Davi', 32) 

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump():
  with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    print('Fazendo dump')
    json.dump (bd, arquivo, ensure_ascii=False, indent=2)
    
if __name__ == '__main__':
  print('ELE é o __main__ do arquivo 1')
  fazer_dump()