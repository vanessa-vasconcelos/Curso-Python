from dataclasses import dataclass, field, fields

@dataclass
class Pessoa:
  nome: str = field(default='Missing')
  sobrenome: str = 'Not sent'
  idade: int = 100
  enderecos: list[str] = field(default_factory=list)
  
  
if __name__ == '__main__':
  p1 = Pessoa()
  print(fields(p1))
  print(p1)