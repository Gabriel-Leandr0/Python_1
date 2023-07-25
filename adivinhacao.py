from random import randrange


def adivinhacao():
    print("**********************************")
    print("Bem vindo ao Jogo de adivinhação")
    print("**********************************")

    numero_secreto = randrange(1, 101)
    print(numero_secreto)
    atual_tentiva = 0
    pontos = 1000

    print("Defina o nível de dificuldade: ")
    nivel = int(input("(1) Fácil (2) Médio (3) Difícil"))

    if nivel == 1:
        total_tentativas = 10
    elif nivel == 2:
        total_tentativas = 5
    else:
        total_tentativas = 3

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
                print("Seu chute foi maior ⬆️")
            else:
                print("Seu chute foi menor ⬇️")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

    print("Pontos: ", pontos)
    print("Game Over ☠")
