# Qual letra aparece mais vezes na frase

frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum'

i = 0
qtd_apareceu_mais_vezes = 0
letra_queapareceu_mais_vezes = ''
while i < len(frase):
  letra_atual = frase[i]
  
  if letra_atual == ' ':
    i += 1
    continue
  
  quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)
  
  if qtd_apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
    qtd_apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
    letra_queapareceu_mais_vezes = letra_atual
    

  
print('A letra que apareceu mais vezez foi'f'{letra_queapareceu_mais_vezes} que apareceu {qtd_apareceu_mais_vezes}x')
