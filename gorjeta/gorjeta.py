conta = float(input('Digite o valor da conta: '))
prc_gorjeta = int(input('Digite a porcentagem da gorjeta (ex: 10): '))

valor_gorjeta = conta * (prc_gorjeta / 100)
total_pagar = (conta+valor_gorjeta)

print (f'\nA porcentagem da gorjeta digitada foi: {prc_gorjeta}%')
print (f'O total a pagar é: {total_pagar:.2f}')