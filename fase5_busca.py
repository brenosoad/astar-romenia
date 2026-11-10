# -*- coding: utf-8 -*-
# fase5_busca.py — Fase 5: o laço while que repete a expansão até chegar.
# Rode com: python fase5_busca.py

from mapa import mapa_romenia, heuristica_bucareste


def busca_a_estrela(inicio, objetivo):
    """Devolve (caminho, custo) do melhor caminho, ou (None, infinito)."""
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()

    while fronteira:
        # escolhe o nó de menor f
        fronteira.sort(key=lambda no: no[0])
        f_atual, g_atual, cidade_atual, caminho = fronteira.pop(0)

        # teste de objetivo: feito ao RETIRAR o nó, não ao gerar
        if cidade_atual == objetivo:
            return caminho, g_atual

        # cidade já explorada por um caminho melhor: descarta
        if cidade_atual in explorados:
            continue
        explorados.add(cidade_atual)

        # gera os filhos e coloca na fronteira
        for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
            if vizinho not in explorados:
                novo_g = g_atual + custo_estrada
                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    return None, float('inf')


if __name__ == '__main__':
    caminho, custo = busca_a_estrela('Arad', 'Bucharest')
    print('Caminho:', ' -> '.join(caminho))
    print('Custo :', custo, 'km')
    print('Passos :', len(caminho) - 1, 'estradas')
