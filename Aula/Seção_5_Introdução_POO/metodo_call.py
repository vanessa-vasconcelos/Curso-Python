# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".


class CallMe: 
  def __init__(self, phone):
    self.phone = phone
    
  # O call faz a instância, o objeto da classe ser executável
  def __call__(self, nome):
    print(nome, 'está chamando', self.phone)
    return 123
    
call1 = CallMe('388541235')
retorno = call1('Vanessa') # Esse é a instância, o objeto
print(retorno)