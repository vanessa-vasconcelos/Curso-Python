'''
Operação Ternária (condicional de uma linha)
<valor> if <condição> else <outro valor>
'''
digito = 10
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)