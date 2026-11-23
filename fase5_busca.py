# fase 5: busca A* com while
from mapa import mapa_romenia, heuristica_bucareste


def busca_a_estrela(inicio, objetivo):
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira.pop(0)

        # testa o objetivo ao tirar da fronteira, não ao gerar o nó
        if cidade == objetivo:
            return caminho, g

        if cidade in explorados:
            continue
        explorados.add(cidade)

        for vizinho, custo in mapa_romenia[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo
                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')


caminho, custo = busca_a_estrela('Arad', 'Bucharest')
print('Caminho:', ' -> '.join(caminho))
print('Custo :', custo, 'km')
print('Passos:', len(caminho) - 1)
