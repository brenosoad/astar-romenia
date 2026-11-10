# Plano de Testes

Executar: `python -m unittest discover -s tests -v`

| ID | Caso de teste | Entrada | Resultado esperado | Requisito |
|---|---|---|---|---|
| CT01 | Quantidade de cidades | `mapa_romenia`, `heuristica_bucareste` | 20 e 20 | RF01, RF02 |
| CT02 | Grafo não dirigido | cada estrada A→B | existe B→A com mesmo custo | RF01 |
| CT03 | Heurística admissível | h(n) vs. custo ótimo real | h(n) ≤ custo real | RN02 |
| CT04 | Custo por Fagaras | Arad-Sibiu-Fagaras-Bucharest | 450 | RF03 |
| CT05 | Custo por Pitesti | Arad-Sibiu-R.Vilcea-Pitesti-Bucharest | 418 | RF03 |
| CT06 | Busca Arad → Bucharest | — | caminho via Pitesti, 418 km | RF05 |
| CT07 | Outras origens | Timisoara, Oradea, Craiova, Iasi | 536, 429, 239, 319 | RF05 |
| CT08 | Sem caminho | grafo com cidade isolada | `(None, inf)` | RF06 |
| CT09 | Origem = objetivo | Bucharest → Bucharest | custo 0 | RF05 |
| CT10 | Rastro | `mostrar=True` | saída contém "1. Expandindo: Arad" | RF07 |
| CT11 | Sem rastro | `mostrar=False` | saída vazia | RF07 |
| CT12 | Programa completo | `main()` | contém "Conferido" | RF08 |
