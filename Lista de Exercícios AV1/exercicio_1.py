# Crie um programa que simule um jogo de adivinhação de palavras.
# O programa deve e
# escolher aleatoriamente uma palavra de uma lista predefinida e dar ao usuário um
# número limitado de tentativas para adivinhar. Após cada tentativa, o programa deve
# informar quais letras estão corretas e em posição correta, e quais estão corretas mas em
# posição errada. Implemente uma função para gerar dicas baseadas nas tentativas
# anteriores do usuário

import random

def main():
    """
    Função principal do jogo de adivinhação de palavras.
    """

    lista_de_palavras_possiveis = ("computação", "tecnologia", "CPU", "Processador", "computador", "software", "aplicativo", "programa", "")
    palavra_secreta = random.choice(lista_de_palavras_possiveis)
    tamanho_palavra = len(palavra_secreta)

    print("\tBem vindo ao jogo de adivinhação de palavras!")
    print("Deve fazer sua suposição de palavra escondida e será retornado se acertou e se não certou, quais letras acertou e em qual posição.\nUma dica, essa adivinhação é com o tema: Ciência da computação.\n Vamos lá!")

    tentativas = 6
    letras_corretas = []
    letras_erradas = []

    while tentativas > 0:
        print(f"Tentativas restantes: {tentativas}")
        palavra_do_usuario = input("Digite o seu palpite para a palavra misteriosa: \n").lower()

        if len(palavra_do_usuario) != tamanho_palavra:
            print("A palavra tem que ter o mesmo tamanho da palavra secreta!")
            continue

        dica = gerar_dica(palavra_secreta, palavra_do_usuario, letras_corretas, letras_erradas)
        print(dica)

        if palavra_do_usuario == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra secreta: {palavra_secreta}")
            break

        for i, letra in enumerate(palavra_do_usuario):
            if letra == palavra_secreta[i]:
                letras_corretas.append(letra)
            elif letra in palavra_secreta and letra not in letras_corretas:
                letras_erradas.append(letra)

        tentativas -= 1

    if tentativas == 0:
        print(f"Suas tentativas acabaram. A palavra secreta era: {palavra_secreta}")

def gerar_dica(palavra_secreta, palavra_do_usuario, letras_corretas, letras_erradas):
    """
    Gera uma dica com base nas tentativas anteriores.

    Args:
        palavra_secreta: A palavra secreta a ser adivinhada.
        palavra_do_usuario: O palpite do usuário.
        letras_corretas: Lista de letras corretas na posição correta.
        letras_erradas: Lista de letras corretas, mas na posição errada.

    Returns:
        Uma string com a dica.
    """

    dica = ""
    for i, letra in enumerate(palavra_do_usuario):
        if letra == palavra_secreta[i]:
            dica += letra
        elif letra in letras_corretas:
            dica += "_"  # Indica que a letra está na palavra, mas na posição errada
        elif letra in letras_erradas:
            dica += "!"  # Indica que a letra não está na palavra
        else:
            dica += "_"

    return dica

if __name__ == "__main__":
    main()
