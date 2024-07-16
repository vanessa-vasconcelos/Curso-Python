# Dictionary Comprehension e Set Comprehension

# Dictionary 
produto = { 
  'nome': 'Caneta Azul', 
  'preco': 2.5, 
  'categoria': 'Escritório'        
} 

dc = {
  chave: valor.upper()
  if isinstance(valor, str) else valor
  for chave, valor in produto.items()
  if chave != 'categoria'
}
 
print(dict(dc))

# Set Comprehension
# Não gera chave, somente valores

s1 = {2 ** i for i in range(10)}
print(s1)
