nome = 'Vanessa'

indice = 0
nova_string = ' '
while indice < len(nome):
  letra = nome[indice]
  nova_string += letra + '*'
  indice += 1

print(nova_string)