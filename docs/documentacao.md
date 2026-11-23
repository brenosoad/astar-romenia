# Documentação do projeto

Busca A* de Arad até Bucareste, feita para a disciplina IIA-008 Inteligência Artificial I. Baseada no capítulo 3 do Russell & Norvig (3. ed.).

## 1. Objetivo

Encontrar o caminho de menor custo, em km, entre Arad e Bucareste no mapa rodoviário da Romênia (figura 3.2 do livro), usando a busca A*.

## 2. Como a busca funciona

Cada cidade na fronteira tem três valores:

| Valor | Significado |
|-------|-------------|
| g(n) | km já percorridos de Arad até a cidade n, somando as estradas |
| h(n) | distância em linha reta de n até Bucareste (figura 3.22) |
| f(n) | g(n) + h(n), a estimativa do custo total passando por n |

A cada rodada o algoritmo tira da fronteira o nó de menor f. Se a cidade for o objetivo, termina. Se já foi explorada, descarta. Senão, marca como explorada e põe os vizinhos na fronteira.

O teste do objetivo é feito ao tirar o nó da fronteira, e não ao gerar. É isso que garante o caminho ótimo: o caminho por Fagaras (450 km) chega a ser gerado, mas o por Pitesti (418 km) sai antes.

## 3. Estruturas de dados

| Estrutura | Tipo em Python | Conteúdo |
|-----------|----------------|----------|
| mapa_romenia | dict | cidade -> lista de estradas |
| estrada | tuple | (vizinho, custo em km) |
| heuristica_bucareste | dict | cidade -> km em linha reta até Bucareste |
| nó | tuple | (f, g, cidade, caminho) |
| fronteira | list | nós ainda não expandidos |
| explorados | set | cidades já expandidas |

O f fica na posição 0 do nó porque a fronteira é ordenada por ele.

## 4. Arquivos

| Arquivo | Fase | O que faz |
|---------|------|-----------|
| mapa.py | 1 | guarda o mapa e a heurística |
| fase1_explorar.py | 1 | navega pelos dados, sem busca |
| fase2_caminhos.py | 2 | custo de um caminho e valores g, h e f |
| fase3_fronteira.py | 3 | nó e fronteira, primeira expansão à mão |
| fase4_expandir.py | 4 | função expandir e conjunto de explorados |
| fase5_busca.py | 5 | busca A* com while |
| a_estrela.py | 6 | programa completo, com rastro e conferência |

Os diagramas UML estão em [diagramas.md](diagramas.md).

## 5. Como executar

Precisa do Python 3. Não há dependências externas.

    python a_estrela.py

Cada fase também roda sozinha, por exemplo:

    python fase2_caminhos.py

## 6. Resultado esperado

Para Arad -> Bucharest:

    Caminho: Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
    Custo: 418 km em 4 passos
    Confere com o livro (418 km, 4 passos).

Os valores de f dos nós expandidos, em ordem, são 366, 393, 413, 415, 417 e 418, como na figura 3.24 do livro.

O programa também calcula outras origens:

| Origem | Custo | Caminho |
|--------|-------|---------|
| Timisoara | 536 km | Timisoara, Arad, Sibiu, Rimnicu Vilcea, Pitesti, Bucharest |
| Oradea | 429 km | Oradea, Sibiu, Rimnicu Vilcea, Pitesti, Bucharest |
| Craiova | 239 km | Craiova, Pitesti, Bucharest |
| Iasi | 319 km | Iasi, Vaslui, Urziceni, Bucharest |

## 7. Decisões e limitações

- A heurística é admissível: a linha reta nunca é maior que o caminho real. Por isso o A* devolve o caminho ótimo.
- A fronteira é uma lista ordenada com sort a cada rodada. Para este mapa pequeno basta. Em um grafo grande o certo seria uma fila de prioridade (heapq).
- A heurística só vale para Bucareste como destino. Outro destino exigiria outra tabela de h.
- Os nomes das cidades seguem a grafia em inglês do livro (Bucharest, e não Bucareste).
