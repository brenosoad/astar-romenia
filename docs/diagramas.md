# Diagramas UML

Diagramas do projeto da busca A* (Arad até Bucareste). Estão em Mermaid, que o GitHub desenha direto na página.

## 1. Diagrama de classes

As estruturas de dados do programa. Em Python elas são dict, list e tuple, não classes de verdade, por isso o estereótipo em cada caixa.

```mermaid
classDiagram
    class mapa_romenia {
        <<dict>>
        cidade : str
        estradas : list
    }
    class heuristica_bucareste {
        <<dict>>
        cidade : str
        km_em_linha_reta : int
    }
    class Estrada {
        <<tuple>>
        vizinho : str
        custo : int
    }
    class No {
        <<tuple>>
        f : int
        g : int
        cidade : str
        caminho : list
    }
    class Fronteira {
        <<list>>
        append(no)
        sort(key)
        pop(0)
    }
    mapa_romenia "1" o-- "1..*" Estrada : estradas de cada cidade
    Fronteira "1" o-- "0..*" No : nos ainda nao expandidos
```

## 2. Diagrama de atividade

O fluxo da função busca_a_estrela.

```mermaid
flowchart TD
    A([Início]) --> B["fronteira recebe o nó inicial<br/>explorados começa vazio"]
    B --> C{"fronteira vazia?"}
    C -- sim --> Z(["Devolve falha"])
    C -- não --> D["Ordena pelo f e tira o primeiro nó"]
    D --> E{"cidade é o objetivo?"}
    E -- sim --> F(["Devolve caminho e custo"])
    E -- não --> G{"cidade já foi explorada?"}
    G -- sim --> C
    G -- não --> H["Marca a cidade como explorada"]
    H --> I["Para cada vizinho não explorado:<br/>calcula g e f e põe na fronteira"]
    I --> C
```

## 3. Diagrama de sequência

Quem chama quem durante a execução.

```mermaid
sequenceDiagram
    participant M as main
    participant B as busca_a_estrela
    participant F as fronteira
    participant G as mapa_romenia
    M->>B: inicio, objetivo, grafo, heuristica
    B->>F: cria com o nó inicial
    loop enquanto houver nós na fronteira
        B->>F: sort e pop(0)
        F-->>B: nó de menor f
        alt cidade é o objetivo
            B-->>M: caminho e custo
        else cidade ainda não explorada
            B->>G: estradas da cidade
            G-->>B: lista de vizinho e custo
            B->>F: append dos filhos
        end
    end
```

## 4. Diagrama de estados

Os estados por onde um nó passa.

```mermaid
stateDiagram-v2
    [*] --> NaFronteira: append
    NaFronteira --> Escolhido: pop(0), menor f
    Escolhido --> Objetivo: cidade é o objetivo
    Escolhido --> Descartado: cidade já explorada
    Escolhido --> Expandido: gera os filhos
    Objetivo --> [*]
    Descartado --> [*]
    Expandido --> [*]
```

## 5. Diagrama de pacotes

Como os arquivos se relacionam. Todos usam os dados de mapa.py.

```mermaid
flowchart LR
    mapa["mapa.py<br/>mapa_romenia<br/>heuristica_bucareste"]
    f1["fase1_explorar.py"] -->|import| mapa
    f2["fase2_caminhos.py"] -->|import| mapa
    f3["fase3_fronteira.py"] -->|import| mapa
    f4["fase4_expandir.py"] -->|import| mapa
    f5["fase5_busca.py"] -->|import| mapa
    af["a_estrela.py"] -->|import| mapa
```
