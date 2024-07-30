# Positional-Only Parameters (/) e Keyword-Only Arguments (*)
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# 🟢 Positional-only Parameters (/) - Tudo antes da barra deve
# ser ❗️APENAS❗️ posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# 🟢 Keyword-Only Arguments (*) - * sozinho ❗️NÃO SUGA❗️ valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# A barra vai impedir que na hora de passar os valores antes dele, passe eles nomeados
def soma(a, b, /, x, y):
  print(a + b)
  
soma(1, 2, 3, y = 3)

# Tudo que vem antes do * é Positional e o que vier depois de * é obrigatório que passe o valor 
# nomeado. O * não impedi de nomear valores antes dele. Para restringir, basta colocar a /
def soma(a, b, / , *, c):
  print(a + b + c)
  
soma(1, 2, c=3)