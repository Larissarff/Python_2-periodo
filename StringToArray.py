#Escreva uma função para dividir uma string e convertê-la em um conjunto de palavras.

def string_to_array(texto_continuo):

    #Função slipt que mapeia com base em uma exigência, no caso, o espaço em branco
    palavras = texto_continuo.split()
    # Converte a lista de palavras em um conjunto para remover duplicatas e ter apenas palavras únicas
    conjunto_palavras = set(palavras)
    return conjunto_palavras

def main():
    texto = input("Insira seu texto contínuo e sera dividido em palavras: \n")
    resultado = string_to_array(texto)
    print(resultado)

if __name__ == "__main__":
    main()
