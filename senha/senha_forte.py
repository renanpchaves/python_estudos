import random
import string

especiais_permitidos = "!@#$%&*"

#1 de cada garantido
maiuscula = random.choice(string.ascii_uppercase)
minuscula = random.choice(string.ascii_lowercase)
numero = random.choice(string.digits)
especiais = random.choice(especiais_permitidos)

#juntar na lista as variaveis
senha = [maiuscula, minuscula, numero, especiais]
todos_caracteres = string.ascii_letters + string.digits + especiais_permitidos

#loop pra pegar 1 de cada ate formar 8
for i in range(8):
    senha.append(random.choice(todos_caracteres))

random.shuffle(senha)
senha_final = ''.join(senha)
print(f'Senha forte: {senha_final}')