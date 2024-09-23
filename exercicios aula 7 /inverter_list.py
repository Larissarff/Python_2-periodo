def main() :
    lenght_of_list = int(input("Digite o tamanho da lista que deseja: \n"))
    
    lista = []
    
    for i in range(lenght_of_list):
        num = int(input(f"Digite o {i+1}° numero da sua lista: \n"))
        lista.append(num)
    
    list_insert = [x for x in lista if x % 2 == 0]
    
    final_list = list_insert[::-1]

    print("A lista final, com números pares invertidos, é:", final_list) 
    
if __name__ == '__main__':
    main()
