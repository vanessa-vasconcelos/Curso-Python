nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

if nome and idade:
  print(f'Seu nome é {nome}')
  print(f'Seu nome invertido é {nome[::-1]}')

  if " " in nome:
    print('Seu nome contém espaços.')
  else:
    print('Seu nome não contém espaço')

  print(f'Seu nome tem {len(nome)} letras')
  print(f'A primeira letra do seu nome é {nome[0]}')
  print(f'A última letra do seu nome é {nome[-1]}')
else:
  print('Desculpa, você de8icou campos vazios')
