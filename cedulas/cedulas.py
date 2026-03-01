cedulas = [100, 50, 20, 10, 5, 2]

while True:
    try: 
        saque = int(input('Digite o valor do saque: R$'))
        if saque <= 0:
            print('\nO valor deve ser positivo.\n')
        elif saque % 2 != 0:
            print ('\nO valor deve ser múltiplo de dois.\n')
        else:
            break
    
    except ValueError:
        print ('Digite apenas números!')

for i in cedulas:
    quantidade = saque // i

    if quantidade>0:
        print(f'{quantidade} cédulas de R$ {i}')

    saque = saque % i

print (f'\nSacando...')
if saque > 0:
    print(f'❌ Erro: Sobrou R$ {saque}')