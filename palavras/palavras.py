contador_long = 0
texto = input('Digite um texto: ') 

for i in texto.split():
    if len(i) > 10:
        contador_long += 1

print (f'Palavras longas encontradas: {contador_long}')