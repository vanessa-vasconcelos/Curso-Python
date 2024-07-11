'''
Higher Order Functions
Funções de primeira classe 
'''

def saudacao(msg, nome):
  return f'{msg}, {nome}'

def executa(funcao, *args):
  return funcao(*args)

# print(saudacao('Bom dia'))

v = executa(saudacao, 'Bom dia', 'Vanessa')
print(v)

print(executa(saudacao, 'Bom dia', 'Catarina'))