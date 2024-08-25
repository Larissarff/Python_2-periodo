def restoNumero(numero: int) -> str:
    if numero % 2 == 0:
        return 'é par'
    else:
        return 'é impar'


def main()-> None:

    numero = (int(input("Digite um numero: ")))

    if numero >= 0:
        resultado = restoNumero(numero)
        print(f"O numero {numero} é {resultado}")

    else:
        print("Numero inválido para análise!")

if __name__ == '__main__':
    main()
