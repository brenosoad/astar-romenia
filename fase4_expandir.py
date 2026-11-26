# fase 4: função expandir e conjunto de explorados
# Objetivo: transformar a expansão feita à mão na fase 3 em uma função
# (expandir) e usar um conjunto de explorados para não voltar a cidades
# que já foram expandidas.
# nó = (f, g, cidade, caminho)
from mapa import mapa_romenia, heuristica_bucareste


def mostrar_fronteira(fronteira):
    """Imprime a fronteira como: cidade(f=valor), cidade(f=valor), ..."""
    print('   fronteira:', ', '.join(f'{c}(f={f})' for f, g, c, caminho in fronteira))


def expandir(no, explorados):
    """Devolve a lista de nós filhos de 'no', ignorando cidades já exploradas."""
    # desempacota o nó em 4 variáveis
    f, g, cidade, caminho = no
    filhos = []
    for vizinho, custo in mapa_romenia[cidade]:
        # não volta para cidade já expandida (evita ciclos, ex.: Sibiu -> Arad)
        if vizinho in explorados:
            continue
        # g do filho = g do pai + km da estrada
        novo_g = g + custo
        # f do filho = g novo + h (linha reta até Bucareste)
        novo_f = novo_g + heuristica_bucareste[vizinho]
        # caminho + [x] cria lista nova, sem alterar a lista do pai
        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return filhos


# ---------------------------------------------------------------
# TESTES DA FUNÇÃO expandir (antes de usar no laço)
# ---------------------------------------------------------------
no_arad = (366, 0, 'Arad', ['Arad'])

# sem explorados, Arad gera 3 filhos
filhos_arad = expandir(no_arad, set())
assert len(filhos_arad) == 3, 'Arad sem explorados deveria gerar 3 filhos'
print('[TESTE OK] expandir(Arad) gerou 3 filhos')

# o filho Sibiu tem g = 140 e f = 140 + 253 = 393
assert (393, 140, 'Sibiu', ['Arad', 'Sibiu']) in filhos_arad, 'filho Sibiu errado'
print('[TESTE OK] filho Sibiu = (f=393, g=140, caminho Arad -> Sibiu)')

# com Sibiu já explorado, ele não pode aparecer entre os filhos
filhos_sem_sibiu = expandir(no_arad, {'Sibiu'})
assert 'Sibiu' not in [n[2] for n in filhos_sem_sibiu], 'Sibiu explorado não deveria aparecer'
assert len(filhos_sem_sibiu) == 2
print('[TESTE OK] cidade explorada (Sibiu) é ignorada: sobram 2 filhos')

# o nó pai não pode ser alterado pela expansão
assert no_arad == (366, 0, 'Arad', ['Arad']), 'o nó pai foi alterado'
print('[TESTE OK] o nó pai não foi alterado pela expansão\n')

# ---------------------------------------------------------------
# SIMULAÇÃO DE 3 RODADAS DO A*
# ---------------------------------------------------------------
inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

# resultado esperado de cada rodada: (cidade expandida, f, g, tamanho da fronteira depois)
esperado = {
    1: ('Arad', 366, 0, 3),
    2: ('Sibiu', 393, 140, 5),
    3: ('Rimnicu Vilcea', 413, 220, 6),
}

for rodada in range(1, 4):
    # ordena por f: o primeiro é o nó mais promissor
    fronteira.sort(key=lambda no: no[0])
    # tira o melhor nó da fronteira e marca a cidade como explorada
    no = fronteira.pop(0)
    explorados.add(no[2])
    print(f'Rodada {rodada}: expandindo {no[2]} (f={no[0]}, g={no[1]})')
    # acrescenta os filhos na fronteira
    fronteira += expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('   explorados:', sorted(explorados), '\n')

    # TESTE da rodada: confere cidade, f, g e tamanho da fronteira
    cidade_esp, f_esp, g_esp, tam_esp = esperado[rodada]
    assert (no[2], no[0], no[1]) == (cidade_esp, f_esp, g_esp), \
        f'rodada {rodada}: nó expandido diferente do esperado'
    assert len(fronteira) == tam_esp, f'rodada {rodada}: tamanho da fronteira errado'
    print(f'[TESTE OK] rodada {rodada}: {cidade_esp} (f={f_esp}, g={g_esp}), '
          f'fronteira com {tam_esp} nós\n')

# TESTE final: a ordem de expansão bate com a figura 3.24 do livro
assert explorados == {'Arad', 'Sibiu', 'Rimnicu Vilcea'}, 'explorados diferentes do esperado'
print('[TESTE OK] explorados = Arad, Sibiu, Rimnicu Vilcea')

print('\n=== Fase 4: todos os testes passaram ===')
