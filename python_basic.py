print("**********************************")
print("Bem vindo ao Jogo de adivinhação")
print("**********************************")

numero_secreto = 10

chute = int(input("Digite seu chute: "))

print("Chute: ", chute)

acertou = numero_secreto == chute
maior = numero_secreto > chute


if acertou:
    print("Você acertou!")
else:
    if maior:
        print("Seu chute foi maior")
    else:
        print("Seu chute foi menor")