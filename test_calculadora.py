import pytest
from calculadora import Calculadora

def test_suma_positiva():
  cal = Calculadora()
  assert cal.sum(1,2) == 3
  

def test_resta():
  cal = Calculadora()
  assert cal.restar(5,2) == 3

def test_multiplicacion():
  cal = Calculadora()
  assert cal.multiplicar(3,2) == 6