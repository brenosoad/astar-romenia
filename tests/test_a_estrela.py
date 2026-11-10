# -*- coding: utf-8 -*-
import io
import os
import sys
import unittest
from contextlib import redirect_stdout

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from mapa import mapa_romenia, heuristica_bucareste  # noqa: E402
from fase2_caminhos import custo_do_caminho  # noqa: E402
from a_estrela import busca_a_estrela, main  # noqa: E402


def busca(origem, destino='Bucharest', mostrar=False):
    return busca_a_estrela(origem, destino, mapa_romenia,
                           heuristica_bucareste, mostrar=mostrar)


class TestDados(unittest.TestCase):
    def test_quantidade(self):
        self.assertEqual(len(mapa_romenia), 20)
        self.assertEqual(len(heuristica_bucareste), 20)

    def test_grafo_nao_dirigido(self):
        for cidade, estradas in mapa_romenia.items():
            for vizinho, custo in estradas:
                self.assertIn((cidade, custo), mapa_romenia[vizinho])

    def test_heuristica_admissivel(self):
        for cidade in mapa_romenia:
            _, custo = busca(cidade)
            self.assertLessEqual(heuristica_bucareste[cidade], custo)


class TestCusto(unittest.TestCase):
    def test_por_fagaras(self):
        self.assertEqual(custo_do_caminho(
            ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']), 450)

    def test_por_pitesti(self):
        self.assertEqual(custo_do_caminho(
            ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']), 418)


class TestBusca(unittest.TestCase):
    def test_arad_bucareste(self):
        caminho, custo = busca('Arad')
        self.assertEqual(caminho, ['Arad', 'Sibiu', 'Rimnicu Vilcea',
                                   'Pitesti', 'Bucharest'])
        self.assertEqual(custo, 418)

    def test_outras_origens(self):
        esperado = {'Timisoara': 536, 'Oradea': 429, 'Craiova': 239, 'Iasi': 319}
        for origem, km in esperado.items():
            self.assertEqual(busca(origem)[1], km)

    def test_sem_caminho(self):
        grafo = dict(mapa_romenia)
        grafo['Ilha'] = []
        h = dict(heuristica_bucareste)
        h['Ilha'] = 1
        caminho, custo = busca_a_estrela('Ilha', 'Bucharest', grafo, h, mostrar=False)
        self.assertIsNone(caminho)
        self.assertEqual(custo, float('inf'))

    def test_origem_igual_objetivo(self):
        self.assertEqual(busca('Bucharest'), (['Bucharest'], 0))

    def test_rastro(self):
        saida = io.StringIO()
        with redirect_stdout(saida):
            busca('Arad', mostrar=True)
        self.assertIn('1. Expandindo: Arad', saida.getvalue())

    def test_sem_rastro(self):
        saida = io.StringIO()
        with redirect_stdout(saida):
            busca('Arad')
        self.assertEqual(saida.getvalue(), '')

    def test_main(self):
        saida = io.StringIO()
        with redirect_stdout(saida):
            main()
        self.assertIn('Conferido: igual ao livro', saida.getvalue())


if __name__ == '__main__':
    unittest.main()
