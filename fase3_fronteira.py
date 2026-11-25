# fase 3: nó e fronteira, expandindo Arad na mão
# Objetivo: montar a fronteira do A* (lista de nós ainda não expandidos)
# e fazer à mão o que o algoritmo vai repetir: tirar o melhor nó,
# gerar os vizinhos e reordenar por f.
# nó = (f, g, cidade, caminho)
from mapa import mapa_romenia, heuristica_bucareste

# ---------------------------------------------------------------
# 1) Fronteira inicial
# ---------------------------------------------------------------
# Começa só com o nó de Arad: g = 0 (ainda não andou) e f = g + h = h(Arad)
inicio = 'Arad'
fronteira = [(heuristica_bucareste[inicio], 0, inicio, [inicio])]
print('Fronteira inicial:', fronteira)

# TESTE: um único nó, com f = 366, g = 0 e caminho só com Arad
assert len(fronteira) == 1, 'a fronteira inicial deveria ter 1 nó'
assert fronteira[0] == (366, 0, 'Arad', ['Arad']), 'nó inicial diferente do esperado'
print('[TESTE OK] fronteira inicial = [(366, 0, Arad, [Arad])]')

# ---------------------------------------------------------------
# 2) Tirando o nó da fronteira
# ---------------------------------------------------------------
# pop(0) remove e devolve o primeiro nó; a tupla é desempacotada em 4 variáveis
f, g, cidade, caminho = fronteira.pop(0)
print('Tirei:', cidade, '| f =', f, '| g =', g)

# TESTE: depois do pop a fronteira fica vazia e o nó tirado é Arad
assert len(fronteira) == 0, 'depois do pop a fronteira deveria estar vazia'
assert cidade == 'Arad' and f == 366 and g == 0
print('[TESTE OK] nó retirado = Arad (f = 366, g = 0) e fronteira vazia')

# ---------------------------------------------------------------
# 3) Expandindo: gerando um nó para cada vizinho
# ---------------------------------------------------------------
for vizinho, custo in mapa_romenia[cidade]:
    # g do vizinho = g do pai + km da estrada
    novo_g = g + custo
    # f do vizinho = g novo + estimativa em linha reta até Bucareste
    novo_f = novo_g + heuristica_bucareste[vizinho]
    # caminho + [x] cria lista nova; append mexeria na lista do pai
    fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))

print('\nDepois de expandir Arad:')
for no in fronteira:
    print(' ', no)

# TESTE: Arad tem 3 vizinhos, então a fronteira ganha 3 nós
assert len(fronteira) == 3, 'expandir Arad deveria gerar 3 nós'
print('[TESTE OK] 3 nós gerados (Zerind, Sibiu e Timisoara)')

# TESTE: valores de f de cada vizinho (g + h)
f_por_cidade = {no[2]: no[0] for no in fronteira}
assert f_por_cidade == {'Zerind': 449, 'Sibiu': 393, 'Timisoara': 447}, \
    'valores de f diferentes do esperado'
print('[TESTE OK] f(Zerind) = 449, f(Sibiu) = 393, f(Timisoara) = 447')

# TESTE: a lista do pai não foi alterada (por isso usamos caminho + [x])
assert caminho == ['Arad'], 'a lista do nó pai foi alterada'
print('[TESTE OK] o caminho do nó pai continua [Arad]')

# ---------------------------------------------------------------
# 4) Ordenando a fronteira por f
# ---------------------------------------------------------------
# o primeiro da lista passa a ser o nó mais promissor (menor f)
fronteira.sort(key=lambda no: no[0])
print('\nOrdenada por f:')
for no in fronteira:
    print(' ', no)

# TESTE: a ordem esperada é Sibiu (393), Timisoara (447), Zerind (449)
ordem = [no[2] for no in fronteira]
assert ordem == ['Sibiu', 'Timisoara', 'Zerind'], 'ordem da fronteira errada'
print('[TESTE OK] ordem por f: Sibiu, Timisoara, Zerind')

# ---------------------------------------------------------------
# 5) Escolhendo o próximo nó a expandir
# ---------------------------------------------------------------
proximo = fronteira.pop(0)
print('\nPróximo:', proximo[2], 'com f =', proximo[0])

# TESTE: o A* escolhe Sibiu (f = 393), igual à figura 3.24 do livro
assert proximo[2] == 'Sibiu' and proximo[0] == 393, 'o próximo deveria ser Sibiu (393)'
assert proximo[3] == ['Arad', 'Sibiu'], 'caminho até Sibiu errado'
print('[TESTE OK] próximo nó = Sibiu (f = 393), caminho Arad -> Sibiu')

print('\n=== Fase 3: todos os testes passaram ===')
