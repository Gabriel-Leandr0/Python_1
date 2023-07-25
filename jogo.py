from forca import forca
from adivinhacao import adivinhacao

print("Escolha seu jogo")
jogo = int(input("(1) Forca (2) Adivinhacao"))

if jogo == 1:
    forca()
else:
    adivinhacao()
