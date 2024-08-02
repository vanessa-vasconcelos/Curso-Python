from abc import ABC, abstractmethod
 
class Notificacao(ABC): 
  def __init__(self, mensagem) -> None:
    self.mensagem = mensagem
    
  @abstractmethod
  def enviar(self) -> bool: ...
  
class NotificacaoEmail(Notificacao): 
  def enviar(self) -> bool:
    print('Email: enviando: ', self.mensagem)
    return True
    
    
class NotificacaoSms(Notificacao): 
  def enviar(self) -> bool:
    print('SMS: enviando: ', self.mensagem)
    return False
    
# A notificacao é polimorfico pq ele muda o objeto sem quebrar a aplicação
def notificar(notificacao: Notificacao): # o tipo de notificacao é a classe Notificacao
  notificacao_enviada = notificacao.enviar()
    
  if notificacao_enviada:
    print('Notificação enviada')
  else:
    print('Notificação não enviada')
      

notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificao_sms = NotificacaoSms('testando sms')
notificar(notificao_sms)