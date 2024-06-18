'''
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
'''

# def Print():
#   print('Vanrias')
#   print('Vanrias')
#   print('Vanrias')
#   print('Vanrias')
  
# Print()

def imprimir(a, b, c):
 print(a, b, c)
    
imprimir(1, 2, 3)
imprimir(4, 5, 6)

def saudacao(nome):
  print(f'Olá, {nome}')
  
saudacao('Luiz')
saudacao('Vanessa')

# Pode definir um valor caso a pessoa não passe nada nos parâmetros
def comprimento(nome='Sem nome'):
  print(f'Olá, {nome}')
  
comprimento()
comprimento('Vanessa')