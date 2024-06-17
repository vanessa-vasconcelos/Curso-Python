'''
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista 
Não permita que o programa quebre com erros de índices inexistentes na lista
'''

lista = []

while True:
  print('Selecione uma opção: ')
  opcao = input('[i]nserir [a]pagar [l]istar: ')
    
  if opcao == 'i':
    produto = input('Qual o nome do produto? ')
    lista.append(produto)
  elif opcao == 'a':
    deletar = input('Qual índice deseja apagar? ')
    
    try:
      if deletar.isdigit:
        deletar_indice = int(deletar)
        del lista[deletar_indice]
    except IndexError:
      print('Não foi possível apagar esse índice')
    except ValueError: 
        print('Por favor, digite um número inteiro')
   
  elif opcao == 'l':
    for produtos in enumerate(lista):
      print(produtos)
  else:
    print('Por favor, escolha uma das três opções')
