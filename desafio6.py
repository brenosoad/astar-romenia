# -*- coding: utf-8 -*-
# Desafios da Fase 6
from mapa import mapa_romenia, heuristica_bucareste
from a_estrela import busca_a_estrela

h_zero = {c: 0 for c in mapa_romenia}
print('1) Heurística zero (custo uniforme):')
caminho, custo = busca_a_estrela('Arad', 'Bucharest', mapa_romenia, h_zero)
print('   custo =', custo, 'km')

print('2) Outras origens:')
for origem in ['Lugoj', 'Mehadia', 'Eforie']:
    caminho, custo = busca_a_estrela(origem, 'Bucharest', mapa_romenia,
                                     heuristica_bucareste, mostrar=False)
    print(f'   {origem:<8} {custo} km', ' -> '.join(caminho))
