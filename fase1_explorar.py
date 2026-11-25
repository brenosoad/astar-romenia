# fase 1: só olhando os dados
# Objetivo: entender como o mapa (grafo) e a heurística estão guardados
# antes de escrever qualquer algoritmo de busca.
from mapa import mapa_romenia, heuristica_bucareste

# ---------------------------------------------------------------
# 1) Tamanho das estruturas
# ---------------------------------------------------------------
# mapa_romenia é um dicionário: cidade -> lista de (vizinho, km)
# heuristica_bucareste é um dicionário: cidade -> km em linha reta até Bucareste
print('Cidades no mapa:', len(mapa_romenia))
print('Valores de h:', len(heuristica_bucareste))

# TESTE: o livro tem 20 cidades e cada uma precisa ter um valor de h
assert len(mapa_romenia) == 20, 'o mapa deveria ter 20 cidades'
assert len(heuristica_bucareste) == 20, 'a heurística deveria ter 20 valores'
print('[TESTE OK] 20 cidades no mapa e 20 valores de h')

# ---------------------------------------------------------------
# 2) Vizinhos de uma cidade
# ---------------------------------------------------------------
# Cada entrada do dicionário é uma lista de tuplas (vizinho, custo)
vizinhos_arad = mapa_romenia['Arad']
print('\nVizinhos de Arad:', vizinhos_arad)
print('Tipo:', type(vizinhos_arad))

# TESTE: Arad tem 3 estradas (Zerind, Sibiu e Timisoara)
assert isinstance(vizinhos_arad, list), 'os vizinhos devem ser uma lista'
assert len(vizinhos_arad) == 3, 'Arad deveria ter 3 estradas'
print('[TESTE OK] Arad tem', len(vizinhos_arad), 'estradas')

# ---------------------------------------------------------------
# 3) Acessando uma tupla (vizinho, custo)
# ---------------------------------------------------------------
primeira = vizinhos_arad[0]
print('\nPrimeira estrada de Arad:', primeira)
print(' vizinho:', primeira[0])  # posição 0 = nome da cidade vizinha
print(' custo :', primeira[1])   # posição 1 = distância em km

# TESTE: a primeira estrada de Arad é Zerind, a 75 km
assert primeira == ('Zerind', 75), 'primeira estrada de Arad deveria ser Zerind (75)'
print('[TESTE OK] primeira estrada = Zerind, 75 km')

# ---------------------------------------------------------------
# 4) Percorrendo as estradas de uma cidade
# ---------------------------------------------------------------
# O for desempacota cada tupla direto em duas variáveis
print('\nEstradas que saem de Arad:')
soma_arad = 0
for vizinho, custo in mapa_romenia['Arad']:
    print(' Arad ->', vizinho, '=', custo, 'km')
    soma_arad += custo

# TESTE: 75 + 140 + 118 = 333 km de estradas saindo de Arad
assert soma_arad == 333, 'a soma das estradas de Arad deveria ser 333'
print('[TESTE OK] soma das estradas de Arad =', soma_arad, 'km')

# ---------------------------------------------------------------
# 5) Quantidade de estradas por cidade
# ---------------------------------------------------------------
print('\nEstradas por cidade:')
total_estradas = 0
for cidade in mapa_romenia:
    qtd = len(mapa_romenia[cidade])
    total_estradas += qtd
    print(f' {cidade:<15} {qtd}')

# TESTE: as estradas são de mão dupla, então o total de entradas é par
# (cada estrada A-B aparece em A e também em B)
assert total_estradas % 2 == 0, 'o total de entradas deveria ser par'
print('[TESTE OK] total de entradas =', total_estradas, '(par, estradas de mão dupla)')

# TESTE: toda cidade que aparece como vizinho também existe no mapa
# e tem valor de h (senão a busca daria KeyError mais tarde)
for cidade in mapa_romenia:
    assert cidade in heuristica_bucareste, f'{cidade} sem valor de h'
    for vizinho, custo in mapa_romenia[cidade]:
        assert vizinho in mapa_romenia, f'{vizinho} (vizinho de {cidade}) não está no mapa'
print('[TESTE OK] todas as cidades têm h e todo vizinho existe no mapa')

# ---------------------------------------------------------------
# 6) Estrada (g) x heurística (h) dos vizinhos de Arad
# ---------------------------------------------------------------
# h é a distância em linha reta até Bucareste; a estrada é o custo real
h_arad = heuristica_bucareste['Arad']
print('\nh(Arad) =', h_arad)

# TESTE: valor da figura 3.22 do livro
assert h_arad == 366, 'h(Arad) deveria ser 366'
print('[TESTE OK] h(Arad) = 366')

for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3} h = {h:>3}')

# TESTE: h(Bucareste) tem que ser 0 (chegou no destino)
assert heuristica_bucareste['Bucharest'] == 0, 'h(Bucharest) deveria ser 0'
print('[TESTE OK] h(Bucharest) = 0')

print('\n=== Fase 1: todos os testes passaram ===')
