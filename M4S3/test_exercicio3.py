from exercicio3 import *
import pytest

#Teste da Função de calculo de preço de volume
def test_atividade_volume_10():
    assert calcular_preco_volume(999) == 10.0

def test_atividade_volume_20():
    assert calcular_preco_volume(1000 and 9999) == 20.0

def test_atividade_volume_30():
    assert calcular_preco_volume(10000 and 29999) == 30.0

def test_atividade_volume_40():
    assert calcular_preco_volume(30000 and 99909) == 40.0


#Teste da função de calculo de multiplicador de peso

def test_atividade_peso_01():
    assert calcular_multiplicador_peso(0.05) == 1.0

def test_atividade_peso_02():
    assert calcular_multiplicador_peso(0.3 and 0.45) == 1.5

def test_atividade_peso_03():
    assert calcular_multiplicador_peso(1.7 and 6) == 2.0

def test_atividade_peso_04():
    assert calcular_multiplicador_peso(11 and 29) == 3.0

#Teste função calculo de Rota
def test_atividade_rota_01():
    assert calcular_multiplicador_rota('rs') == 1.0
    assert calcular_multiplicador_rota('sr') == 1.0

def test_atividade_rota_02():
    assert calcular_multiplicador_rota('bs') == 1.2
    assert calcular_multiplicador_rota('SB') == 1.2

def test_atividade_rota_03():
    assert calcular_multiplicador_rota('br') == 1.5
    assert calcular_multiplicador_rota('rb') == 1.5