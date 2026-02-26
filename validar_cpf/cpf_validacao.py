#multiplicaçao por pesos e soma (Valor 1)
def digito_um(digitos):
    soma = 0
    peso = 10
    for digito in digitos[:9]:
        soma += digito * peso
        peso -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto

#multiplicaçao por pesos e soma (Valor 2)
def digito_dois(digitos, v1):
    soma = 0
    peso = 11
    for digito in digitos[:10]:
        soma += digito * peso
        peso -= 1
    resto = soma % 11
    return 0 if resto < 2 else 11 - resto