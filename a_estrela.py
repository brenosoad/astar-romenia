# Busca A* de Arad até Bucareste (Russell & Norvig, cap. 3)
# f(n) = g(n) + h(n): g = km andados, h = km em linha reta até o destino
from mapa import mapa_romenia, heuristica_bucareste


def resumo_fronteira(fronteira):
    return ', '.join(f'{c}({f})' for f, g, c, caminho in fronteira)


def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    """Devolve (caminho, custo), ou (None, inf) se não houver caminho.
    Nó da fronteira: (f, g, cidade, caminho)."""
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'--- A* de {inicio} para {objetivo} ---')

    while fronteira:
        iteracao += 1
        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandindo {cidade} | g={g}, h={heuristica[cidade]}, f={f}')

        if cidade == objetivo:
            return caminho, g

        if cidade in explorados:
            continue
        explorados.add(cidade)

        for vizinho, custo in grafo.get(cidade, []):
            if vizinho not in explorados:
                novo_g = g + custo
                novo_f = novo_g + heuristica[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('   fronteira:', resumo_fronteira(fronteira))

    return None, float('inf')


def main():
    caminho, custo = busca_a_estrela('Arad', 'Bucharest',
                                     mapa_romenia, heuristica_bucareste)
    print('\n--- Resultado ---')
    if not caminho:
        print('Sem caminho.')
        return
    print('Caminho:', ' -> '.join(caminho))
    print(f'Custo: {custo} km em {len(caminho) - 1} passos')

    # o livro dá 418 km em 4 passos
    if custo == 418 and len(caminho) - 1 == 4:
        print('Confere com o livro (418 km, 4 passos).')
    else:
        print('ATENÇÃO: diferente do livro (418 km, 4 passos).')

    print('\n--- Outras origens ---')
    for origem in ['Timisoara', 'Oradea', 'Craiova', 'Iasi']:
        caminho, custo = busca_a_estrela(origem, 'Bucharest', mapa_romenia,
                                         heuristica_bucareste, mostrar=False)
        print(f'{origem:<10} {custo:>4} km ', ' -> '.join(caminho))


if __name__ == '__main__':
    main()
