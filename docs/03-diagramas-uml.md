# Diagramas UML

## Atividade — algoritmo A*
```mermaid
flowchart TD
    I([Início]) --> A["fronteira = [(h(início), 0, início, [início])]<br/>explorados = set()"]
    A --> B{fronteira vazia?}
    B -- sim --> F["return None, inf"]
    B -- não --> C["ordenar fronteira por f"]
    C --> D["retirar nó de menor f"]
    D --> E{cidade == objetivo?}
    E -- sim --> G["return caminho, g"]
    E -- não --> H{cidade em explorados?}
    H -- sim --> B
    H -- não --> J["explorados.add(cidade)"]
    J --> K["para cada vizinho não explorado:<br/>novo_g = g + custo<br/>novo_f = novo_g + h(vizinho)<br/>adicionar à fronteira"]
    K --> B
```

## Sequência — programa completo
```mermaid
sequenceDiagram
    participant P as Python
    participant M as main()
    participant B as busca_a_estrela()
    participant R as resumo_fronteira()
    P->>M: __name__ == '__main__'
    M->>B: ('Arad','Bucharest', grafo, h)
    loop while fronteira
        B->>B: sort e pop(0)
        B-->>M: imprime "N. Expandindo"
        opt cidade == objetivo
            B-->>M: return caminho, g
        end
        B->>R: resumo_fronteira(fronteira)
        R-->>B: "Cidade(f), ..."
    end
    M->>M: confere 418 km / 4 passos
    loop outras origens
        M->>B: busca(origem, ..., mostrar=False)
        B-->>M: (caminho, custo)
    end
```

## Classes — estruturas de dados
```mermaid
classDiagram
    class mapa_romenia {
        <<dict>>
        chave : str
        valor : list~estrada~
    }
    class estrada {
        <<tuple>>
        vizinho : str
        custo : int
    }
    class heuristica_bucareste {
        <<dict>>
        chave : str
        valor : int
    }
    class no {
        <<tuple>>
        f : int
        g : int
        cidade : str
        caminho : list~str~
    }
    class fronteira {
        <<list>>
        append(no)
        sort(key)
        pop(0)
    }
    mapa_romenia "1" *-- "1..*" estrada
    fronteira "1" o-- "0..*" no
    no ..> heuristica_bucareste : usa h(n)
    no ..> mapa_romenia : expande
```

## Estados — arquivo no Git
```mermaid
stateDiagram-v2
    [*] --> Modificado
    Modificado --> Preparado : git add
    Preparado --> Commitado : git commit
    Commitado --> Publicado : git push
    Publicado --> Modificado : editar arquivo
```

## Pacotes — arquivos do projeto
```mermaid
flowchart LR
    subgraph astar-romenia
        mapa[mapa.py]
        f1[fase1_explorar.py] -.import.-> mapa
        f2[fase2_caminhos.py] -.import.-> mapa
        f3[fase3_fronteira.py] -.import.-> mapa
        f4[fase4_expandir.py] -.import.-> mapa
        f5[fase5_busca.py] -.import.-> mapa
        f6[a_estrela.py] -.import.-> mapa
        t[tests/test_a_estrela.py] -.import.-> f6
    end
```

## Objetos — árvore de busca (Arad → Bucareste)
```mermaid
flowchart TD
    A["1. Arad f=366"] --> S["2. Sibiu f=393"]
    A --> T["Timisoara f=447"]
    A --> Z["Zerind f=449"]
    S --> O["Oradea f=671"]
    S --> F["4. Fagaras f=415"]
    S --> R["3. Rimnicu Vilcea f=413"]
    F --> B1["Bucharest f=450 (não retirado)"]
    R --> C1["Craiova f=526"]
    R --> P["5. Pitesti f=417"]
    P --> B2["6. Bucharest f=418 ✔"]
    P --> C2["Craiova f=615"]
    style B2 fill:#c8f0d8
```
