 # Abstração 
 # Herança - É um
 
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
  def _log(self, msg):
    raise NotImplementedError('Implemente o método log')
  
  def log_error(self, msg):
    return self._log(f'Error: {msg}')
  
  def log_success(self, msg):
    return self._log(f'Success: {msg}')

class LogFilemixin(Log):
  def _log(self, msg):
    msg_formatada = f'{msg} ({self.__class__.__name__})'
    print('Salvando no log: ', msg)
    with open(LOG_FILE, 'a', encoding='utf_8_sig') as arquivo:
      arquivo.write(msg_formatada)
      arquivo.write('\n')
  
class LogPrintmixin(Log):
  def _log(self, msg):
    print(f'{msg} ({self.__class__.__name__})')
  
  
if __name__ == '__main__':  
  lp = LogPrintmixin()
  lp.log_error('qualquer coisa')
  lp.log_success('Que legal')
  
  
  ls = LogFilemixin()
  ls.log_error('qualquer coisa')
  ls.log_success('Que legal')
  