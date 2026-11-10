# -*- coding: utf-8 -*-
# fase2_caminhos.py — Fase 2: funções, custo de um caminho e os valores g, h e f.
# Rode com: python fase2_caminhos.py

from mapa import mapa_romenia, heuristica_bucareste


def custo_da_estrada(origem, destino):
    """Devolve os km da estrada origem -> destino, ou None se ela não existe."""
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None


def custo_do_caminho(caminho):
    """Recebe uma lista de cidades e devolve a soma das estradas, em km."""
    total = 0
    for i in range(len(caminho) - 1):
        total = total + custo_da_estrada(caminho[i], caminho[i + 1])
    return total


def mostrar_g_h_f(caminho):
    """Para cada cidade do caminho imprime g (já andado), h (falta) e f = g + h."""
    print(f' {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')
    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h
        print(f' {cidade:<15} {g:>5} {h:>5} {f:>5}')


if __name__ == '__main__':
    print('Arad -> Sibiu custa', custo_da_estrada('Arad', 'Sibiu'), 'km')
    print('Arad -> Bucharest custa', custo_da_estrada('Arad', 'Bucharest'),
          '(não existe estrada direta)')

    por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
    por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
    print()
    print('Caminho por Fagaras:', ' -> '.join(por_fagaras))
    print('   custo =', custo_do_caminho(por_fagaras), 'km')
    print('Caminho por Pitesti:', ' -> '.join(por_pitesti))
    print('   custo =', custo_do_caminho(por_pitesti), 'km')

    print()
    print('Valores ao longo do caminho por Fagaras:')
    mostrar_g_h_f(por_fagaras)
    print()
    print('Valores ao longo do caminho por Pitesti:')
    mostrar_g_h_f(por_pitesti)
