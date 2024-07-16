# dir, hasattr e getattr 

# dir - vai mostra todos os nomes dentro de string
string = 'Luiz'
metodo = 'upper'
# print(string)

# hasattr - checa se umj determinado objeto tem determinado nome lá dentro
if hasattr(string, metodo):
  print('Existe Upper')
  print(getattr(string, metodo)())
else:
  print('Não existe o método', metodo)