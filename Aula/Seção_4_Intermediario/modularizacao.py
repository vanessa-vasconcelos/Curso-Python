# Entendendo os seus próprios módulos Python 
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

# Importa somente uma vez, então são singontons
# import sys
# import importlib
# import modularizacao_m
# from modularizacao_m import variavel, soma

# sys.path.append('/home')

# print('Este módulo se chama', __name__)
# print(modularizacao_m.variavel)
# print(soma(2, 3))
# print(modularizacao_m.soma(2, 3))

from aula_package import soma


print(soma(2,3))