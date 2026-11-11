# -*- coding: utf-8 -*-
# Desafios da Fase 2
from fase2_caminhos import custo_do_caminho, mostrar_g_h_f

longo = ['Arad', 'Timisoara', 'Lugoj', 'Mehadia', 'Drobeta', 'Craiova',
         'Pitesti', 'Bucharest']
print('1) Custo do caminho longo:', custo_do_caminho(longo), 'km')
print('2) Valores g, h, f:')
mostrar_g_h_f(longo)
