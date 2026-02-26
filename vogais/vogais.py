texto = input('Digite um texto: ')
vogais = 'aeiouAEIOU'
contador = 0

for i in texto:
    if i in vogais:
        contador += 1

vogais_print = print (f'A saída contém {contador} vogais.')