# -*- coding: utf-8 -*-
# a_estrela.py — Fase 6: o programa completo da busca A*.
# Rode com: python a_estrela.py
#
# f(n) = g(n) + h(n)
#   g(n): km já percorridos desde a origem até n (custo real)
#   h(n): km em linha reta de n até Bucareste (estimativa, heurística)
#   f(n): estimativa do custo total do caminho que passa por n

from mapa import mapa_romenia, heuristica_bucareste


def resumo_fronteira(fronteira):
    """Texto curto com a fronteira: Cidade(f) separados por vírgula."""
    return ', '.join(f'{cidade}({f})' for f, g, cidade, caminho in fronteira)


def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    """Busca A* em grafo. Devolve (caminho, custo) ou (None, infinito).

    Cada nó da fronteira é a tupla (f, g, cidade, caminho); o f fica na
    posição 0 porque é por ele que a fronteira é ordenada.
    """
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'--- Busca A* de {inicio} para {objetivo} ---')

    while fronteira:
        iteracao = iteracao + 1
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandindo: {cidade_atual} | '
                  f'g(n)={g_atual}, h(n)={heuristica[cidade_atual]} '
                  f'-> f(n)={f_atual}')

        if cidade_atual == objetivo:
            return caminho, g_atual

        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        for vizinho, custo_estrada in grafo.get(cidade_atual, []):
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('   fronteira:', resumo_fronteira(fronteira))

    return None, float('inf')


def main():
    caminho, custo = busca_a_estrela('Arad', 'Bucharest',
                                     mapa_romenia, heuristica_bucareste)
    print()
    print('--- Resultado ---')
    if caminho:
        print('Caminho encontrado:', ' -> '.join(caminho))
        print(f'Custo real total: {custo} km em {len(caminho) - 1} passos')
    else:
        print('Não foi possível encontrar um caminho.')

    # Teste de regressão: o livro diz 418 km em 4 passos.
    if caminho and custo == 418 and len(caminho) - 1 == 4:
        print('Conferido: igual ao livro (418 km, 4 passos).')
    else:
        print('ATENÇÃO: o livro espera 418 km em 4 passos. Revise o código.')

    print()
    print('--- Outras origens (sem rastro) ---')
    for origem in ['Timisoara', 'Oradea', 'Craiova', 'Iasi']:
        caminho, custo = busca_a_estrela(origem, 'Bucharest', mapa_romenia,
                                         heuristica_bucareste, mostrar=False)
        print(f'{origem:<10} {custo:>4} km ', ' -> '.join(caminho))


if __name__ == '__main__':
    main()
