import os

tarefas = []

def terminar():
    print('=== VOCÊ SAIU DO SISTEMA === \n')

def to_menu():
    input ('\nAperte uma tecla para voltar ao menu.')

def header(text):
    os.system('cls')
    lines = '*' * (len(text))
    print (lines)
    print(text)
    print (lines)
    print()

def options():
    header('=== ESCOLHA UMA DAS OPÇÕES ===')
    print ('1. Adicionar tarefa')
    print ('2. Visualizar tarefas')
    print ('3. Remover tarefas')
    print ('4. Sair')
    
def adicionar():
    header('=== ADICIONAR TAREFA ===')
    tarefa = input('Digite a tarefa: ')
    print('Tarefa adicionada!')
    tarefas.append(tarefa)
    to_menu()

def visualizar(mostrar_menu=True):
    header('=== VISUALIZANDO TAREFAS ===')
    if not tarefas:
        print('Nenhuma tarefa encontrada.')
    else:
        for indice, tarefa in enumerate(tarefas):
            print(f'{indice+1}. {tarefa}')

    if mostrar_menu:
        to_menu()

def remover():
    if not tarefas:
        print('Nenhuma tarefa para remover!')
        to_menu()
        return
    
    header('=== REMOVER TAREFA ===')
    visualizar(mostrar_menu=False)
    
    numero = int(input('\nDigite o número da tarefa que deseja remover: '))
    tarefas.pop(numero - 1)
    print('Tarefa removida.')
    to_menu()

def selecao(escolha):
    print('=== ESCOLHA A SUA OPÇÃO: ===')
    if escolha in ['1', '2', '3', '4']:
        if escolha == '1':
            adicionar()
        elif escolha == '2':
            visualizar()
        elif escolha == '3':
            remover()
        elif escolha == '4':
            terminar()
            return True
    else:
        print('Opção inválida! Escolha entre 1 e 4')
        to_menu()
    return False

def main():
    while True:
        os.system('cls')
        options()

        escolha = input ('\n Digite a opção (1-4): ')
        sair = selecao(escolha)

        if sair:
            break

if __name__ == '__main__':
    main()