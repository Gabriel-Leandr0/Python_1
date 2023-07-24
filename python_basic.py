print("**********************************")
print("Bem vindo ao Jogo de adivinhação")
print("**********************************")

total_tentativas = 5
numero_secreto = 10
atual_tentiva = 0

while total_tentativas > atual_tentiva:

    atual_tentiva += 1
    print(f"tentativa {atual_tentiva} de {total_tentativas}")
    chute = int(input("Digite seu chute: "))
    print("Chute: ", chute)
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