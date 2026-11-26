# fase 5: busca A* com while
# Objetivo: juntar tudo o que foi feito nas fases anteriores em um laço while
# que repete: ordenar a fronteira, tirar o melhor nó, testar o objetivo,
# marcar como explorado e gerar os vizinhos.
# nó = (f, g, cidade, caminho)
from mapa import mapa_romenia, heuristica_bucareste


def busca_a_estrela(inicio, objetivo):
    """Devolve (caminho, custo), ou (None, inf) se não houver caminho."""
    # fronteira começa só com o nó inicial: g = 0 e f = h(inicio)
    fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
    # cidades já expandidas
    explorados = set()

    # enquanto houver nós para expandir
    while fronteira:
        # o nó com menor f fica na frente da lista
        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira.pop(0)

        # testa o objetivo ao tirar da fronteira, não ao gerar o nó
        # (garante que o primeiro caminho encontrado é o de menor custo)
        if cidade == objetivo:
            return caminho, g

        # nó repetido: a cidade já foi expandida por um caminho melhor
        if cidade in explorados:
            continue
        explorados.add(cidade)

        # gera um nó para cada vizinho ainda não explorado
        for vizinho, custo in mapa_romenia[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo
                novo_f = novo_g + heuristica_bucareste[vizinho]
                # caminho + [x] cria lista nova, sem alterar a do pai
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

    # fronteira esvaziou sem chegar ao objetivo
    return None, float('inf')


def soma_do_caminho(caminho):
    """Soma o km de cada trecho direto no mapa (usado só para conferir o g)."""
    total = 0
    for origem, destino in zip(caminho, caminho[1:]):
        total += dict(mapa_romenia[origem])[destino]
    return total


# ---------------------------------------------------------------
# EXECUÇÃO PRINCIPAL: Arad -> Bucareste
# ---------------------------------------------------------------
caminho, custo = busca_a_estrela('Arad', 'Bucharest')
print('Caminho:', ' -> '.join(caminho))
print('Custo :', custo, 'km')
print('Passos:', len(caminho) - 1)

# ---------------------------------------------------------------
# TESTES
# ---------------------------------------------------------------
print('\n--- Testes ---')

# TESTE 1: resultado igual ao da figura 3.24 do livro
assert caminho == ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'], \
    'caminho diferente do livro'
assert custo == 418, 'custo deveria ser 418 km'
assert len(caminho) - 1 == 4, 'deveria ter 4 passos'
print('[TESTE OK] Arad -> Bucharest = 418 km em 4 passos (igual ao livro)')

# TESTE 2: o custo devolvido bate com a soma das estradas do caminho
assert soma_do_caminho(caminho) == custo, 'custo g diferente da soma das estradas'
print('[TESTE OK] custo devolvido = soma das estradas do caminho')

# TESTE 3: o caminho começa no início e termina no objetivo
assert caminho[0] == 'Arad' and caminho[-1] == 'Bucharest'
print('[TESTE OK] caminho começa em Arad e termina em Bucharest')

# TESTE 4: o A* achou o caminho mais barato (o por Fagaras custa 450)
assert custo < 450, 'o caminho por Fagaras (450 km) é pior que o encontrado'
print('[TESTE OK] custo 418 é menor que o caminho por Fagaras (450)')

# TESTE 5: origem igual ao destino não precisa andar
caminho_zero, custo_zero = busca_a_estrela('Bucharest', 'Bucharest')
assert caminho_zero == ['Bucharest'] and custo_zero == 0
print('[TESTE OK] Bucharest -> Bucharest = 0 km, caminho só com Bucharest')

# TESTE 6: origens perto do destino (resultados conferidos à mão)
esperados = {
    'Pitesti': 101,    # Pitesti -> Bucharest
    'Craiova': 239,    # Craiova -> Pitesti -> Bucharest (138 + 101)
    'Iasi': 319,       # Iasi -> Vaslui -> Urziceni -> Bucharest (92 + 142 + 85)
    'Oradea': 429,     # Oradea -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
}
for origem, custo_esp in esperados.items():
    c, k = busca_a_estrela(origem, 'Bucharest')
    assert k == custo_esp, f'{origem}: esperado {custo_esp}, veio {k}'
    assert soma_do_caminho(c) == k
    print(f'[TESTE OK] {origem:<8} -> Bucharest = {k} km ({" -> ".join(c)})')

print('\n=== Fase 5: todos os testes passaram ===')
