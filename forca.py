def forca():
    print("jogo da forca")
    enforcou = False
    acertou = False
    palavra_secreta = "banana".upper()
    acertos = []
    while (not enforcou and not acertou):
        chute = input("Qual letra?").upper()
        index = 0

        for letra in palavra_secreta:
            if chute == letra:
                print(f"Letra {letra} Posição:{index}")
            index += 1
            if acertos == palavra_secreta:
                print("voce venceu")
                break


if __name__ == "__main__":
    forca()
