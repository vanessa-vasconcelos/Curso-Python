from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
  nome: str
  sobrenome: str
  
  
if __name__ == '__main__':
  p1 = Pessoa('Vanessa', 'Vasconcelos')
  print(asdict(p1).keys()) # Convertendo a dataclasse em dicionário
  print(asdict(p1).values())
  print(asdict(p1).items())
  print(astuple(p1)[0]) # Convertendo a dataclasse em tupla