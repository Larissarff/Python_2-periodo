# Crie uma função que receba uma lista de tuplas representando coordenadas (x, y) e retorne a tupla com a maior distância da origem (0, 0)

import math

def coordenada_mais_distante(coordenadas):
    # Função auxiliar para calcular a distância de uma coordenada (x, y) até a origem
    def distancia(coordenada):
        x, y = coordenada
        return math.sqrt(x**2 + y**2)
    
    # Retorna a coordenada com a maior distância da origem
    return max(coordenadas, key=distancia)

# Exemplo de uso
coordenadas = [(1, 2), (3, 4), (6, 8), (-7, -5)]
resultado = coordenada_mais_distante(coordenadas)

print(f"A coordenada mais distante é: {resultado}")
