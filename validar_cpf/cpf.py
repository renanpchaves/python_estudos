from cpf_validacao import digito_um, digito_dois

cpf_inpt = (input('Digite seu CPF (ex: 33001680075): ').strip())

#validaçao input
if len(cpf_inpt) != 11:
    print('Inválido! Deve ter 11 dígitos.')
    raise SystemExit
elif not cpf_inpt.isdigit():
    print('Registros devem ser apenas números.')
    raise SystemExit
elif cpf_inpt == cpf_inpt[0] * 11:
    print('Inválido! CPF com digitos iguais.')
    raise SystemExit

digitos = [int(d) for d in cpf_inpt]

v1 = digito_um(digitos)
v2 = digito_dois(digitos, v1)

if v1 == digitos[9] and v2 == digitos[10]:
    print ('CPF válido!')
else:
    print ('CPF inválido!')