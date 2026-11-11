# -*- coding: utf-8 -*-
# Desafio da Fase 4: seis rodadas (sem teste de objetivo)
from mapa import heuristica_bucareste
from fase4_expandir import expandir, mostrar_fronteira

fronteira = [(heuristica_bucareste['Arad'], 0, 'Arad', ['Arad'])]
explorados = set()
for rodada in range(1, 7):
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    explorados.add(no[2])
    print(f'Rodada {rodada}: expandindo {no[2]} (f={no[0]})')
    fronteira = fronteira + expandir(no, explorados)
    mostrar_fronteira(fronteira)
