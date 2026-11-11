# -*- coding: utf-8 -*-
# Desafios da Fase 3
from mapa import mapa_romenia, heuristica_bucareste

# Fronteira depois de expandir Arad (já ordenada) e Sibiu à mão
fronteira = [(447, 118, 'Timisoara', ['Arad', 'Timisoara']),
             (449, 75, 'Zerind', ['Arad', 'Zerind'])]
f, g, cidade, caminho = (393, 140, 'Sibiu', ['Arad', 'Sibiu'])
for vizinho, custo in mapa_romenia[cidade]:
    novo_g = g + custo
    fronteira.append((novo_g + heuristica_bucareste[vizinho], novo_g,
                      vizinho, caminho + [vizinho]))

fronteira.sort(key=lambda no: no[0])
print('1) Fronteira ordenada por f:')
for no in fronteira:
    print('  ', no[2], no[0])

fronteira.sort(key=lambda no: no[1])
print('2) Ordenando por g, sai primeiro:', fronteira[0][2], '(custo uniforme)')
