# fase 3: nó e fronteira, expandindo Arad na mão
# nó = (f, g, cidade, caminho)
from mapa import mapa_romenia, heuristica_bucareste

inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
print('Fronteira inicial:', fronteira)

f, g, cidade, caminho = fronteira.pop(0)
print('Tirei:', cidade, '| f =', f, '| g =', g)

for vizinho, custo in mapa_romenia[cidade]:
    novo_g = g + custo
    novo_f = novo_g + heuristica_bucareste[vizinho]
    # caminho + [x] cria lista nova; append mexeria na lista do pai
    fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

print('\nDepois de expandir Arad:')
for no in fronteira:
    print(' ', no)

fronteira.sort(key=lambda no: no[0])
print('\nOrdenada por f:')
for no in fronteira:
    print(' ', no)

proximo = fronteira.pop(0)
print('\nPróximo:', proximo[2], 'com f =', proximo[0])
