'''
Formatação básica de strings 
s - string
d - int 
f - float
.<número de dígitos>f
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou - 
Ex: 0>-100,.1f
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.14789651223: .1f}')
print(f'{variavel!r}')