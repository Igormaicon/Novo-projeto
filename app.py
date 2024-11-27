import random

def escolher_palavra():
    palavras = ['python', 'programação', 'computador', 'algoritmo']
    palavra_secreta = random.choice(palavras)
    return palavra_secreta

def iniciar_jogo(palavra_secreta):
    letras_acertadas = ['_' for letra in palavra_secreta]
    letras_usadas = []
    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        print(letras_acertadas)
        chute = input("Digite uma letra: ").strip().lower()

        if chute in letras_usadas:
            print("Você já chutou essa letra antes!")
            continue

        letras_usadas.append(chute)

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            print("Você errou!")

        enforcou = "_" not in letras_acertadas
        acertou = set(letras_acertadas) == set(palavra_secreta)

    if acertou:
        print("Parabéns, você ganhou!")
    else:
        print("Você foi enforcado!")
        print(f"A palavra era {palavra_secreta}")

palavra_secreta = escolher_palavra()
iniciar_jogo(palavra_secreta)
