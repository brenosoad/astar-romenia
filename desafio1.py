# -*- coding: utf-8 -*-
# Desafios da Fase 1
from mapa import mapa_romenia, heuristica_bucareste

print('1) Cidades com exatamente 1 estrada:')
for cidade in mapa_romenia:
    if len(mapa_romenia[cidade]) == 1:
        print('  ', cidade)

print('2) Cidades com h(n) < 200 km:')
for cidade in heuristica_bucareste:
    if heuristica_bucareste[cidade] < 200:
        print('  ', cidade, heuristica_bucareste[cidade])

print('3) Estrada mais longa:')
maior = ('', '', 0)
for cidade in mapa_romenia:
    for vizinho, custo in mapa_romenia[cidade]:
        if custo > maior[2]:
            maior = (cidade, vizinho, custo)
print('  ', maior[0], '-', maior[1], maior[2], 'km')
