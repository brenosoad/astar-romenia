# fase 1: só olhando os dados
from mapa import mapa_romenia, heuristica_bucareste

print('Cidades no mapa:', len(mapa_romenia))
print('Valores de h:', len(heuristica_bucareste))

vizinhos_arad = mapa_romenia['Arad']
print('\nVizinhos de Arad:', vizinhos_arad)
print('Tipo:', type(vizinhos_arad))

primeira = vizinhos_arad[0]
print('\nPrimeira estrada de Arad:', primeira)
print(' vizinho:', primeira[0])
print(' custo  :', primeira[1])

print('\nEstradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print(' Arad ->', vizinho, '=', custo, 'km')

print('\nEstradas por cidade:')
for cidade in mapa_romenia:
    print(f' {cidade:<15} {len(mapa_romenia[cidade])}')

print('\nh(Arad) =', heuristica_bucareste['Arad'])
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3}   h = {h:>3}')
