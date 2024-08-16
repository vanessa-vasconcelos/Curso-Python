from time import sleep
from threading import Thread
from threading import Lock

"""
Maneira 1 de se criar Threads

class MeuThread(Thread):
  def __init__(self, texto, tempo):
    self.texto = texto
    self.tempo = tempo
    
    super().__init__()
    
  def run(self):
    sleep(self.tempo)
    print(self.texto)
    

t1 = MeuThread('Thread 1', 2)
t1.start()

t2 = MeuThread('Thread 2', 4)
t2.start()

t3 = MeuThread('Thread 3', 6)
t3.start()

for i in range(10):
  print(i)
  sleep(1)

"""
"""
# Maneira 2 de se criar threads

def vai_demorar(texto, tempo):
  sleep(tempo)
  print(texto)
  
  
t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 1))
t2.start()

t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 3))
t3.start()

for i in range(20):
  print(i)
  sleep(.5)
"""

"""
def vai_demorar(texto, tempo):
  sleep(tempo)
  print(texto)
  
  
t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()

# Essa é uma forma de esperar a thread ser execultada para filanizar todo o programa
while t1.is_alive():
  print('Esperando a thread.')
  sleep(2)
  
"""

class Ingresso: 
  def __init__(self, estoque):
    self.estoque = estoque
    self.lock = Lock()
    
  def comprar(self, quantidade):
    self.lock.acquire()
    
    if self.estoque < quantidade:
      print('Não temos ingressos suficientes.')
      self.lock.release()
      return
    
    sleep(1)
    
    self.estoque -= quantidade
    print(f'Você comprou {quantidade} ingresso(s). Ainda temos {self.estoque}')
    
    self.lock.release()
    
    
if __name__ == '__main__':
  ingressos = Ingresso(20)
  
  for i in range(1, 10):
    t = Thread(target=ingressos.comprar, args=(i, ))
    t.start()
    
  print(ingressos.estoque)
    
 