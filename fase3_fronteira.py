# -*- coding: utf-8 -*-
# fase3_fronteira.py — Fase 3: o nó de busca e a fronteira, feitos à mão.
# Rode com: python fase3_fronteira.py

from mapa import mapa_romenia, heuristica_bucareste

# Um nó é uma tupla com 4 posições: (f, g, cidade, caminho)
inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]
no_inicial = (g + h, g, inicio, [inicio])

fronteira = [no_inicial]
print('Fronteira no começo:', fronteira)

# tirar o primeiro nó da fronteira
no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no
print()
print('Nó retirado:', no)
print(' f =', f_atual, '| g =', g_atual, '| cidade =', cidade_atual,
      '| caminho =', caminho)
print('Fronteira agora:', fronteira)

# gerar os filhos (vizinhos) do nó retirado
for vizinho, custo_estrada in mapa_romenia[cidade_atual]:
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print()
print('Fronteira depois de expandir Arad (ordem de inserção):')
for item in fronteira:
    print(' ', item)

# ordenar a fronteira pelo f
fronteira.sort(key=lambda no: no[0])
print()
print('Fronteira ordenada pelo f (posição 0 da tupla):')
for item in fronteira:
    print(' ', item)

# o próximo nó a ser expandido
proximo = fronteira.pop(0)
print()
print('Próximo nó a expandir:', proximo[2], 'com f =', proximo[0])
