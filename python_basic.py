from random import randrange

print("**********************************")
print("Bem vindo ao Jogo de adivinhação")
print("**********************************")

total_tentativas = 5
numero_secreto = randrange(1, 10)
print(numero_secreto)
atual_tentiva = 0

for atual_tentiva in range(1, total_tentativas + 1):

    print(f"tentativa {atual_tentiva} de {total_tentativas}")
    chute = int(input("Digite seu chute: "))
    print("Chute: ", chute)

    if (chute < 1) or (chute > 100):
        print("Digite um número entre 1 e 100:")
        continue

    acertou = numero_secreto == chute
    maior = numero_secreto < chute

    if acertou:
        print("Você acertou!")
        break

    else:
        if maior:
            print("Seu chute foi maior")
        else:
            print("Seu chute foi menor")

print("Game Over ☠")
