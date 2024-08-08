from dataclasses import dataclass

#frozen=True - deixa a dataclasse congelada, sem poder alterar nada nele
#repr=False - desativa o repr da dataclass
# order=True - ele ordena seus dados na ordem

@dataclass(order=True) 
class Pessoa:
  nome: str
  sobrenome: str
  
  
if __name__ == '__main__':
  lista = [Pessoa('A', 'Z'), Pessoa('B', 'Y'),Pessoa('C', 'X')]
  ordenadas = sorted(lista, reverse=False, key=lambda p: p.sobrenome) # aqui definil a própria ordem
  print(ordenadas)