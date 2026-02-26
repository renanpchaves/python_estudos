import random

jokenpo = ['pedra', 'papel', 'tesoura']
aleatorio = random.choice(jokenpo)
player = input('Escolha: pedra, papel ou tesoura? \n').lower()

print(f'Você escolheu: {player}')
print(f'Computador escolheu: {aleatorio}')

# empatou
if player == aleatorio:
    print('Empate!')

# player ganha aqui
elif (player == 'pedra' and aleatorio == 'tesoura') or \
     (player == 'papel' and aleatorio == 'pedra') or \
     (player == 'tesoura' and aleatorio == 'papel'):
    print('Você ganhou!')

# perdeu tudo
else:
    print('Você perdeu!')