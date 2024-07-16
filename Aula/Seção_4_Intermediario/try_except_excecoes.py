# Try, except, else e finally

try: 
  a = 18
  b = 0
  #print(b[0])
  print('Linha 1'[1000])
  c = a / b
  print('Linha 2 ')
except ZeroDivisionError:
  print('Dividiu por zero.')
except NameError:
  print('Nome b não está definido.')
except (TypeError, IndexError) as error:
  print('TypeError + IndexError')
  print('MSG:', error)
  print('Nome:', error.__class__.__name__)
except Exception:
  print('Erro Desconhecido')


print('Continuar')


# Finally sempre será executado, mesmo se houver ou não um erro

try: 
  print('Abrir arquivo')
  # 8/0
except ZeroDivisionError:
  print('Dividiu 0')
else:
  print('Não deu erro')
finally:
  print('Fechar arquivo')