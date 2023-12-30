from exercicio1 import porcentagem_desconto
from exercicio1 import valor_normal
from exercicio1 import valor_descontado
import pytest

quant=100

def test_desconto_1():
    assert porcentagem_desconto(quant) == 0.95

def test_desconto_2():
    assert porcentagem_desconto(quant) == 0.90

def test_desconto_3():
    assert porcentagem_desconto(quant) == 0.85
    
def test_valor_quantidade():
    assert valor_normal(5,10) == 50
    
def test_valor_com_desconto():
    return valor_descontado(50,0.90) == 45
    