'''
Imprecisão de ponto flutuante
'''

import decimal

numero_01 = decimal.Decimal('0.1')
numero_02 = decimal.Decimal('0.7')
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)
print(f'{numero_3:.2f}')
# ROUND ÉPARA ARREDONDAR UM NÚMERO, PRIMEIRO PASSA O NÚMERO E DEPOIS A QUANTIDADE DE CASAS DECIMAIS QUE DESEJA
print(round(numero_3, 3))
