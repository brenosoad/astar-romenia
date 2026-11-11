# astar-romenia

Busca A* de Arad a Bucareste (Russell & Norvig, cap. 3),
feita em 6 fases na disciplina IIA-008 Inteligência Artificial I.

Aluno(a): Breno

## Como rodar

    python a_estrela.py

Testes:

    python -m unittest discover -s tests -v

## Resultado

Arad -> Sibiu -> Rimnicu Vilcea -> Pitesti -> Bucharest
(418 km em 4 passos, igual à Figura 3.24 do livro)

## Fases

| Arquivo | Conteúdo |
|---|---|
| mapa.py | dados: mapa da Romênia e heurística |
| fase1_explorar.py | navegar nos dados |
| fase2_caminhos.py | custo de caminho e f = g + h |
| fase3_fronteira.py | nó e fronteira à mão |
| fase4_expandir.py | função expandir e conjunto de explorados |
| fase5_busca.py | busca A* com while |
| a_estrela.py | programa completo |
| desafio1.py a desafio6.py | desafios de cada fase |

## Documentação (engenharia de software)

| Documento | Conteúdo |
|---|---|
| [docs/01-requisitos.md](docs/01-requisitos.md) | requisitos funcionais, não funcionais, regras e rastreabilidade |
| [docs/02-casos-de-uso.md](docs/02-casos-de-uso.md) | diagrama e descrição dos casos de uso |
| [docs/03-diagramas-uml.md](docs/03-diagramas-uml.md) | atividade, sequência, classes, estados, pacotes e objetos |
| [docs/04-plano-de-testes.md](docs/04-plano-de-testes.md) | casos de teste |
