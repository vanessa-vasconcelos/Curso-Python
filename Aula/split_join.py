'''
split e join com list e str
split - divide uma string
join - une uma str
'''

frase = ' Olha só que, coisa interessante'
lista_palavras = frase.split(',')

lista_frase = []
for i, frase in enumerate(lista_palavras):
  # strip = corta os espaços do comço e do fim da minha str
 # print(lista_palavras[i].strip())
 lista_frase.append(lista_palavras[i].strip())

print(lista_palavras)
print(lista_frase)

# JOIN
frases_unidas = '-'.join(lista_frase)
print(frases_unidas)