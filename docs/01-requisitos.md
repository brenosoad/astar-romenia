# Especificação de Requisitos

## Objetivo
Encontrar o caminho de menor custo entre duas cidades da Romênia (padrão: Arad → Bucareste) usando busca A*, com f(n) = g(n) + h(n).

## Requisitos funcionais
| ID | Requisito | Prioridade |
|---|---|---|
| RF01 | O sistema deve armazenar o mapa rodoviário como grafo não dirigido ponderado (20 cidades). | Alta |
| RF02 | O sistema deve armazenar a heurística h(n) (distância em linha reta até Bucareste). | Alta |
| RF03 | O sistema deve calcular o custo de um caminho (soma das estradas). | Alta |
| RF04 | O sistema deve calcular g(n), h(n) e f(n) para cada cidade de um caminho. | Média |
| RF05 | O sistema deve executar a busca A* entre origem e objetivo e devolver (caminho, custo). | Alta |
| RF06 | O sistema deve devolver `(None, infinito)` quando não houver caminho. | Alta |
| RF07 | O sistema deve imprimir o rastro de cada iteração (nó expandido e fronteira). | Média |
| RF08 | O sistema deve conferir automaticamente o resultado esperado (418 km, 4 passos). | Média |

## Requisitos não funcionais
| ID | Requisito |
|---|---|
| RNF01 | Python 3, somente biblioteca padrão. |
| RNF02 | Dados separados da lógica (`mapa.py`). |
| RNF03 | A busca deve ser reutilizável: grafo e heurística passados por parâmetro. |
| RNF04 | O resultado deve ser ótimo (heurística admissível e teste de objetivo ao retirar o nó). |
| RNF05 | Histórico Git com um commit por fase. |

## Regras de negócio
- RN01: custo da estrada em km, inteiro positivo.
- RN02: a heurística nunca superestima o custo real (admissível).
- RN03: cidades já exploradas não são expandidas novamente.

## Rastreabilidade
| Requisito | Arquivo | Teste |
|---|---|---|
| RF01, RF02 | `mapa.py` | `TestDados` |
| RF03, RF04 | `fase2_caminhos.py` | `TestCusto` |
| RF05, RF06, RF07, RF08 | `a_estrela.py` | `TestBusca` |
