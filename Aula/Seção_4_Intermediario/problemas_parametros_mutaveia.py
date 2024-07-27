# Problema dos parâmetros mutáveis em funções Python

def adiciona_clientes(nome, lista=None):
  if lista is None:
    lista = []
  lista.append(nome)
  return lista


cliente = adiciona_clientes('vanessa')
adiciona_clientes('Joana', cliente)
adiciona_clientes('Fernando', cliente)
cliente.append('Edu')
print(cliente)

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('marcos', cliente2)
print(cliente2)

cliente3 = adiciona_clientes('Fernando')
adiciona_clientes('Carlos', cliente3)
print(cliente3)