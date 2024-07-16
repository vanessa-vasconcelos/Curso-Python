# Módulos padrão do Python (import, from, as e *)
# inteiro - import nome_modulo
#Vantagens: você tem o namespace do módulo
#Desvantagens: nomes grandes

# import sys

# plataform = 'A minha'
# print(sys.platform)
# print(plataform)

# partes - from nome_modulo import object 1, object 2
# Vantagens: nomes pquenos
# Desvantagens: sem o namespace do módulo

# from sys import exit, platform

# print(platform)

#  alias 1 - import nome_modulo as apelido
# import sys as s

# sys= 'alguma coisa'
# print(s.platform)
# print(sys)

# alias 2 - from nome_modulo import object as apelido
# from sys import platform as pf, exit as ex

# print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da liguagem

#má pratica - from nome_modulo import *
from sys import *

print(platform)
exit()

# Vantagens: importa tudo do módulo
# Desvantagens: importa tudo do módulo