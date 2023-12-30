from exercicio4 import *
from unittest import mock
import pytest
import sys
from io import StringIO
def test_remover_peca(monkeypatch):

    pecas.append({'codigo': 1, 'nome': 'Roda4', 'fabricante': 'Cofap', 'valor': 10.5})

    monkeypatch.setattr('builtins.input', lambda _: 1)

    remover_peca()

    assert len(pecas) == 0

import sys
from io import StringIO
def test_imprimir_peca():

    output = StringIO()
    sys.stdout = output

    peca = {'codigo': 1, 'fabricante': 'fabricante 1', 'valor': 10.0}


    imprimir_peca(peca)

    printed_output = output.getvalue()

    sys.stdout = sys.__stdout__

    assert printed_output == "Código: 1\nFabricante: fabricante 1\nValor: 10.0R$\n"


def simulate_input(inputs_list):
    return lambda *args: inputs_list.pop(0)

def test_cadastro_peca(monkeypatch):

    inputs = [123, 'Nome da Peça', 'Fabricante de Peça', 10.5]
    monkeypatch.setattr('builtins.input', simulate_input(inputs))


    cadastrar_peca()

    assert len(pecas) == 1
    assert pecas[0]["codigo"] == 123
    assert pecas[0]["nome"] == 'Nome da Peça'
    assert pecas[0]["fabricante"] == 'Fabricante de Peça'
    assert pecas[0]["valor"] == 10.5