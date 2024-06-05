''' Operadores Lógicos
and - or - not
and - Todas as condiões precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão inteira será avaliado naquele valor.
São considerados falosy(até o momento)
0 0.0 False ''
Também existe o tipo None que é usado para representrar um não valor
''' 
# AND

entrada = input('[E]ntrar [S]air: ')
digite_senha = input('Senha: ')

senha_permitida = '123456'

'''
if entrada == 'E' and digite_senha == senha_permitida:
  print('Entrou')
else:
  print('Saiu')

  
Avaliação de curto circuito
print(True and True and True)
'''
# OR
'''
if (entrada == 'E' or entrada == 'e') and digite_senha == senha_permitida:
  print('Entrou')
else:
   print('Saiu')

Avaliação de curto circuito
print(True or False)
'''

# NOT

'''
Usado para inverter expressões
not True = False
not False = True

senha = input('Senha: ')

if not senha:
  print('Você não digitou nada')

Avaliação de curto circuito
print(not 0)
'''

