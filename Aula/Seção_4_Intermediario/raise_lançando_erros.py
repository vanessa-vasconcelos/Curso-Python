print(123)
#raise ValueError('Deu erro')

def nao_aceito_zero(d):
  if d == 0: 
    raise ZeroDivisionError('Você está tentando dividir por 0')

def deve_ser_int_ou_float(n):
  tipo_n = type(n)
  if not isinstance(n, (float, int)):
    raise TypeError(f'"{n}" deve ser int ou float.'
                    f'"{tipo_n}" enviado')
  return True

def divide(n, d):
  deve_ser_int_ou_float(n)
  deve_ser_int_ou_float(d)
  nao_aceito_zero (d)
  return n / d
  
print(divide(8,'0'))