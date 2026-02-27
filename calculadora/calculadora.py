resultado = 0

while True:
    try:
        primeiro = int(input ('Escolha o primeiro número: '))
        operati = (input ('Escolha a operação (+, -, *, /): '))
        segundo = int(input ('Escolha o segundo número: '))

        if operati == '+':
            resultado = primeiro + segundo
        elif operati == '-':
            resultado = primeiro - segundo
        elif operati == '*':
            resultado = primeiro * segundo
        elif operati == '/':
            if segundo == 0:
                print ('Divisão por 0, revalidar.')
                continue
            resultado = primeiro / segundo
        else:
            print ('Operação inválida, tente novamente.\n')
            continue

        print (f'Resultado: {resultado}\n')
        break
        
    except ValueError:
        print ('Operação inválida, tente novamente: ')