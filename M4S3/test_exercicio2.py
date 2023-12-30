from exercicio2 import menu
import pytest

def test_menu100():
    assert menu(100) == 9
    
def test_menu101():
    assert menu(101) == 11
    
def test_menu102():
    assert menu(102) == 12

def test_menu103():
    assert menu(103) == 12
    
def test_menu104():
    assert menu(104) == 14
    
def test_menu105():
    assert menu(105) == 17
    
def test_menu200():
    assert menu(200) == 5
    
def test_menu201():
    assert menu(201) == 4