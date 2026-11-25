# fase 2: custo de caminho e g, h, f
# Objetivo: calcular o custo de uma estrada e de um caminho inteiro (g),
# e montar f(n) = g(n) + h(n), que é o valor que o A* usa para escolher
# qual cidade expandir primeiro.
from mapa import mapa_romenia, heuristica_bucareste


def custo_da_estrada(origem, destino):
    """Devolve o km da estrada direta origem -> destino, ou None se não existir."""
    # percorre as estradas que saem da origem procurando o destino
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    # chegou ao fim sem achar: não há estrada direta
    return None


def custo_do_caminho(caminho):
    """Soma o km de cada trecho de uma lista de cidades. Isso é o g(n)."""
    total = 0
    # pares consecutivos: (caminho[0], caminho[1]), (caminho[1], caminho[2]), ...
    for i in range(len(caminho) - 1):
        total += custo_da_estrada(caminho[i], caminho[i + 1])
    return total


def mostrar_g_h_f(caminho):
    """Imprime g, h e f = g + h para cada cidade do caminho."""
    print(f' {"cidade":<15} {"g":>5} {"h":>5} {"f":>5}')
    for i, cidade in enumerate(caminho):
        # g: custo acumulado desde o início até esta cidade
        g = custo_do_caminho(caminho[:i + 1])
        # h: estimativa em linha reta até Bucareste
        h = heuristica_bucareste[cidade]
        print(f' {cidade:<15} {g:>5} {h:>5} {g + h:>5}')


# dois caminhos possíveis de Arad até Bucareste
por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']

# ---------------------------------------------------------------
# 1) Custo de uma estrada direta
# ---------------------------------------------------------------
print('Arad -> Sibiu:', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('Arad -> Bucharest:', custo_da_estrada('Arad', 'Bucharest'), '(sem estrada direta)')

# TESTE: Arad-Sibiu existe (140 km) e Arad-Bucareste não existe
assert custo_da_estrada('Arad', 'Sibiu') == 140, 'Arad -> Sibiu deveria ser 140'
assert custo_da_estrada('Arad', 'Bucharest') is None, 'Arad -> Bucharest não tem estrada direta'
print('[TESTE OK] Arad -> Sibiu = 140 km e Arad -> Bucharest = None')

# TESTE: a estrada de ida e de volta tem o mesmo custo (mão dupla)
assert custo_da_estrada('Sibiu', 'Arad') == custo_da_estrada('Arad', 'Sibiu')
print('[TESTE OK] estrada de mão dupla: Sibiu -> Arad = Arad -> Sibiu')

# ---------------------------------------------------------------
# 2) Custo de um caminho inteiro
# ---------------------------------------------------------------
custo_fagaras = custo_do_caminho(por_fagaras)
custo_pitesti = custo_do_caminho(por_pitesti)

print('\nPor Fagaras:', ' -> '.join(por_fagaras), '=', custo_fagaras, 'km')
print('Por Pitesti:', ' -> '.join(por_pitesti), '=', custo_pitesti, 'km')

# TESTE: 140 + 99 + 211 = 450 e 140 + 80 + 97 + 101 = 418
assert custo_fagaras == 450, 'caminho por Fagaras deveria custar 450'
assert custo_pitesti == 418, 'caminho por Pitesti deveria custar 418'
print('[TESTE OK] Fagaras = 450 km e Pitesti = 418 km')

# TESTE: o caminho por Pitesti é o mais barato (é o que o A* deve achar)
assert custo_pitesti < custo_fagaras, 'Pitesti deveria ser mais barato que Fagaras'
print('[TESTE OK] o caminho por Pitesti é o mais barato (418 < 450)')

# TESTE: caminho com uma única cidade custa 0
assert custo_do_caminho(['Arad']) == 0, 'caminho de uma cidade deveria custar 0'
print('[TESTE OK] caminho com uma só cidade custa 0 km')

# ---------------------------------------------------------------
# 3) Valores de g, h e f ao longo de cada caminho
# ---------------------------------------------------------------
print('\nValores por Fagaras:')
mostrar_g_h_f(por_fagaras)
print('\nValores por Pitesti:')
mostrar_g_h_f(por_pitesti)

# TESTE: f no último nó = custo total (porque h(Bucareste) = 0)
for nome, caminho in [('Fagaras', por_fagaras), ('Pitesti', por_pitesti)]:
    ultimo = caminho[-1]
    f_final = custo_do_caminho(caminho) + heuristica_bucareste[ultimo]
    assert f_final == custo_do_caminho(caminho), f'f final por {nome} deveria ser igual a g'
print('[TESTE OK] no último nó f = g, pois h(Bucharest) = 0')

# TESTE: f de Fagaras (415) vem antes de f de Rimnicu Vilcea (413)?
# Aqui 413 < 415, então o A* prefere Rimnicu Vilcea a Fagaras
f_fagaras = custo_do_caminho(['Arad', 'Sibiu', 'Fagaras']) + heuristica_bucareste['Fagaras']
f_rimnicu = custo_do_caminho(['Arad', 'Sibiu', 'Rimnicu Vilcea']) + heuristica_bucareste['Rimnicu Vilcea']
print(f'f(Fagaras) = {f_fagaras} | f(Rimnicu Vilcea) = {f_rimnicu}')
assert f_fagaras == 415 and f_rimnicu == 413, 'valores de f diferentes da figura 3.24'
assert f_rimnicu < f_fagaras, 'o A* deveria preferir Rimnicu Vilcea'
print('[TESTE OK] f(Rimnicu Vilcea) = 413 < f(Fagaras) = 415')

print('\n=== Fase 2: todos os testes passaram ===')
