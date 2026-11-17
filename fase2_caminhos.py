# fase 2: custo de caminho e g, h, f
from mapa import mapa_romenia, heuristica_bucareste


def custo_da_estrada(origem, destino):
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None


def custo_do_caminho(caminho):
    total = 0
    for i in range(len(caminho) - 1):
        total += custo_da_estrada(caminho[i], caminho[i + 1])
    return total


def mostrar_g_h_f(caminho):
    print(f' {"cidade":<15} {"g":>5} {"h":>5} {"f":>5}')
    for i, cidade in enumerate(caminho):
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        print(f' {cidade:<15} {g:>5} {h:>5} {g + h:>5}')


por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']

print('Arad -> Sibiu:', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('Arad -> Bucharest:', custo_da_estrada('Arad', 'Bucharest'), '(sem estrada direta)')

print('\nPor Fagaras:', ' -> '.join(por_fagaras), '=', custo_do_caminho(por_fagaras), 'km')
print('Por Pitesti:', ' -> '.join(por_pitesti), '=', custo_do_caminho(por_pitesti), 'km')

print('\nValores por Fagaras:')
mostrar_g_h_f(por_fagaras)
print('\nValores por Pitesti:')
mostrar_g_h_f(por_pitesti)
