import abc

class Conta(abc.ABC):
  def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
    self.agencia = agencia
    self.conta = conta
    self.saldo = saldo
  
  @abc.abstractmethod # isso diz que qualquer conta pode sacar
  def sacar(self, valor: float) -> float: ...
  
  def depositar(self, valor: float) -> float:
    self.saldo += valor
    self.detalhes(f'(DEPÓSITO: {valor} reais)')
    return self.saldo
  
  def detalhes(self, msg: str = '') -> None:
    print(f'O saldo é {self.saldo:.2f} {msg}')
    print('- - - ')

  def __repr__(self): 
    class_name = type(self).__name__
    attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
    return f'{class_name} {attrs}'

class ContaPoupanca(Conta):
  def sacar(self, valor):
    valor_pos_saque = self.saldo - valor
    
    if valor_pos_saque >= 0:
      self.saldo -= valor
      self.detalhes(f'(SAQUE: {valor} reais)')
      return self.saldo
    
    print('Não foi possível sacar o valor desejado')
    self.detalhes(f'(SAQUE NEGADO: {valor} reais)')
    return self.saldo
    

class ContaCorrente(Conta):
  def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
    super().__init__(agencia, conta, saldo)
    self.limite = limite
  
  def sacar(self, valor: float) -> float:
    valor_pos_saque = self.saldo - valor
    limite_maximo = -self.limite
    
    if valor_pos_saque >= limite_maximo:
      self.saldo -= valor
      self.detalhes(f'(SAQUE: {valor} reais)')
      return self.saldo
    
    
    print('Não foi possível sacar o valor desejado')
    print(f'Seu limite é {-self.limite:.2f} reais')
    self.detalhes(f'(SAQUE NEGADO: {valor} reais)')
    return self.saldo
  
  def __repr__(self): 
      class_name = type(self).__name__
      attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, {self.limite!r})'
      return f'{class_name} {attrs}'

if __name__ == '__main__':
  cp1 = ContaPoupanca(111, 222)
  cp1.sacar(1)
  cp1.depositar(1)
  cp1.sacar(1)
  print('###')
  cc1 = ContaCorrente(245, 321, 0, 100)
  cc1.sacar(2)
  cc1.depositar(8)
  cc1.sacar(3)
  cc1.sacar(98)
  cc1.sacar(6)
  