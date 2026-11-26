# Busca A* de Arad até Bucareste (Russell & Norvig, cap. 3)
# f(n) = g(n) + h(n): g = km andados, h = km em linha reta até o destino
#
# Como funciona, em resumo:
#   1. a fronteira guarda os nós ainda não expandidos;
#   2. a cada passo o nó com menor f sai da fronteira;
#   3. se ele é o objetivo, terminou: o caminho é o de menor custo;
#   4. senão, ele é marcado como explorado e seus vizinhos entram na fronteira.
from mapa import mapa_romenia, heuristica_bucareste


def resumo_fronteira(fronteira):
    """Texto curto da fronteira para imprimir: cidade(f), cidade(f), ..."""
    return ', '.join(f'{c}({f})' for f, g, c, caminho in fronteira)


def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    """Devolve (caminho, custo), ou (None, inf) se não houver caminho.
    Nó da fronteira: (f, g, cidade, caminho)."""
    # fronteira começa só com o nó inicial: g = 0 e f = h(inicio)
    fronteira = [(heuristica[inicio], 0, inicio, [inicio])]
    # cidades que já foram expandidas
    explorados = set()
    # contador usado só para numerar as linhas impressas
    iteracao = 0

    if mostrar:
        print(f'--- A* de {inicio} para {objetivo} ---')

    # enquanto houver nós para expandir
    while fronteira:
        iteracao += 1
        # ordena por f: o nó mais promissor (menor f) fica em primeiro
        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira.pop(0)

        if mostrar:
            print(f'{iteracao}. Expandindo {cidade} | g={g}, h={heuristica[cidade]}, f={f}')

        # testa o objetivo ao tirar da fronteira (não ao gerar o nó):
        # assim o primeiro caminho encontrado é o de menor custo
        if cidade == objetivo:
            return caminho, g

        # cidade já expandida por um caminho melhor: ignora o nó repetido
        if cidade in explorados:
            continue
        explorados.add(cidade)

        # gera um nó para cada vizinho ainda não explorado
        # (grafo.get evita erro se a cidade não tiver estradas)
        for vizinho, custo in grafo.get(cidade, []):
            if vizinho not in explorados:
                # g do vizinho = g do pai + km da estrada
                novo_g = g + custo
                # f do vizinho = g novo + h (linha reta até o destino)
                novo_f = novo_g + heuristica[vizinho]
                # caminho + [x] cria lista nova, sem alterar a do pai
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

        if mostrar:
            fronteira.sort(key=lambda no: no[0])
            print('   fronteira:', resumo_fronteira(fronteira))

    # fronteira esvaziou sem chegar ao objetivo: não existe caminho
    return None, float('inf')


def soma_do_caminho(caminho):
    """Soma o km de cada trecho direto no mapa (usado só para conferir o g)."""
    total = 0
    for origem, destino in zip(caminho, caminho[1:]):
        total += dict(mapa_romenia[origem])[destino]
    return total


def testes():
    """Testes automáticos: cada [TESTE OK] impresso é um assert que passou."""
    print('\n--- Testes ---')

    # TESTE 1: Arad -> Bucareste igual à figura 3.24 do livro
    caminho, custo = busca_a_estrela('Arad', 'Bucharest', mapa_romenia,
                                     heuristica_bucareste, mostrar=False)
    assert caminho == ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']
    assert custo == 418
    print('[TESTE OK] Arad -> Bucharest = 418 km, via Sibiu, Rimnicu Vilcea e Pitesti')

    # TESTE 2: o custo devolvido é a soma das estradas do caminho
    assert soma_do_caminho(caminho) == custo
    print('[TESTE OK] custo devolvido = soma das estradas do caminho')

    # TESTE 3: origem igual ao destino custa 0
    caminho0, custo0 = busca_a_estrela('Bucharest', 'Bucharest', mapa_romenia,
                                       heuristica_bucareste, mostrar=False)
    assert caminho0 == ['Bucharest'] and custo0 == 0
    print('[TESTE OK] Bucharest -> Bucharest = 0 km')

    # TESTE 4: outras origens (valores conferidos à mão e com Dijkstra)
    esperados = {'Timisoara': 536, 'Oradea': 429, 'Craiova': 239, 'Iasi': 319}
    for origem, custo_esp in esperados.items():
        c, k = busca_a_estrela(origem, 'Bucharest', mapa_romenia,
                               heuristica_bucareste, mostrar=False)
        assert k == custo_esp, f'{origem}: esperado {custo_esp}, veio {k}'
        assert c[0] == origem and c[-1] == 'Bucharest'
        assert soma_do_caminho(c) == k
        print(f'[TESTE OK] {origem:<9} -> Bucharest = {k} km')

    # TESTE 5: sem caminho, devolve (None, inf)
    # grafo pequeno com a cidade C isolada (sem estradas)
    grafo_teste = {'A': [('B', 1)], 'B': [('A', 1)], 'C': []}
    h_teste = {'A': 0, 'B': 0, 'C': 0}
    c_nulo, k_nulo = busca_a_estrela('A', 'C', grafo_teste, h_teste, mostrar=False)
    assert c_nulo is None and k_nulo == float('inf')
    print('[TESTE OK] cidade sem ligação: devolve (None, inf)')

    # TESTE 6: a heurística é admissível (h nunca passa do custo real)
    # condição para o A* achar sempre o caminho ótimo
    for cidade in mapa_romenia:
        _, real = busca_a_estrela(cidade, 'Bucharest', mapa_romenia,
                                  heuristica_bucareste, mostrar=False)
        assert heuristica_bucareste[cidade] <= real, f'h({cidade}) maior que o custo real'
    print('[TESTE OK] h(n) <= custo real em todas as 20 cidades (heurística admissível)')

    print('\n=== Todos os testes passaram ===')


def main():
    # execução principal: Arad -> Bucareste, mostrando cada iteração
    caminho, custo = busca_a_estrela('Arad', 'Bucharest',
                                     mapa_romenia, heuristica_bucareste)
    print('\n--- Resultado ---')
    if not caminho:
        print('Sem caminho.')
        return
    print('Caminho:', ' -> '.join(caminho))
    print(f'Custo: {custo} km em {len(caminho) - 1} passos')

    # o livro dá 418 km em 4 passos
    if custo == 418 and len(caminho) - 1 == 4:
        print('Confere com o livro (418 km, 4 passos).')
    else:
        print('ATENÇÃO: diferente do livro (418 km, 4 passos).')

    # roda o A* para outras cidades, sem imprimir as iterações
    print('\n--- Outras origens ---')
    for origem in ['Timisoara', 'Oradea', 'Craiova', 'Iasi']:
        caminho, custo = busca_a_estrela(origem, 'Bucharest', mapa_romenia,
                                         heuristica_bucareste, mostrar=False)
        print(f'{origem:<10} {custo:>4} km ', ' -> '.join(caminho))

    # testes automáticos no final
    testes()


# só executa main() quando o arquivo é rodado direto (python a_estrela.py)
if __name__ == '__main__':
    main()
