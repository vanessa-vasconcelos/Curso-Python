# Generator são geralemnte funções que sabem pausar em determinada ocasião
import sys

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000 ))

print(sys.getsizeof(lista)) # A lista está todo na memória
print(sys.getsizeof(generator)) # generator não, ele espera pedir um valor para enviar

print(next(generator))