# -*- coding: utf-8 -*-
# Desafio 1 da Fase 5: ordenar só por h vira busca gulosa (450 km)
from mapa import mapa_romenia, heuristica_bucareste


def busca_gulosa(inicio, objetivo):
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    explorados = set()
    while fronteira:
        fronteira.sort(key=lambda no: heuristica_bucareste[no[2]])
        f, g, cidade, caminho = fronteira.pop(0)
        if cidade == objetivo:
            return caminho, g
        if cidade in explorados:
            continue
        explorados.add(cidade)
        for vizinho, custo in mapa_romenia[cidade]:
            if vizinho not in explorados:
                fronteira.append((0, g + custo, vizinho, caminho + [vizinho]))
    return None, float('inf')


caminho, custo = busca_gulosa('Arad', 'Bucharest')
print('Gulosa:', ' -> '.join(caminho), '=', custo, 'km')
