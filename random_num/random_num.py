import random

digito = random.randint(1, 100)
tentativas = 0

while True:
    usuario_input = int(input('Tente adivinhar o número (1-100): '))

    if not 1 <= usuario_input <= 100:
        print ('Número deve ser entre 0 e 100, tente novamente.\n')
        continue
    break
    

while usuario_input != digito:
    if usuario_input < digito:
        print ('Número é maior!') 
        tentativas += 1
    elif usuario_input > digito:
        print ('Número é menor!')
        tentativas += 1

    usuario_input = int(input('Tente novamente: '))

print (f'Você acertou. Quantidade de tentativas: {tentativas}')