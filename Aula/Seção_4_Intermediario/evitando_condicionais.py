import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print( )
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)


tarefas = []
tarefas_refazer = []

while True:
  print('Comandos: listar, desfazer e refazer')
  tarefa = input('Digite uma tarefa ou comando: ')

  # Quando chamo o dicionário ele já executa todos e retorna None, preciso adiar o retorno de cada
  comandos= {
    'listar': lambda: listar(tarefas), # A lambda adia pq ela que está sendo retornada e não minha
    # execução
    'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
    'refazer': lambda: refazer(tarefas, tarefas_refazer),
    'clear': lambda: os.system(' '),
    'adicionar': lambda: adicionar(tarefa, tarefas),
  }

  comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else comandos['adicionar']
  comando()














  # if tarefa == 'listar':
  #   listar(tarefas)
  #   continue
  # elif tarefa == 'desfazer':
  #   desfazer(tarefas, tarefas_refazer)
  #   listar(tarefas)
  #   continue
  # elif tarefa == 'refazer':
  #   refazer(tarefas, tarefas_refazer)
  #   listar(tarefas)
  #   continue
  # elif tarefa == 'clear':
  #   os.system('clear')
  #   continue
  # else:
  #   adicionar(tarefa, tarefas)
  #   listar(tarefas)
  #   continue
  
  
  