"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""
import re

# O .replace('o caractere que deseja trocar', 'pelo o que deseja trocar') você pode substituir algo no valor que você desejar
#cpf_enviado_usuario = '321.756.780-32'.replace('.', '').replace('-', '')
entrada = input('Digite o CPF: ')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)
cpf_correto = '32175678032'

# Penúltimo número
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 11

resultado_digito_1 = 0
for numero in nove_digitos:
  contador_regressivo_1 -= 1 
  resultado_digito_1 += int(numero) * contador_regressivo_1
  
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
  
# Último número
cpf_dez_digitos = nove_digitos + str(digito_1)

contador_regressivo_2 = 12

resultado_digito_2 = 0
for numero_2 in cpf_dez_digitos:
  contador_regressivo_2 -= 1
  resultado_digito_2 += int(numero_2) * contador_regressivo_2
  
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# CPF verificado
digito_2_str = str(digito_2)
cpf_verificado = cpf_dez_digitos + digito_2_str

if cpf_verificado == cpf_correto:
  print('CPF válido.')
else:
  print('CPF inválido')