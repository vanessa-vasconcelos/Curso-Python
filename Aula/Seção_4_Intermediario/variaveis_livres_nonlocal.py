# Variavel livre + nonlocal (locals, globals)

# print(globals())
# def fora(x):
#   a = x
  
#   def dentro():
#     print(locals())
#     return a
#   return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
  valor_final = string_inicial
  
  def interna(valor_a_concatenar=""):
    # Como valor_final não é dessa função, não é possível alterar ele, 
    # somente fazer a leitura da variável, para que a alteração seja possível basta informar
    # antes que a variável não é nem local e nem global, mas sim nonlocal
    nonlocal valor_final
    valor_final += valor_a_concatenar
    return valor_final
  return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
print(c('e'))