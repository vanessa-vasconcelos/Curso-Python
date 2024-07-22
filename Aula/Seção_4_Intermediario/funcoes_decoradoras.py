# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são usadas para fazer o Python usar as funções decoradas em outras funções.
# Decoradores são 'Syntax Sugar' (Açúcar sintática)

def criar_funcao(func):
  def interna(*args, **kwargs):
    print('vou te decorar')
    for arg in args:
      is_string(arg)
    resultado = func(*args, **kwargs)
    print('Ok, você agora foi decorada')
    return resultado
  return interna

@criar_funcao
def inverte_string(string):
  return string[::-1]

def is_string(param):
  if not isinstance(param, str):
    raise TypeError('param deve ser string')

# Isso pode ser feito com o @syntax_sugar
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123')

invertida = inverte_string('123')
print(invertida)