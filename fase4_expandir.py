# fase 4: função expandir e conjunto de explorados
from mapa import mapa_romenia, heuristica_bucareste


def mostrar_fronteira(fronteira):
    print('   fronteira:', ', '.join(f'{c}(f={f})' for f, g, c, caminho in fronteira))


def expandir(no, explorados):
    f, g, cidade, caminho = no
    filhos = []
    for vizinho, custo in mapa_romenia[cidade]:
        if vizinho in explorados:
            continue
        novo_g = g + custo
        novo_f = novo_g + heuristica_bucareste[vizinho]
        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
    return filhos


inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
explorados = set()

for rodada in range(1, 4):
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    explorados.add(no[2])
    print(f'Rodada {rodada}: expandindo {no[2]} (f={no[0]}, g={no[1]})')
    fronteira += expandir(no, explorados)
    mostrar_fronteira(fronteira)
    print('   explorados:', sorted(explorados), '\n')
